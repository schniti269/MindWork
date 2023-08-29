from tagging import add_hashtags
import os
import PyPDF2  # PyPDF2 library for PDF handling

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def process_pdf(pdf_path, output_folder):
    try:
        base_name = os.path.basename(pdf_path)
        
        print(f"Processing {base_name}...")
        
        text = extract_text_from_pdf(pdf_path)
        tagged_text = add_hashtags(text)
        
        # Save tagged text to an MD file
        output_file = os.path.join(output_folder, f"{base_name}.md")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(tagged_text)
            print(f"Saved {output_file}")
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")

def main(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    pdf_files = [file for file in os.listdir(input_folder) if file.endswith(".pdf")]
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_file)
        process_pdf(pdf_path, output_folder)
        print(f"Processed {pdf_file}")

if __name__ == "__main__":
    input_folder = r"C:\Users\ian-s\Desktop\Mindwork\Scripts"
    output_folder = r"C:\Users\ian-s\Desktop\Mindwork\Output"
    main(input_folder, output_folder)
