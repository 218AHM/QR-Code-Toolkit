#Imports:
import tkinter as tk
from main_window import MainWindow

# Run:
if __name__ == '__main__':  # check if the current script is being run as the main module
    root = tk.Tk() 
    MainWindow(root)  # Create a tkinter object (Main window) 
    root.mainloop()  # Start the event loop for the main file (Main window)
