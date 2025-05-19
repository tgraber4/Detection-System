import pyautogui
import time
import threading
from pynput import keyboard
from pynput.mouse import Controller

mouse = Controller()
status = "idle"
runner_thread = None

def readCommandFile():
    global status
    with open("mouse_log.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if (status == "stop"):
                break
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
    global status, runner_thread
    if (key == keyboard.Key.tab and status == "idle"):
        status = "running"
        runner_thread = threading.Thread(target=readCommandFile)
        runner_thread.start()
    elif (key == keyboard.Key.tab and status == "running"):
        print("Program stopped")
        status = "stop"
        return False


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()