# Function to check if a tag is in the tag_list
def check_tag(tag):
    return tag in tag_list

# List of HTML tags
tag_list = ["html", "head", "body", "title", "link", "script", "h1", "h2", "h3", "h4", "h5", "h6", "p", 
            "br", "em", "b", "abbr", "strong","small","hr","div", "a","img","button", "form", "input",
            "ol", "table","tr", "td","th"]

# List to store tags and attributes
tag_container = []

# Count the number of lines
line_count = 0

# READ FILE HTML
with open("index.html") as read_html:
    for line in read_html:
        word = line.strip()
        end_index = -1
        line_count += 1

        for i in range(len(line.strip())):
            if word[i] == "<":
                start_index = i
                if end_index != -1:
                    if word[end_index + 1:start_index] != "":
                        tag_container.append("$")

            if word[i] == ">":
                end_index = i
                tag_content = word[start_index + 1:end_index]

                # Process the tag content
                if tag_content.startswith("/"):
                    # Handle closing tags
                    tag_container.append("/" + tag_content[1:])
                else:
                    # Handle opening tags
                    tag_container.append(tag_content)
                    if " " in tag_content:
                        # If the tag has attributes, split them correctly
                        attributes = tag_content.split(" ", 1)[1]
                        tag_container.extend(attributes.split(' '))

print("Tag container:")
print(tag_container)
print("Line count:", line_count)
['html', 'head', 'title', '$', '/title', 'link', 'rel="stylesheet"', 'href=""', '/', 'script', 'src="#src"', '/script', '/head', 'body', 'em', '$', '/em', 'hr /', '/', 'strong', 'p', '$', '/p', 'p', '$', '/p', 'b', 'p', '$', '/p', 'p', '$', '/p', '/b', '/strong', 'h1', 'abbr', 'title="inijudul"', '$', '/abbr', '/h1', 'h2', 'p', '/p', '/h2', 'h3', 'p', '/p', '/h3', 'h4', 'p', '/p', '/h4', 'h5', 'p', '/p', '/h5', 'h6', 'p', '/p', '/h6', 'p', '/p', '/body', '/html']
