import sys
from tasukete import *

# Function to check if a tag is in the tag_list
def check_tag(file_html):
    # List of HTML tags
    tag_attribute_list = ["html", "head", "body", "title", "link", "script", "h1", "h2", "h3", "h4", "h5", "h6", "p", 
                "br", "em", "b", "abbr", "strong", "small", "hr", "div", "a", "img", "button", "form", "input",
                "ol", "table", "tr", "td", "th", "rel", "href", "src", "alt", "type", "action", "type", "method"]

    # List to store tags and attributes
    tag_container = []

    # Count the number of lines
    line_count = 0

    # READ FILE HTML
    # file_html = input("Enter the name of the HTML file: ")

    with open(file_html) as read_html:
        for line in read_html:
            word = line.strip()
            end_index = -1
            line_count += 1

            for i in range(len(line.strip())):
                if word[i] == "<":
                    start_index = i
                    if end_index != -1:
                        tag_container.append("$")

                if word[i] == ">":
                    end_index = i
                    tag_content = word[start_index:end_index + 1]

                    # Process the tag content
                    if tag_content.startswith("<!--"):
                        # Handle comments
                        tag_container.append("!--")
                        tag_container.append("$")
                        tag_container.append("--")
                    elif tag_content.startswith("/"):
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
        

    # print(tag_container_filtered)
    return tag_container_filtered

# ['html', 'head', '!--', '$', '--', 'title', '$', '/title', 'link', 'rel=""', 'href=""', '/', 'script', 'src=""', '$', '/script', '/head', 'body', 'em', '$', '/em', 'hr', '/', 'strong', 'p', '$', '/p', 'p', '$', '/p', 'b', 'p', '$', '/p', 'p', '$', '/p', '/b', '/strong', 'h1', 'abbr', 'title=""', '$', '/abbr', '/h1', 'h2', 'p', '$', '/p', '/h2', 'h3', 'p', '$', '/p', '/h3', 'h4', 'p', '$', '/p', '/h4', 'h5', 'p', '$', '/p', '/h5', 'h6', 'p', '$', '/p', '/h6', 'p', '$', '/p', '/body', '/html']

if len(sys.argv) >= 2:
    input_file = sys.argv[2]
    #print(input_file)
    # print("Nama file input:", input_file)

    pda = open("PDA.txt")
    state = ((pda.readline()).rstrip()).split()
    input_simbol = ((pda.readline()).rstrip()).split()
    stack_simbol = ((pda.readline()).rstrip()).split()
    start_state = ((pda.readline()).rstrip()).split()
    start_stack = ((pda.readline()).rstrip()).split()
    accepting_state =  ((pda.readline()).rstrip()).split()
    kondisi = ((pda.readline()).rstrip()).split()
    pda.close()


    #Bagian ini buat ngebaca fungsi transisi
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
    # print(isiHTML)


    state = start_state
    stack = start_stack
    accepting = accepting_state


    for masukkan in isiHTML:
        flag = False
        for transisi in transition_function:
            #print(transisi)
            if (listToString(state) == currentState(transisi) and stack[-1] == topFromStack(transisi) and masukkan == alphabetInput(transisi)):
                state = nextState(transisi)
                elemen = parsingStack(addToStack(transisi))
                # print(transisi)
                # print(elemen)
                #print(elemen)
                if (elemen[1] != ''):
                        stack.append(elemen[0])
                        # print("ini stack",stack)
                elif (elemen[1] == ''):
                        if (elemen[0] == 'e'): 
                            stack.pop()
                            # print("ini stack",stack)
        
                flag = True
        if (flag == False):
            exit("Syntax Error")

    for i in accepting_state:
        if (state == i):
            exit("Accepted")
            
    exit("Syntax Error")  

else:
    print("Usage: python main.py pda.txt \"[nama_file].html\"")