import tkinter as tk
import subprocess

def start_script_1():
    subprocess.Popen(["python", "normale.py"])

def start_script_2():
    subprocess.Popen(["python", "script2.py"])

root = tk.Tk()
root.title("Python Script Launcher")

button1 = tk.Button(root, text="Start Script 1", command=start_script_1)
button1.pack(pady=10)

button2 = tk.Button(root, text="Start Script 2", command=start_script_2)
button2.pack(pady=10)

root.mainloop()