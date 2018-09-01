import json
from src import rpc

def init():
    accountName = input("Input your account name: ")
    path = input("Input path to your Path of Exile directory: ")

    jsonObj = {
        'accountName': accountName,
        'path': path
    }

    with open('src/config/config.json', 'w') as outfile:
        json.dump(jsonObj, outfile)
    
    start()


def start():
    with open('src/config/config.json', 'r') as f:
        f = ' '.join(f.readlines())

        if f != "":
            data = json.loads(f)
            accountName = data["accountName"]
            poePath = data["path"]

            rpc.start(accountName, poePath)
        else:
            init()

start()
