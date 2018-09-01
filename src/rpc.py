from src import pypresence
import time
import requests
import json

def start(accountName, poePath):
    logsPath = poePath + '\\logs\\Client.txt'

    client_id = '466251900157820929'

    RPC = pypresence.Presence(client_id, pipe=0)
    RPC.connect()
        
    lastLine = ''

    ping = '0ms'
    loc = 'anywhere' 
    lvl = ''
    exp = ''
    nick = ''
    charClass = ''

    print('Your rich presence is running!')

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
                loc = ' '.join(arr[11:]).replace('.', '')

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

        largeIcon = charClass.lower()

        RPC.update(state="Ping: " + ping, details="In " + loc, large_image=largeIcon, large_text=nick + " | level: " + str(lvl) + " | experience: " + str(exp))

        time.sleep(2)

