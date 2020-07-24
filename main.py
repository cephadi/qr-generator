from tkinter import *
from tkinter import messagebox
import pyqrcode
import os

gui = Tk()
gui.title("QR - Generator")

def generateQr():
    if len(subject.get()) != 0:
        global myQr
        myQr = pyqrcode.create(subject.get())
        imageQr = myQr.xbm(scale=6)
        global photoQr
        photoQr = BitmapImage(data=imageQr)
    else:
        messagebox.showinfo("Error!", "Please enter valid subject!")

    try:
        showCodeQr()
    except:
        pass

def showCodeQr():
    global photoQr
    labelNotif.config(image=photoQr)
    subLabel.config(text="Show QR for : " + subject.get())

def saveQr():
    directory = path1 = os.getcwd() + "\\QR Codes"
    if not os.path.exists(directory):
        os.makedirs(directory)
    try:
        if len(filename.get()) != 0:
            global myQr
            myQr.png(os.path.join(directory, filename.get() + ".png"), scale=6)
        else:
            messagebox.showinfo("Error!", "Please enter valid filename!")
    except Exception as e:
        print(e)
        messagebox.showinfo("Error!", "Please generate QR code first!")

label1 = Label(gui, text="Enter subject : ", font=("Helvetica", 12))
label1.grid(row=0, column=0, sticky=N + S + E + W)

label2 = Label(gui, text="Enter Filename : ", font=("Helvetica", 12))
label2.grid(row=1, column=0, sticky=N + S + E + W)

subject = StringVar()
entrySubject = Entry(gui, textvariable=subject, font=("Helvetica", 12))
entrySubject.grid(row=0, column=1, sticky=N + S + E + W)

filename = StringVar()
entryFilename = Entry(gui, textvariable=filename, font=("Helvetica", 12))
entryFilename.grid(row=1, column=1, sticky=N + S + E + W)

buttonCreate = Button(gui, text="Create QR", font=("Helvetica", 12), width=15, command=generateQr)
buttonCreate.grid(row=0, column=3, sticky=N + S + E + W)

labelNotif = Label(gui)
labelNotif.grid(row=2, column=1, sticky=N + S + E + W)

subLabel = Label(gui, text="")
subLabel.grid(row=3, column=1, sticky=N + S + E + W)

buttonShow = Button(gui, text="Save as PNG", font=("Helvetica", 12), width=15, command=saveQr)
buttonShow.grid(row=1, column=3, sticky=N + S + E + W)

# make responsive layout
totalRow = 3
totalCol = 3
for row in range(totalRow + 1):
    gui.grid_rowconfigure(row, weight=1)

for col in range(totalCol + 1):
    gui.grid_columnconfigure(col, weight=1)

gui.mainloop()