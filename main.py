from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

from tkinter import messagebox

import cv2

import pyqrcode
import png
from pyqrcode import QRCode

import webbrowser

from screeninfo import get_monitors

# def scan():
#     cap = cv2.VideoCapture(0)
#     detector = cv2.QRCodeDetector()
#
#     while True:
#         ret, img = cap.read()
#         data, one, _ = detector.detectAndDecode(img)
#         if data:
#             a = data
#             break
#
#         cv2.imshow('qrcodescanner app', img)
#         if cv2.waitKey(1) == ord('q'):
#             break
#
#     # b = webbrowser.open(str(a))
#     cap.release()
#     cv2.destroyAllWindows()
#     print(a)


monitor = get_monitors()

global prm_x
global prm_y
global prm_width
global prm_height

global sec_x
global sec_y
global sec_width
global sec_height

for m in monitor:
    if m.is_primary:
        prm_x = m.x
        prm_y = m.y
        prm_width = m.width
        prm_height = m.height

print(prm_x)
print(prm_y)
print(prm_height)
print(prm_width)

for m in monitor:
    if not m.is_primary:
        sec_x = m.x
        sec_y = m.y
        sec_width = m.width
        sec_height = m.height

print(sec_x)
print(sec_y)
print(sec_height)
print(sec_width)

# creating window
# window = Tk()


# getting screen width and height of display
# width= window.winfo_screenwidth()
# height= window.winfo_screenheight()
#
# print(width)
# print(height)


# setting tkinter window size
# window.geometry("%dx%d" % (width, height))
# window.title("SPAC 22")
# label = Label(window, text="Hello Tkinter!")
# label.pack()
#
# window.mainloop()

#
# cap = cv2.VideoCapture(0)
#
#
# def scan():
#     detector = cv2.QRCodeDetector()
#
#     while True:
#         ret, img = cap.read()
#         data, one, _ = detector.detectAndDecode(img)
#         if data:
#             a = data
#             break
#
#         cv2.imshow('qrcodescanner app', img)
#         if cv2.waitKey(1) == ord('q'):
#             break
#
#     # b = webbrowser.open(str(a))
#     #cap.release()
#     #cv2.destroyAllWindows()
#     page4(a)


window = Tk()
window.geometry("%dx%d" % (prm_width, prm_height))
window.title("SPAC 22")

label = Label(window, text="Hello Tkinter! page1")
label.pack()
# ttk.Button(window, text="Scan Qr code of bus", command='').place(x=325, y=350)

scan_scrn = Toplevel(window)
scan_scrn.geometry("%dx%d+%d+%d" % (sec_width, sec_height, sec_x, sec_y))
scan_scrn.title("SPAC 22")
label = Label(scan_scrn, text="Scan Qr Code", width=30, height=10)
label.grid(row=0, column=0)

label1 = Label(scan_scrn)
label1.grid(row=1, column=0)
cap = cv2.VideoCapture(0)


# global data
# global a


# Define function to show frame

# label3 = Label(scan_scrn, text='asdgffds')
# label3.grid(row=0, column=1)


def page4(a):
    # for widgets in scan_scrn.winfo_children():
    #     widgets.destroy()

    #grid_remove()

    label3 = Label(scan_scrn, text=a, width=30, height=10)
    label3.grid(row=0, column=1)



    strng = 'Departure: Mirpur\nDestination: Jamuna\nTicket Staus: Student\nFare: 10\nPayment Status: Confirmed'
    qr = pyqrcode.create(strng)
    qr.png('Ticketqr.png', scale=10)


def show_frames():
    # Get the latest frame and convert into Image
    cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
    detector = cv2.QRCodeDetector()
    data, one, _ = detector.detectAndDecode(cv2image)
    if data:
        a = data
        page4(data)

    img = Image.fromarray(cv2image)

    # Convert image to PhotoImage
    imgtk = ImageTk.PhotoImage(image=img)

    label1.imgtk = imgtk
    label1.configure(image=imgtk)
    # Repeat after an interval to capture continiously
    label1.after(20, show_frames)




label2 = Label(scan_scrn, text='a')
label2.grid(row=2, column=0)

show_frames()

scan_scrn.mainloop()

window.mainloop()
#print(a)
