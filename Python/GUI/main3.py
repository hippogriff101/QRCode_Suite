from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import qrcode
import os

number = 0
path = os.getcwd()

def main():
    global number
    number += 1
    if coify.get().strip() == "":
        result_message.set("Please enter some text to generate a QR code.")
        return
    img = qrcode.make(coify.get())
    filename = f"{path}/qrcode_suite{number}.png" 
    img.save(filename)
    result_message.set(f"QR code generated and saved successfully as '{filename}'.")

def history():
    list_of_files = os.listdir(path)
    qr_files = [f for f in list_of_files if f.startswith("qrcode_suite") and f.endswith(".png")]
    if qr_files:
        history_message = "Generated QR Code Files:\n" + "\n".join(qr_files)
    else:
        history_message = "No QR code files found."
    result_message.set(history_message)
def preview():
    root = Toplevel()
    if number == 0:
        result_message.set("No QR code to preview.")
        root.destroy()
    else:
        filename = f"qrcode_suite{number}.png"
        ttk.Label(root, text=filename).grid(column=2, row=2, sticky=(W, E), padx=5, pady=5)
        ttk.Button(root, text="Close", command=root.destroy).grid(column=2, row=4, sticky=(W, E), padx=5, pady=5)
        img = ImageTk.PhotoImage(Image.open(filename))
        panel = ttk.Label(root, image=img)
        panel.image = img
        panel.grid(column=2, row=3, sticky=(W, E), padx=5, pady=5)
        root.mainloop()
root = Tk()
root.title("Basic QR Code Generator")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(2, weight=1)

coify = StringVar()
coify_entry = ttk.Entry(mainframe, width=30, textvariable=coify)
coify_entry.grid(column=2, row=1, sticky=(W, E), padx=5, pady=5)

result_message = StringVar()
result_message.set("Enter text and click QRify to generate a QR code.")
ttk.Label(mainframe, textvariable=result_message).grid(column=2, row=2, sticky=(W, E), padx=5, pady=5)
ttk.Button(mainframe, text="QRify", command=main).grid(column=3, row=3, sticky=W, padx=5, pady=5)
ttk.Button(mainframe, text="History", command=history).grid(column=6, row=3, sticky=W, padx=5, pady=5)
ttk.Button(mainframe, text="Preview", command=preview).grid(column=9, row=3, sticky=W, padx=5, pady=5)
ttk.Button(mainframe, text="Close", command=root.destroy).grid(column=12, row=3, sticky=W, padx=5, pady=5)

coify_entry.focus()
root.mainloop()