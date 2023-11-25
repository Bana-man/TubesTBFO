import sys
from tasukete import *

class bcolors:
    fail = '\033[91m'     # fail bright red
    success = '\033[92m'  # success bright green
    elmt = '\033[33m'     # tags/attributes yellow
    endc = '\033[0m'      # end color

# Function to check if a tag is in the tag_list
def check_tag(file_html):
    # List of HTML tags
    tag_attribute_list = ["html", "head", "body", "title", "link", "script", "h1", "h2", "h3", "h4", "h5", "h6", "p", 
                "br", "em", "b", "abbr", "strong", "small", "hr", "div", "a", "img", "button", "form", "input",
                "ol", "table", "tr", "td", "th", "rel", "href", "src", "alt", "type", "action", "type", "method"]

    # List tags + attributes
    tag_container = []

    # Hitung line code
    line_count = 0

    # Flag untuk comment
    in_comment = False

    with open(file_html) as read_html:
        for line in read_html:
            word = line.strip()
            end_index = -1
            line_count += 1

            for i in range(len(line.strip())):
                if word[i:i + 4] == "<!--":
                    in_comment = True
                    start_index = len(word) - 1

                if word[i:i + 3] == "-->":
                    end_index = len(word) - 1
                    in_comment = False
                    tag_container.append("!--")
                    tag_container.append("$")
                    tag_container.append("--")

                if not in_comment:
                    if word[i] == "<":
                        start_index = i
                        if end_index != -1:
                            tag_container.append("$")

                    if word[i] == ">":
                        end_index = i
                        tag_content = word[start_index:end_index + 1]

                        if tag_content.startswith("/"):
                            # Handle closing tags
                            tag_container.append(tag_content[1:])
                        else:
                            # Handle opening tags
                            tag_name = tag_content.split()[0]
                            tag_container.append(tag_name)

                            attributes_list = []
                            # Process attributes
                            if " " in tag_content:
                                attributes = tag_content.split(" ", 1)[1]
                                attributes_list = attributes.split()

                            for i, attr in enumerate(attributes_list):
                                if "=" in attr:
                                    attr_name, attr_value = attr.split("=", 1)
                                    if attr_name.lower() != "method" and '"' in attr_value:
                                        attr_value = '""'
                                    elif attr_name.lower() == "method" and attr_value.lower() != "get":
                                        attr_value = '"POST"'
                                    elif attr_name.lower() == "method" and attr_value.lower() != "post":
                                        attr_value = '"GET"'

                                    attributes_list[i] = f"{attr_name}={attr_value}"

                            tag_container.extend(attributes_list)


    tag_container_filtered = []

    for tags in tag_container:
        if tags.startswith("<") and tags.endswith(">"):
            tag_container_filtered.append(tags[1:-1])
        elif tags.startswith("<") :
            tag_container_filtered.append(tags[1:])
        elif tags.startswith("/"):
            tag_container_filtered.append("/")
        elif tags.endswith(">") and tags[:-1] not in tag_attribute_list:
            continue
        elif tags.endswith(">"):
            tag_container_filtered.append(tags[:-1])
        else:
            tag_container_filtered.append(tags)
        
    return tag_container_filtered

if len(sys.argv) >= 2:
    input_file = sys.argv[2]

    pda = open("PDA.txt")
    state = ((pda.readline()).rstrip()).split()
    input_simbol = ((pda.readline()).rstrip()).split()
    stack_simbol = ((pda.readline()).rstrip()).split()
    start_state = ((pda.readline()).rstrip()).split()
    start_stack = ((pda.readline()).rstrip()).split()
    accepting_state =  ((pda.readline()).rstrip()).split()
    kondisi = ((pda.readline()).rstrip()).split()
    pda.close()


    # Read fungsi transisi
    pda = open("PDA.txt")
    temp = pda.readlines()
    pda.close()

    count = 0
    transition_function = []
    panjang_baris = len(temp)
    for i in range( panjang_baris):
        if i >= 7:        
            transition_function.append(temp[i].rstrip().split())

    isiHTML = check_tag(input_file)
    print(f"{bcolors.elmt}{isiHTML}{bcolors.endc}")

    state = start_state
    stack = start_stack
    accepting = accepting_state

    for masukkan in isiHTML:
        flag = False
        for transisi in transition_function:
            if (listToString(state) == currentState(transisi) and stack[-1] == topFromStack(transisi) and masukkan == alphabetInput(transisi)):
                state = nextState(transisi)
                elemen = parsingStack(addToStack(transisi))

                if (elemen[1] != ''):
                        stack.append(elemen[0])
                elif (elemen[1] == ''):
                        if (elemen[0] == 'e'): 
                            stack.pop()
        
                flag = True

        if (flag == False):
            exit(f"{bcolors.fail}Syntax Error{bcolors.endc}")


    for i in accepting_state:
        if (state == i):
            exit(f"{bcolors.success}Accepted{bcolors.endc}")
            
    exit(f"{bcolors.fail}Syntax Error{bcolors.endc}")

else:
    print(f"{bcolors.fail}Usage: python main.py pda.txt \"[nama_file].html\"{bcolors.endc}")