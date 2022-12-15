import tkinter as tk
from tkinter import *
import screeninfo

screeninfo.get_monitors()

root = Tk()

root.geometry("200x200")

# def open():
top = Toplevel(root)

top.mainloop()

label = Label(root, text="Hello Tkinter!")
# btn = Button(root, text="open", command=open)

# btn.place(x=75, y=50)

root.mainloop()


def get_monitor_from_coord(x, y):
    monitors = screeninfo.get_monitors()

    for m in reversed(monitors):
        if m.x <= x <= m.width + m.x and m.y <= y <= m.height + m.y:
            return m
    return monitors[0]


# Get the screen which contains top
current_screen = get_monitor_from_coord(root.winfo_x(), root.winfo_y())

# Get the monitor's size
print(current_screen.width, current_screen.height)
