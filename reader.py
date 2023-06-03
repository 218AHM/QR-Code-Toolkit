# Imports:
import tkinter as tk
from tkinter import *
import os
from tkinter import filedialog
from PIL import Image
import clipboard
import webbrowser
import pyzbar.pyzbar as pyzbar

# The main class:
class QRCodeReader:
    def __init__(self, master):

        # Setup:
        self.master = master
        self.master.title("QR Code Reader")
        self.master.geometry("450x230+700+200")
        self.master.iconbitmap("qrcode.ico")
        self.master.resizable(False, False)

        # Layout:
        self.f3 = tk.Frame(self.master, width=450, height=230, bg="#4D677A")
        self.f3.place(x=0, y=0)

        self.iconback = PhotoImage(
            file="iconBack.png")   # Creates a PhotoImage object named "iconback" by loading the image file "iconBack.png"
        self.back_icon = self.iconback.subsample(5, 5)  # reduce "iconback" object (image) size
        self.back_button = tk.Button(self.master, image=self.back_icon, activebackground="#4D677A", activeforeground="White",
                                    compound=CENTER, fg="White", bg="#4D677A", relief="flat", command=self.go_back)
        self.back_button.place(x=2, y=2)

        self.iconbrowse = PhotoImage(file = "iconBrowse.png")
        self.browse_icon = self.iconbrowse.subsample(3, 3)  # reduce "iconbrowse" object (image) size
        self.browse_button = Button(self.f3, text = ' Browse', image = self.browse_icon, compound = LEFT, bg="#4D677A", relief="flat", fg="White", activebackground="#4D677A", activeforeground="White", command=self.browse_file)
        self.browse_button.place(x=190, y=20)

        self.qr_data_label = tk.Label(self.master, text="QR Data:", font=(
            "Arial", 15), fg="White", bg="#4D677A")
        self.qr_data_label.place(x=2, y=90)

        self.qr_data_entry = tk.Entry(self.master, width=35, font=(
            "Arial", 12), fg="Black", bg="#5D7283", relief="flat")
        self.qr_data_entry.place(x=95, y=95)

        self.iconcopy = PhotoImage(
            file="iconCopy.png")
        self.copy_icon = self.iconcopy.subsample(12, 12)
        self.copy_button = tk.Button(self.master, image=self.copy_icon, activebackground="#4D677A", activeforeground="White",
                                    compound=CENTER, fg="White", bg="#4D677A", relief="flat", command=self.copy)
        self.copy_button.place(x=405, y=77)

        self.open_url_button = tk.Button(
            self.master, font=("Arial", 13), fg="White", bg="#4D677A", relief="flat", command=self.open_url, state='disabled')  # Just appear if the content is link
        self.open_url_button.place(x=190, y=145)

    def go_back(self):
        self.master.destroy()  # Close the generator window
        root = tk.Tk()  # Create a new Tk() instance for the main window
        from main_window import MainWindow  # Importing here to avoid "most likely due to a circular import" error
        MainWindow(root)
        root.mainloop()

    def copy(self):
        clipboard.copy(self.qr_data_entry.get())  # Copy text from the entry

    def browse_file(self):
        self.master.withdraw()  # Hide  the main window

        # Prompt (ask) the user to select an image file
        self.file_path = filedialog.askopenfilename(initialdir=os.getcwd(), filetypes=[
                                                ("PNG", "*.png"), ("JPEG", "*.jpg")])
        try:
            #  Open the selected image file
            with Image.open(self.file_path) as img:
                img = img.convert('RGB')    # Convert the image to RGB format for compatibility with pyzbar
                decoded_objects = pyzbar.decode(img)    # Decode (get content) the QR codes in the image
                if decoded_objects:
                    # Process the decoded QR codes
                    link = decoded_objects[0].data.decode('utf-8')  # Get the data of the first decoded QR code
                    for obj in decoded_objects:
                        data = obj.data.decode('utf-8')  # Get the data of each decoded QR code
                        self.qr_data_entry.config(state="normal")  # Enable editing of the entry widget
                        self.qr_data_entry.delete(0, tk.END)
                        self.qr_data_entry.insert(0, data)
                        self.qr_data_entry.config(state="readonly")  # Disable editing of the entry widget
                    self.open_url_button.config(state='normal')  # Enable the open URL button
                else:
                    # No QR code found in the selected image
                    tk.messagebox.showwarning(
                        "Error", "No QR Code found in the selected image!")
                    self.open_url_button.config(state='disabled')  # Disable the open URL button

        except Exception as e:
            print(e)  # Print the exception error message to the console
            tk.messagebox.showwarning(
                "Error", "An error occurred while processing the image. Please select a valid image file!")

        self.master.deiconify()  # Show the main window again

    def open_url(self):
        link = self.qr_data_entry.get()
        webbrowser.open(link)  # Open the link in the default browser
