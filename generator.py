# Imports:
import tkinter as tk
from tkinter import *
import qrcode
from tkinter import ttk, filedialog
import clipboard

# The main class:
class QRCodeGenerator:
    def __init__(self, master):

        # Setup:
        self.master = master
        self.master.title("QR Code Generator")
        self.master.geometry("450x230+700+200")
        self.master.iconbitmap("images\qrcode.ico")
        self.master.resizable(False, False)

        # Layout:
        self.f = tk.Frame(self.master, width=450, height=230, bg="#4D677A")
        self.f.place(x=0, y=0)

        self.iconback = PhotoImage(
            file="images\iconBack.png")   # Creates a PhotoImage object named "iconback" by loading the image file "images\iconBack.png"
        self.back_icon = self.iconback.subsample(5, 5)  # reduce "iconback" object (image) size
        self.back_button = tk.Button(self.master, image=self.back_icon, activebackground="#4D677A", activeforeground="White",
                                    compound=CENTER, fg="White", bg="#4D677A", relief="flat", command=self.go_back)
        self.back_button.place(x=2, y=2)

        self.link_label = tk.Label(self.master, text="link or \n content", font=(
            "Arial", 15), fg="White", bg="#4D677A")
        self.link_label.place(x=2, y=56)

        self.link_entry = tk.Entry(self.master, width=35, font=(
            "Arial", 12), fg="White", bg="#5D7283", relief="flat", insertbackground="white")
        self.link_entry.place(x=85, y=70)

        self.iconpaste = PhotoImage(
            file="images\iconPaste.png")
        self.paste_icon = self.iconpaste.subsample(15, 15)
        self.paste_button = tk.Button(self.master, image=self.paste_icon, activebackground="#4D677A", activeforeground="White",
                                    compound=CENTER, fg="White", bg="#4D677A", relief="flat", command=self.paste)
        self.paste_button.place(x=407, y=58)

        self.color_label = tk.Label(self.master, text="Color", font=(
            "Arial", 15), fg="White", bg="#4D677A")
        self.color_label.place(x=7, y=110)

        #Combobox (color selection)
        self.style = ttk.Style()  # Create an instance of ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TCombobox', background='#4D677A', foreground='White', font=(
            'Arial', 15), fieldbackground='#5D7283')

        self.colors = ["black", "red", "blue", "green", "purple"]
        self.color_combo = ttk.Combobox(
            self.master, values=self.colors, height=10)
        self.color_combo.current(0)  # Set the initial selected item in the combobox to the first color in the list (balck)
        self.color_combo.place(x=85, y=115)

        self.generate_button = tk.Button(self.master, text="Generate", font=(
            "Arial", 15, "bold"), fg="White", bg="#5D7283", relief="flat", command=self.generate_qr_code)
        self.generate_button.place(x=172, y=163)

        # Saving options
        self.options = {
            'initialdir': '~/Pictures',
            'initialfile': 'untitled.png',
            'defaultextension': '.png',
            'filetypes': [('PNG files', '*.png'), ('JPEG files', '*.jpg')],
            'title': 'Save As'
        }

    def go_back(self):
        self.master.destroy()  # Close the generator window
        root = tk.Tk()  # Create a new Tk() instance for the main window
        from main_window import MainWindow  # Importing here to avoid "most likely due to a circular import" error
        MainWindow(root)
        root.mainloop()

    def paste(self):
        self.link_entry.insert(0, clipboard.paste())  # Get paste into link_entry

    def generate_qr_code(self):
        self.master.withdraw()  # Hide the main window
        link = self.link_entry.get()

        # QR Code Generating
        if link:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(link)
            qr.make(fit=True)

            # Qr Code Coloring
            color = self.color_combo.get()
            img = qr.make_image(fill_color=color, back_color="white")
            save_file_path = filedialog.asksaveasfilename(**self.options)

            # QR Code Saving
            if save_file_path:
                img.save(save_file_path)
                self.link_entry.delete(0, tk.END)
                self.color_combo.current(0)
                tk.messagebox.showinfo(
                    "Success", "QR Code generated and saved successfully!")
        else:
            tk.messagebox.showwarning(
                "Error", "Please enter both link or content!")

        self.master.deiconify()  # Show the main window again
