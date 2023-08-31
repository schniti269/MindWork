import os
import pdfplumber
from tagging import add_hashtags

# Function to split a PDF into pages
def split_PDF_into_pages(pdf_path, output_folder):

    title = os.path.splitext(os.path.basename(pdf_path))[0]
    os.makedirs(output_folder, exist_ok=True)

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            # Extract text from the page
            page_text = page.extract_text()

            
            # Generate hashtags from the extracted text
            hashtags = add_hashtags(page_text, onlytags=True)
            
            # Create a markdown content with hashtags and PDF link
            markdown_content = f"\n![[{os.path.basename(pdf_path)}#page={page_num}]]"
            markdown_content += hashtags

            # Save markdown file with tags and PDF link
            markdown_filename = os.path.join(output_folder, f"{title}_{page_num + 2}.md")
            with open(markdown_filename, "w", encoding="utf-8") as markdown_file:
                markdown_file.write(markdown_content)

def main(input_folder, output_folder):
    pdf_files = [f for f in os.listdir(input_folder) if f.endswith(".pdf")]

    for pdf_file in pdf_files:
        print("processing: "+pdf_file)
        pdf_path = os.path.join(input_folder, pdf_file)
        output_subfolder = os.path.join(output_folder, os.path.splitext(pdf_file)[0])
        split_PDF_into_pages(pdf_path, output_subfolder)

if __name__ == "__main__":
    input_folder = r"C:\Users\ian-s\Desktop\MindWork\Scripts"
    output_folder = r"C:\Users\ian-s\Desktop\MindWork\Output"
    main(input_folder, output_folder)
