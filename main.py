import sys
from tasukete import *
import os

# Hitung line code
arrayOfLineNumber = []
class bcolors:
    fail = '\033[91m'     # fail bright red
    success = '\033[92m'  # success bright green
    elmt = '\033[33m'     # tags/attributes yellow
    endc = '\033[0m'      # end color

def check_tag(file_html):
    # List tags + attributes
    tag_container = []

    # Hitung line code
    line_count = 0

    # Flag untuk comment
    in_comment = False

    with open(file_html, encoding="utf-8") as read_html:
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
                    arrayOfLineNumber.append(line_count)
                    tag_container.append("$")
                    arrayOfLineNumber.append(line_count)
                    tag_container.append("--")
                    arrayOfLineNumber.append(line_count)

                if not in_comment:
                    if word[i] == "<":
                        start_index = i
                        if end_index != -1:
                            tag_container.append("$")
                            arrayOfLineNumber.append(line_count)

                    if word[i] == ">":
                        end_index = i
                        tag_content = word[start_index:end_index + 1]

                        if tag_content.startswith("/"):
                            # Handle closing tags
                            tag_container.append(tag_content[1:])
                            arrayOfLineNumber.append(line_count)
                        else:
                            tag_name = tag_content.split()[0]
                            tag_container.append(tag_name)
                            arrayOfLineNumber.append(line_count)

                            attributes_list = []

                            # Process attributes
                            if " " in tag_content:
                                attributes = tag_content.split(" ", 1)[1]
                                attributes_list = attributes.split()
                                for i in range(len(attributes_list)):
                                    arrayOfLineNumber.append(line_count)

                            # print(attributes_list)
                            i = 0
                            while i < len(attributes_list):
                                if attributes_list[i].count('"') % 2 != 0:
                                    attributes_list[i] = attributes_list[i] + attributes_list[i+1]
                                    attributes_list.pop(i+1)
                                    arrayOfLineNumber.pop(i+1)
                                else :
                                    i += 1

                            # print(attributes_list)
                            for i, attr in enumerate(attributes_list):
                                if "=" in attr:
                                    attr_name, attr_value = attr.split("=", 1)
                                    attr_value = attr_value.replace(">","")
                                    tag_name = tag_name.replace("<","")

                                    if attr_name.lower() not in ["type", "method"]:
                                        attr_value = '""'
                                    else:
                                        if tag_name == "button" and attr_name == "type":
                                            if "submit" in attr_value.lower():
                                                attr_value = '"submit"'
                                            elif "reset" in attr_value.lower():
                                                attr_value = '"reset"'
                                            elif "button" in attr_value.lower():
                                                attr_value = '"button"'
                                            elif attr_value.lower() not in ["submit", "reset", "button"]:
                                                attr_value = '""'

                                        if tag_name == "input" and attr_name == "type":
                                            if "text" in attr_value.lower():
                                                attr_value = '"text"'
                                            elif "password" in attr_value.lower():
                                                attr_value = '"password"'
                                            elif "email" in attr_value.lower():
                                                attr_value = '"email"'
                                            elif "number" in attr_value.lower():
                                                attr_value = '"number"'
                                            elif "checkbox" in attr_value.lower():
                                                attr_value = '"checkbox"'
                                            elif attr_value.lower() not in ["text", "password", "email", "number", "checkbox"]:
                                                attr_value = '""'
                                        
                                        if attr_name == "method":
                                            if "get" in attr_value.lower():
                                                attr_value = '"GET"'
                                            elif "post" in attr_value.lower():
                                                attr_value = '"POST"'
                                            elif attr_value.lower() not in ["get", "post"]:
                                                attr_value = '""'
                                    
                                    attributes_list[i] = f"{attr_name}={attr_value}"

                            tag_container.extend(attributes_list)

    # print(tag_container)
    tag_container_filtered = []
    panjang = len(tag_container)
    
    for i in range(panjang):
        if len(tag_container[i]) == 1 and not tag_container[i].startswith("$"):
            arrayOfLineNumber.pop(i)
            continue
        elif tag_container[i].startswith("<") and tag_container[i].endswith(">"):
            tag_container_filtered.append(tag_container[i][1:-1])
        elif tag_container[i].startswith("<") :
            tag_container_filtered.append(tag_container[i][1:])
        elif tag_container[i].startswith("/"):
            tag_container_filtered.append("/")
        elif tag_container[i].endswith(">"):
            tag_container_filtered.append(tag_container[i][:-1])
        else:
            tag_container_filtered.append(tag_container[i])
    
    return tag_container_filtered

if len(sys.argv) == 3:
    if sys.argv[1] != "PDA.txt":
        exit(f"{bcolors.fail}Usage: python main.py PDA.txt \"[nama_file].html\"{bcolors.endc}")
    else:
        path = os.getcwd() + "\\" + sys.argv[2]
        if not os.path.isfile(path):
            print(f"{bcolors.fail}File {sys.argv[2]} tidak ditemukan{bcolors.endc}\n")
            exit(f"{bcolors.fail}Usage: python main.py PDA.txt \"[nama_file].html\"{bcolors.endc}")
        else:
            input_file = sys.argv[2]
            isiHTML = check_tag(input_file)

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


            state = start_state
            stack = start_stack
            accepting = accepting_state
            idx = 0
            for masukkan in isiHTML:
                flag = False
                # print(stack)
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
                idx += 1

                if (flag == False):
                    # print(arrayOfLineNumber)
                    # print(isiHTML)
                    line_error = arrayOfLineNumber[idx-1]
                    print(f"{bcolors.fail}Syntax Error\n{bcolors.endc}")
                    f = open(sys.argv[2], 'r')
                    for i in range(line_error):
                        line = f.readline()
                    exit(f"{bcolors.fail}Terjadi kesalahan ekspresi pada line {line_error} : {line.strip()}{bcolors.endc}")


            for i in accepting_state:
                if (state == i):
                    exit(f"{bcolors.success}Accepted{bcolors.endc}")


            print(f"{bcolors.fail}Syntax Error{bcolors.endc}\n")
            print(f"{bcolors.fail}Terjadi kesalahan ekspresi pada line {max(arrayOfLineNumber)} : (Tag {stack[-1]} tidak memiliki penutup){bcolors.endc}")
            exit()
else:
    print(f"{bcolors.fail}Usage: python main.py PDA.txt \"[nama_file].html\"{bcolors.endc}")