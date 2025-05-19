from pynput import mouse, keyboard
import time

last_move_time = 0
move_delay = 0.2  # (unit = seconds)
lastCommands = 0
status = "idle"

def initializeLastCommands():
    global lastCommands
    lastCommands = time.time()

def writeToFile(input):
    if (status == "running"):
        with open("mouse_log.txt", "a") as f:
                f.write(input)
    
def checkTime():
    global lastCommands
    if (time.time() - lastCommands > 0.25):
        writeToFile("d, " + str(time.time() - lastCommands) + "\n")  
    lastCommands = time.time()    


def on_move(x, y):
    global last_move_time       
    now = time.time()   
    if now - last_move_time > move_delay:
        checkTime()
        writeToFile("mm, " + str(x) + ", " + str(y) + "\n")

def on_click(x, y, button, pressed):
    pressString = ""
    if pressed:
        pressString = "down"
    else:
        pressString = "up"
    checkTime()
    writeToFile("mc, " + str(x) + ", " + str(y) + ", " + str(button) + ", "  + pressString + "\n")
    
# def on_scroll(x, y, dx, dy):
#     print(f"Mouse scrolled at ({x}, {y}) with delta ({dx}, {dy})")

pressed_counts = {}

def on_press(key):
    checkTime()
    if key not in pressed_counts:
        pressed_counts[key] = 1
        writeToFile("kp, " + str(key) + "\n")
    else:
        pressed_counts[key] += 1
        writeToFile("kd, " + str(key) + "\n")

def on_release(key):
    global status
    checkTime()
    if key in pressed_counts:
        if pressed_counts[key] > 1:
            writeToFile("kr, " + str(key) + "\n")
        pressed_counts.pop(key)
    if key == keyboard.Key.tab:
        if status == "idle":
            status = "running"
        elif status == "running":
            print("TAB pressed. Stopping listeners.")
            mouse_listener.stop()
            keyboard_listener.stop()

initializeLastCommands()
    
mouse_listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    # on_scroll=on_scroll
)
mouse_listener.start()

keyboard_listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release,
)
keyboard_listener.start()

mouse_listener.join()
keyboard_listener.join()
