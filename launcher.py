import tkinter as tk
import subprocess

class Fullscreen_Example:
    def __init__(self):
        self.window = tk.Tk()
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)
        self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (self.w, self.h))
        
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)
        
        self.start_script1_button = tk.Button(self.window, text="Gara Normale", command=self.start_script1)
        self.start_script1_button.pack(pady=20)

        self.start_script2_button = tk.Button(self.window, text="Gara Sprint", command=self.start_script2)
        self.start_script2_button.pack(pady=20)

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

    def start_script1(self):
        subprocess.Popen(["python", "normale.py"])
        self.window.destroy()

    def start_script2(self):
        subprocess.Popen(["python", "script2.py"])
        self.window.destroy()

if __name__ == '__main__':
    app = Fullscreen_Example()
    app.window.mainloop()