import os
import csv
from typing import List, Dict

def export_to_csv(flashcards: List[Dict[str, str]], output_folder: str) -> None:
    """Export flashcards to a CSV file."""
    csv_filename = "cards.csv"
    csv_path = os.path.join(output_folder, csv_filename)

    with open(csv_path, mode='w', newline='', encoding='utf-8') as csv_file:
        # Customize the delimiter and quote characters for tab-delimited CSV with double quotes
        csv_writer = csv.writer(csv_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for flashcard in flashcards:
            # Check if both "front" and "back" fields are not empty
            if flashcard.get("front") and flashcard.get("back"):
                csv_writer.writerow([flashcard["front"], flashcard["back"]])

# Example usage:
flashcards = [
    {"front": "Question 1", "back": "Answer 1"},
    {"front": "Question 2", "back": ""},
    {"front": "", "back": "Answer 3"},
    {"front": "Question 4", "back": "Answer 4"},
]

output_folder = ""
export_to_csv(flashcards, output_folder)