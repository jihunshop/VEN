import requests
import time

token = "ODM4NjA3Mzg2NTI4MDU1MzE2.YI9kTw.YywzpbyJQ4Ssq_3p0yaOdsJXKGE"
channelId = "828642105827655701"

while True:
    requests.post("https://discord.com/api/v8/channels/" +
                  channelId + "/messages", json={"content": "!d bump"},
                  headers={"Authorization": token})
    time.sleep(7210)