# Detection and Replica System
---------------------------------

Youtube: https://www.youtube.com/watch?v=J7vPxMJME8c

This program records all mouse movements, mouse clicks, and keyboard actions. Then it generates a command file that you can play back those same actions later.

Allows you to replicate all actions performed during the recording process.

Setup: <br>
1.) pip install pyautogui <br>
2.) pip install pynput <br>

How to use record functionality: <br>
1.) start record.py <br>
2.) press "Tab" key when ready for the program to start recording your actions <br>
3.) Press "Tab" key when done recording actions. <br>
- Note: Can change the key that stops the recording process from "Tab" to any key. Just change the line: "if key == keyboard.Key.tab:" <br>

How to use playback functionality <br>
1.) start playback.py <br>
2.) Press "Tab" key when ready to replicate actions in command file <br>
3.) Press "Tab" key to end program early or just <br>
- Note: Can change the key that stops the playback process from "Tab" to any key. Just change the 2nd line of "if key == keyboard.Key.tab:" <br>
