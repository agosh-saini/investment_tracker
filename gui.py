import tkinter as tk

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Investment Tracker")
        
        # Add your GUI elements here
        
        self.window.mainloop()

if __name__ == "__main__":
    gui = GUI()