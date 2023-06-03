# Imports:
import tkinter as tk
from generator import QRCodeGenerator  # "generator" is a python file, and the "QRCodeGenerator" is the main class
from reader import QRCodeReader  # "reader" is a python file, and the "QRCodeReader" is the main class

# The main class:
class MainWindow:
    def __init__(self, master):  # the constructor method of the "MainWindow" class
        
        # Setup:
        self.master = master
        self.master.title("QR Code Tool")
        self.master.geometry("360x150+700+200")
        self.master.iconbitmap("qrcode.ico")
        self.master.resizable(False, False)

        # Layout:
        self.f1 = tk.Frame(self.master, width=360, height=150, bg="#4D677A")  # 
        self.f1.place(x=0, y=0)

        self.generator_button = tk.Button(self.f1, text="QR Code Reader", font=(
            "Arial", 13, "bold"), fg="White", bg="#5D7283", relief="flat", command=self.open_reader)
        self.generator_button.place(x=10, y=50)

        self.reader_button = tk.Button(self.f1, text="QR Code Generator", font=(
            "Arial", 13, "bold"), fg="White", bg="#5D7283", relief="flat", command=self.open_generator)
        self.reader_button.place(x=180, y=50)
    
    def open_generator(self):  # Function to Open QR Code Generator Window
        self.master.destroy()  # Close the main window
        generator_window = tk.Tk()  # Create a new Tk() instance for the generator window
        QRCodeGenerator(generator_window)  # Create an instance of the "QRCodeGenerator" class, passing the "generator_window" as an argument.
        generator_window.mainloop()  # Start the event loop for the generator window

    def open_reader(self):  # Open QR Code Reader Window
        self.master.destroy()
        reader_window = tk.Tk()
        QRCodeReader(reader_window)
        reader_window.mainloop()
