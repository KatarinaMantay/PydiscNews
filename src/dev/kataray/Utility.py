PROCESSED_LINKS_FILE = "readLinks.txt"

def loadReadLinks():

    try:
        with open(PROCESSED_LINKS_FILE, "r") as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        return set()

def saveLink(link):
    with open(PROCESSED_LINKS_FILE, "a") as file:
        file.write(link + "\n")

def isNewLink(link, processed_links):
    return link not in processed_links
