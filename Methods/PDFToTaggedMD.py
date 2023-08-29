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
        base_name_without_extension = os.path.splitext(base_name)[0]
        
        print(f"Processing {base_name}...")
        
        text = extract_text_from_pdf(pdf_path)
        
        # Split text into segments
        segments = []
        current_segment = ""
        lines = text.split('\n')
        for line in lines:
            if line.strip() == "" or len(current_segment.split('\n')) >= 6:
                if current_segment.strip() != "":
                    segments.append(current_segment)
                current_segment = ""
            current_segment += line + '\n'
        if current_segment.strip() != "":
            segments.append(current_segment)
        
        # Create a folder for the PDF
        pdf_folder = os.path.join(output_folder, "Scripts", base_name_without_extension)
        os.makedirs(pdf_folder, exist_ok=True)
        
        # Save segments to individual MD files with hashtags
        for idx, segment in enumerate(segments):
            tagged_segment = add_hashtags(segment)
            output_file = os.path.join(pdf_folder, f"{base_name_without_extension}_{idx + 1}.md")
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(tagged_segment)
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
    input_folder = r"C:\Users\ian-s\Repos\MindWork\Scripts"
    output_folder = r"C:\Users\ian-s\Repos\MindWork\Output"
    main(input_folder, output_folder)
