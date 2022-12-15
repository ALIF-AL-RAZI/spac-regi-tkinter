# import tkinter as tkinter
# from tkinter import *
#
# root = tkinter.Tk()
#
# # specify resolutions of both windows
# w0, h0 = 3840, 2160
# w1, h1 = 1920, 1080
#
# # set up a window for first display, if wanted
# win0 = tkinter.Toplevel()
# win0.geometry(f"{w0}x{h0}+0+0")
#
# # set up window for second display with fullscreen
# win1 = tkinter.Toplevel()
# win1.geometry(f"{w1}x{h1}+{w0}+0") # <- this is the key, offset to the right by w0
# win1.attributes("-fullscreen", True)
#
# root.mainloop()



from screeninfo import get_monitors

monitor= get_monitors()

global prm_x
global prm_y
global prm_width
global prm_height


global sec_x
global sec_y
global sec_width
global sec_height

for m in monitor:
    if m.is_primary == True:
        prm_x = m.x
        prm_y = m.y
        prm_width = m.width
        prm_height = m.height

print(prm_x)
print(prm_y)
print(prm_height)
print(prm_width)

for m in monitor:
    if m.is_primary == False:
        sec_x = m.x
        sec_y = m.y
        sec_width = m.width
        sec_height = m.height

print(sec_x)
print(sec_y)
print(sec_height)
print(sec_width)


