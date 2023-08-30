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
            print("returned here 1")
            break
        if ls[index][1] == offset_now+1:
            node.children.append(build_tree(ls,current_index=index))

    return node

def generate_tree(lines):
    indent_levels = get_indentation_level(lines)
    print(indent_levels)
    
    return build_tree(indent_levels)


markdown_content = """
# Ai-900

## NLP processing Azure

### Answer to Text

- chat

	- best practice

		- 1 database for FAQ
		- different channels are connected to it
		- workflow with steps
		- customer has the option to go back to top of procedure

	- text to speech
	- speech to text

### Translate Text

- translations

### text analysis

- recap text

### sentiment analysis

- mood

### speech recognition

- voice

## Workloads for Ai

### Solvable problems

- ML
- Anomaly detect
- comp vision 
- NLP

### Important factors

- Understanding the Situation
- Understanding core problems

## Features on Azure
more example file
"""
def print_tree(node, indent=0):
    
    print("  " * indent + node.content)
    for child in node.children:
        print_tree(child, indent + 1)

lines = markdown_content.split('\n')
tree=generate_tree(lines)
print_tree(tree)



