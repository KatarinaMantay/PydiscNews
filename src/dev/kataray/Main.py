import time
from RSSFetcher import getTweetInfo
from DiscordNotifier import send_to_discord
from src.dev.kataray.Utility import isNewLink, loadReadLinks, saveLink

def main():
    readLinks = loadReadLinks()

    while True:

        title, link = getTweetInfo()

        if isNewLink(link, readLinks):
            send_to_discord(title)

            readLinks.add(link)
            saveLink(link)
        else:
            print("no new news atm")

        time.sleep(600)

if __name__ == "__main__":
    main()
