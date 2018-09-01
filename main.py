from pypresence import Presence
import time
import requests
import json

client_id = 'your_client_id'

logsPath = 'path_to_path_of_exile\\logs\\Client.txt'

accountName = 'FollowTM'

RPC = Presence(client_id)
RPC.connect()
    
lastLine = ''

ping = '0ms'
loc = '' 
lvl = ''
exp = ''
nick = ''
league = ''
charClass = ''

while True:
    f = open(logsPath, 'r', encoding="utf8")
    lines = ""

    try:
        lines = f.readlines()
    except:
        print("error")

    if lines[-1] != lastLine:
        line = lines[-1]

        if 'Connect time to instance server was' in line:
            arr = line.split(" ")
            ping = ' '.join(arr[13:])
        
        if 'You have entered' in line:
            arr = line.split(" ")
            loc = ' '.join(arr[11:])

    lastLine = lines[-1]

    r = requests.get('https://www.pathofexile.com/character-window/get-characters?accountName=' + accountName)
    res = json.loads(r.text)

    for obj in res:
        if "lastActive" in obj:
            nick = obj["name"]
            lvl = obj["level"]
            charClass = obj["class"]
            exp = obj["experience"]
            league = obj["league"]

    largeIcon = 'ranger'

    if charClass == "Ranger":
        largeIcon = 'ranger'

    RPC.update(state="Ping: " + ping, details="In " + loc, large_image=largeIcon, large_text=nick + " | level: " + str(lvl) + " | experience: " + str(exp))

    time.sleep(2)

