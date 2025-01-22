import requests
from Config import DISCORD_WEBHOOK_URL

def send_to_discord(title):

    message = {
        "content": f"New Tweet: {title}"
    }

    sendToDisc = requests.post(DISCORD_WEBHOOK_URL, json=message)

    if sendToDisc.status_code == 204:
        print("Tweet sent to webhook")
    else:
        print("failed to send msg: ", sendToDisc.status_code)
