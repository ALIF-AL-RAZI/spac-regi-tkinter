from tkinter import *
from screeninfo import get_monitors
monitor = get_monitors()

global prm_x
global prm_y
global prm_width
global prm_height

for m in monitor:
    if m.is_primary:
        prm_x = m.x
        prm_y = m.y
        prm_width = m.width
        prm_height = m.height

global sec_x
global sec_y
global sec_width
global sec_height

for m in monitor:
    if not m.is_primary:
        sec_x = m.x
        sec_y = m.y
        sec_width = m.width
        sec_height = m.height


window = Tk()
window.geometry("%dx%d" % (prm_width, prm_height))
window.title("SPAC 22")
label = Label(window, text="Hello Tkinter! page1")
label.pack()

scan_scrn = Toplevel(window)
scan_scrn.geometry("%dx%d+%d+%d" % (sec_width, sec_height, sec_x, sec_y))
scan_scrn.title("SPAC 22")
label = Label(scan_scrn, text="Hello Tkinter! page2")
label.pack()
scan_scrn.mainloop()

window.mainloop()
