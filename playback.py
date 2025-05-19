import pyautogui
import time
from pynput import keyboard
from pynput.mouse import Controller
mouse = Controller()

status = "idle"

def readCommandFile():
    with open("mouse_log.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            parts = line.split(",")
            if (parts[0].strip() == "mm"):
                time.sleep(0.01)
                mouse.position = (int(parts[1].strip()), int(parts[2].strip()))  
                # pyautogui.moveTo(int(parts[1].strip()), int(parts[2].strip()), duration=0)    
            elif (parts[0].strip() == "mc"):
                if (parts[3].strip() == "Button.left"):
                    if (parts[4].strip() == "down"):
                        pyautogui.mouseDown()
                    else:
                        pyautogui.mouseUp()
            elif (parts[0].strip() == "kp"):
                command = parts[1].strip().replace("'", "")  
                command = command.replace("Key.", "")
                pyautogui.press(command)
            elif (parts[0].strip() == "kd"):
                command = parts[1].strip().replace("'", "")
                command = command.replace("Key.", "")
                pyautogui.keyDown(command)
            elif (parts[0].strip() == "kr"):
                command = parts[1].strip().replace("'", "")
                command = command.replace("Key.", "")
                pyautogui.keyUp(command)
            elif (parts[0].strip() == "d"):
                time.sleep(float(parts[1].strip()))

def on_press(key):  
    global status
    print(status)
    if (key == keyboard.Key.tab and status == "idle"):
        status = "running"
        readCommandFile()
    elif (key == keyboard.Key.tab and status == "running"):
        return False


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()