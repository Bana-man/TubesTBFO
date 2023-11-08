def check_tag(tag):
    if tag in tag_list:
        return True
    return False





tag_list = ["html", "head", "body", "title", "link", "script", "h1", "h2", "h3", "h4", "h5", "h6", "p", 
            "br", "em", "b", "abbr", "strong","small","hr","div", "a","img","button", "form", "input",
            "ol", "table","tr", "td","th"]

tag_container = []

# Read HTML file and check if all tags are valid
read_html = open("index.html")

# print((read_html.readline()).strip().split())
for line in read_html:
    # words = line.replace(" ", "")
    # words = words.split()
    word = line.strip()
    for i in range(len(line.strip())):

        if word[i] == "<":
            start_index = i
        if word[i] == ">":
            end_index = i
            tag_container.append(word[start_index+1:end_index])
            # break
            
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

print(tag_container)

# print("words: ", word_in_html)