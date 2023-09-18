
import os
import pdfplumber
import openai
import csv
from typing import List, Dict

# Diese Funktion sollte den Text aus einem PDF extrahieren
def textfrompdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = []
        for page in pdf.pages:
            text += [page.extract_text()]

    return text


def gpt_flashcards(pages):
    # Teilen Sie den Eingabetext in Segmente von x Zeilen auf
    

    # Liste für die Flashcards erstellen
    flashcard_list = []

    for segment in pages:
        # Führen Sie einen API-Request mit dem aktuellen Segment und dem Prompt durch
        response = make_api_request(segment)

        # Verarbeiten Sie die API-Antwort, um Flashcards zu extrahieren
        flashcards = extract_flashcards(response)
        # Fügen Sie die Flashcards der Liste hinzu
        flashcard_list.extend(flashcards)

    return flashcard_list


def make_api_request(text):
    print(text)

    prompt = '''Erstelle eine Lernkarte im Markdown-Format mit einer Vorder- und Rückseite. Verwende HTML-Tags, um die Karten zu definieren: `<vorn></vorn>` für die Vorderseite und `<hinten></hinten>` für die Rückseite. Geben Sie nur den grundlegenden Karten-Strukturcode zurück.

Für die Frage auf der Vorderseite und die Musterantwort auf der Rückseite könnten folgende Beispiele dienen:
<vorn>Was ist die Hauptstadt von Frankreich?</vorn>
<hinten>Die Hauptstadt von Frankreich ist Paris.</hinten>

Fügen Sie gerne zusätzliches Wissen zum Thema hinzu, aber halten Sie die Karten kurz und prägnant. Wenn Sie denken, dass eine Karte nicht ausreichend ist, können Sie auch mehrere Karten erstellen, um das Thema umfassender abzudecken.
hier ist der text:'''

    apikey = "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"  # Replace with your OpenAI API key
    openai.api_key = apikey
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt+text},
        ]
    )

    # Extract the generated text from the OpenAI response
    api_response = response['choices'][0]['message']['content']
    print(api_response)
    return api_response


def extract_flashcards(api_response):
    flashcards = []

    # Annahme: Die API-Antwort enthält Flashcards in einem benutzerdefinierten Format
    # Sie müssen den Code hier anpassen, um das genaue Format zu analysieren
    start_tag = "<vorn>"
    end_tag = "<hinten>"

    while start_tag in api_response and end_tag in api_response:
        start_index = api_response.index(start_tag)
        end_index = api_response.index(end_tag)

        front = api_response[start_index + len(start_tag):end_index]
        back = api_response[end_index + len(end_tag):]

        flashcards.append({"front": front, "back": back})

        # Entfernen Sie die extrahierte Flashcard aus der API-Antwort
        api_response = api_response[end_index + len(end_tag):]

    return flashcards


def export_to_csv(flashcards: List[Dict[str, str]], output_folder: str) -> None:
    """Export flashcards to a CSV file."""
    csv_filename = "cards.csv"
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
        
        pages = textfrompdf(pdf_path)
        # Extract flashcards from the PDF
        flashcards = gpt_flashcards(pages)

        # Export flashcards to a CSV file
        export_to_csv(flashcards, output_folder)

if __name__ == "__main__":
    input_folder = r"/home/ian/Documents/Repository/MindWork/Anki"  # Set your input folder path
    output_folder = r"/home/ian/Documents/Repository/MindWork/Anki"  # Set your output folder path
    main(input_folder, output_folder)
