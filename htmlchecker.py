PDA = open("PDA.txt")
STATE = ((PDA.readline()).rstrip()).split()
#print(STATE)

tag_list = ["html", "head", "body", "title", "link", "script", "h1", "h2", "h3", "h4", "h5", "h6", "p", 
            "br", "em", "b", "abbr", "strong","small","hr","div", "a","img","button", "form", "input",
            "ol", "table","tr", "td","th"]

# Path: htmlchecker.py

def check_tag(tag):
    if tag in tag_list:
        return True
    return False



