import os
import re
from tagging import add_hashtags
#working as intended 


class TreeNode:
    def __init__(self, content):
        self.content = content
        self.children = []

def count_char_until_stop(line, char_to_count,offset=0):
    count = 0
    stop_found = False
    stripped_text = ""

    for char in line:
        if char == char_to_count:
            count += 1
            continue
        if char!= char_to_count:
            break
    stripped_text=line[count:-1]+line[-1]
    return [stripped_text, count+offset]

def get_indentation_level(lines):
    ls=[]
    current=0
    for line in lines:
        if line=="":
            continue
        if line[0]=="#":
            #mofo usiing hashtags
            ls.append(count_char_until_stop(line,"#"))
            current=ls[-1][1]#last elements indent
            continue
        else:
            ls.append(count_char_until_stop(line,"\t",offset=current+1))#tab and first one does not have tab

    return(ls)


def build_tree(ls,current_index=0):
    now=ls[current_index]
    node = TreeNode(now[0])
    offset_now= now[1]
    for index in range(current_index +1,len(ls)):
        if ls[index][1] < offset_now+1:
            
            break
        if ls[index][1] == offset_now+1:
            node.children.append(build_tree(ls,current_index=index))

    return node

def generate_tree(lines):
    indent_levels = get_indentation_level(lines)
    return build_tree(indent_levels)

def distance_to_closest_leaf(node):
    if node.children==[]:  # Node is a leaf
        return 0
    dinstances=[0]  # Initialize with a large value
    for child in node.children:
        dinstances.append(distance_to_closest_leaf(child) + 1)
    min_distance = max(dinstances)
    return min_distance

def tree_toStr(node, depth=0):
    tree_str = "  " * depth + node.content + "\n"
    
    for child in node.children:
        tree_str += tree_toStr(child, depth + 1)
    return tree_str

def split_tree(node, output_root, path="", max_indent_level=4,toplevelname=""):
    path += node.content.strip().replace(' ', '_')
    filename = re.sub(r'[^\w\s-]', '', node.content.split('\n')[0]).replace("-","").strip(" ").replace(" ","")
    toplevelname+=f" #{filename}"
    filename=filename+".md"
    depths=[]
    for child in node.children:
        depths.append([distance_to_closest_leaf(child),child])
        #populate depth ls

    above_depths = [pair for pair in depths if pair[0] > max_indent_level]
    below_depths = [pair for pair in depths if pair[0] <= max_indent_level]
    
    thisTx=""
    if below_depths != []:
        for element in below_depths:
            thisTx+=tree_toStr(element[1])
            
        tagged = add_hashtags(thisTx)

        output_root=output_root.strip().replace(' ', '_')
        full_output_path = os.path.join(output_root, path)
        os.makedirs(full_output_path, exist_ok=True)  # Create the necessary folders along the path
        output_path = os.path.join(full_output_path, filename)

        
        with open(output_path, 'w') as f:
            f.write(toplevelname)
            f.write(tagged)

    if above_depths != []:
        for element in above_depths:
            split_tree(element[1],output_root,path=path,toplevelname=toplevelname)


def split_text(text, output_root, max_indent_level=2):
    lines = text.split('\n')
    tree=generate_tree(lines)
    split_tree(tree,output_root,max_indent_level=max_indent_level)



def process_markdown_file(file_path, output_root):
    with open(file_path, 'r') as f:
        text = f.read()
    
    split_text(text, output_root)
    print(f"Processed '{file_path}': Built tree structure")




def process_folder(input_folder, output_folder):
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, input_folder)
                output_path = os.path.join(output_folder, os.path.splitext(relative_path)[0])
                process_markdown_file(file_path, output_path)


if __name__ == "__main__":

    input_folder_path = r"C:\Users\ian-s\Desktop\MindWork\Xmind"
    output_folder_path = r"C:\Users\ian-s\Desktop\MindWork\Output"
    process_folder(input_folder_path, output_folder_path)
