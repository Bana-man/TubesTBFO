def check_tag(tag):
    if tag in tag_list:
        return True
    return False

# LIST TAG HTML
tag_list = ["html", "head", "body", "title", "link", "script", "h1", "h2", "h3", "h4", "h5", "h6", "p", 
            "br", "em", "b", "abbr", "strong","small","hr","div", "a","img","button", "form", "input",
            "ol", "table","tr", "td","th"]

# LIST TAG DALAM HTML
tag_container = []

# HITUNG LINE
line_count = 0

# READ FILE HTML
read_html = open("index.html")

for line in read_html:
    word = line.strip()
    end_index = -1
    line_count += 1

    for i in range(len(line.strip())):
        if word[i] == "<":
            start_index = i
            if end_index != -1:
                if word[end_index+1:start_index] != "":
                    tag_container.append("$")

        # 
        if word[i] == ">":
            end_index = i
            tag_container.append(word[start_index+1:end_index])
            
    #         if word[-1] == ">":
    #             word = word[:-1]
    #         tag_container.append(word[1:])

        #     word = word[1:]
        #     print(word)
            # if word[-1] == ">":
            #     word = word[:-1]
            # if check_tag(word) == False:
            #     print("Invalid tag: ", word)
            # else:
            #     print("Valid tag: ", word)
            
read_html.close()

print("Tag container: ")
print(tag_container, "\n")
print("Line count: ", line_count)