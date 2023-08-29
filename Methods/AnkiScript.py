import os
import re
import spacy

#not tested

# Load the multilingual language model for spaCy
nlp = spacy.load("xx_ent_wiki_sm")  # "xx" represents the multilingual language identifier


def add_hashtags(text):
    doc = nlp(text)
    new_tokens = []
    for token in doc:
        if token.pos_ == "NOUN":
            new_tokens.append(f"#{token.text}")
        else:
            new_tokens.append(token.text)
    return " ".join(new_tokens)

def process_markdown_file(file_path, output_root, path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.readlines()
    
    current_folder = output_root
    
    header_pattern = re.compile(r"^(#+)\s(.+)$")
    indentation_pattern = re.compile(r"^\s+")
    
    stack = []
    
    for line in content:
        if header_pattern.match(line):
            header_level, header_text = header_pattern.findall(line)[0]
            header_level = len(header_level)
            header_text = add_hashtags(header_text.strip())
            
            # Replace characters not allowed in Windows directory names
            invalid_chars = r'<>:"/\|?*'
            for char in invalid_chars:
                header_text = header_text.replace(char, "_")
            
            if stack:
                while stack and stack[-1][0] >= header_level:
                    stack.pop()
                    current_folder = os.path.dirname(current_folder)
            
            stack.append((header_level, header_text))
            
            new_folder = os.path.join(current_folder, header_text)
            if not os.path.exists(new_folder):
                os.makedirs(new_folder)
            current_folder = new_folder
            
            if header_level <= 3:
                tree_depth = header_level
            
            # Use the name of the top-level header as the filename
            top_level_name = stack[0][1]
            new_file_path = os.path.join(current_folder, f"{top_level_name}.md")
            with open(new_file_path, "w", encoding="utf-8") as new_file:
                path_header = " > ".join([header for _, header in stack])
                new_file.write(f"{path_header}\n\n{'#'*header_level} {header_text}\n\n")
        
        elif indentation_pattern.match(line):
            content_line = line.strip()
            if content_line:
                # Write the content to the current markdown file
                with open(new_file_path, "a", encoding="utf-8") as new_file:
                    new_file.write(f"{content_line}\n")
    
    print(f"Processed '{file_path}': Built tree structure")

def process_folder(input_folder, output_folder):
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, input_folder)
                output_path = os.path.join(output_folder, os.path.splitext(relative_path)[0])
                process_markdown_file(file_path, output_path, relative_path.replace(os.path.sep, " > "))


if __name__ == "__main__":
    input_folder_path = r"C:\Users\ian-s\Desktop\xmind"
    output_folder_path = r"C:\Users\ian-s\Desktop\output"
    process_folder(input_folder_path, output_folder_path)