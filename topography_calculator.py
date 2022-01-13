from tkinter import *
from PIL import ImageTk, Image

# root
root = Tk()
root.geometry('1000x700')

# Image Import
img = ImageTk.PhotoImage(Image.open('images\pexels-trace-hudson-2400594.jpg'))

# scheme window
left_side = Frame(root)
right_side = Frame(root)
left_side.place(relx=0, relwidth=0.40, relheight=1)
#right_side.place(relx=0, relwidth=0, relheight=1)

# Left panel
widget_left = Label(left_side, image=img)
widget_left.pack(side='left', fill='both', expand='yes')


#def widgetSelector(link):
#   if (link == '/home'):

#   return widget_left

#text_panel = ttk.Label(left_side, position='center').grid()
# text_panel.grid


# module
root.mainloop()
