import random
import os
import pdfplumber
import csv
from tagging import gap_text
from typing import List, Dict

def generate_flashcard(text: str) -> Dict[str, str]:
    """Generate a flashcard with a random card type."""
    # Select a random card type
    card_type = random.choice(types_of_cards)

    # Generate the flashcard based on the selected card type
    flashcard = {
        "front": card_type(text),
        "back": text
    }

    return flashcard

def extract_flashcards_from_pdf(pdf_path: str) -> List[Dict[str, str]]:
    """Extract flashcards from a PDF file."""
    with pdfplumber.open(pdf_path) as pdf:
        flashcards = []

        # Iterate through pages
        for page in pdf.pages:
            # Iterate through text boxes on the page
            for textbox in page.extract_textboxes():
                text = textbox.extract_text()

                # Generate a flashcard for each text box
                flashcard = generate_flashcard(text)
                flashcards.append(flashcard)

    return flashcards

def export_to_csv(flashcards: List[Dict[str, str]], output_folder: str) -> None:
    """Export flashcards to a CSV file."""
    csv_filename = os.path.splitext(pdf_file)[0] + ".csv"
    csv_path = os.path.join(output_folder, csv_filename)

    with open(csv_path, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ["front", "back"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for flashcard in flashcards:
            writer.writerow(flashcard)

def main(input_folder: str, output_folder: str) -> None:
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all PDF files in the input folder
    pdf_files = [f for f in os.listdir(input_folder) if f.endswith(".pdf")]

    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_file)
        
        # Extract flashcards from the PDF
        flashcards = extract_flashcards_from_pdf(pdf_path)

        # Export flashcards to a CSV file
        export_to_csv(flashcards, output_folder)

if __name__ == "__main__":
    input_folder = r"C:\Users\ian-s\Desktop\MindWork\Anki"
    output_folder = r"C:\Users\ian-s\Desktop\MindWork\Anki"
    types_of_cards = [gap_text]  # Define your card types here
    main(input_folder, output_folder)
