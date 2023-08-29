import os
import re

from tagging import add_hashtags
#working as intended 


def split_text(text, output_root, max_indent_level=3):
    # Split the text into sections based on indent level
    sections = re.split(r'\n(?= *#+ )', text)
    
    # Check if any section has more than max_indent_level indent levels
    for section in sections:

        
        indent_level = len(re.match(r' *#+', section).group()) // 2
        if indent_level > max_indent_level:
            split_text(section, output_root, max_indent_level)
        else:
            # Strip hashtags from the topmost line of the section
            section = re.sub(r'^ *#+\s+#', '#', section)
            
            # Create a new file for the section with a filename based on the topmost line stripped of hashtags
            filename = re.sub(r'[^\w\s-]', '', section.split('\n')[0]).strip().replace(' ', '_') + '.md'
            output_path = os.path.join(output_root, filename)
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, 'w') as f:
                # Add hashtags before processing
                section = add_hashtags(section)
                f.write(section)



def process_markdown_file(file_path, output_root, path):
    with open(file_path, 'r') as f:
        text = f.read()
    
    
    
    # Split the text into sections with no more than 3 indent levels using a recursive function
    split_text(text, output_root)
    
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

    input_folder_path = r"C:\Users\ian-s\Repos\MindWork\Xmind"
    output_folder_path = r"C:\Users\ian-s\Repos\MindWork\Output"
    
    
    process_folder(input_folder_path, output_folder_path)
