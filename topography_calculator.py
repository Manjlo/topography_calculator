from math import sin
import numpy as np
from cProfile import label
from turtle import right
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# window
root = Tk()
root.geometry('1000x700')
root.title('Calculadora Topografica')

# Image import
img = ImageTk.PhotoImage(Image.open('images\pexels-trace-hudson-2400594.jpg'))

# scheme window
left_side = Frame(root)
right_side = Frame(root)
left_side.place(relx=0, relwidth=0.40, relheight=1)
right_side.place(relx=0.40, relwidth=0.60, relheight=1, bordermode="outside")


# functions links

def fun1():
    for widget in left_side.winfo_children():
        widget.destroy()
    for widget in right_side.winfo_children():
        widget.destroy()
    widgetSelector("/fun1")

# function bottons


def backButton():
    for widget in left_side.winfo_children():
        widget.destroy()
    for widget in right_side.winfo_children():
        widget.destroy()
    widgetSelector('/home')


# calc functions


def calc_Coordinate(y, x, distance, angulo):

    y2 = y + (distance*np.sin(angulo))
    x2 = x + (distance*np.cos(angulo))
    return x2, y2

# widget link  function selector


def widgetSelector(link):
    if (link == '/home'):
        # left panel
        widget_left = LabelFrame(left_side)
        widget_left.pack(fill='both', expand='yes')
        widget_image = Label(widget_left, image=img)
        widget_image.place(x=0, y=0, relheight=1, relwidth=1)
        widget_text = Label(widget_left, text='Bienvenido',
                            font=("Helvetica", 50))
        widget_text.pack(pady=50)
        widget_text.place(y=270, x=35)
        widget_text2 = Label(
            widget_left, text='Por favor presione la opción', font=("Helvetica", 20))
        widget_text2.place(y=370, x=32)
        widget_text3 = Label(
            widget_left, text='requerida', font=("Helvetica", 20))
        widget_text3.place(y=405, x=120)
        # right panel
        widget_right = LabelFrame(right_side)
        widget_right.pack(fill="both", expand="yes")
        widget_button1 = Button(
            widget_right, text="CALCULO DE COORDENADAS", font=("Helvetica", 20), foreground="gray", command=fun1)
        widget_button1.grid(row=0, column=0, pady=20)
        widget_button2 = Button(
            widget_right, text="DISTANCIA EUCLIDIANA", font=("Helvetica", 20), foreground="gray")
        widget_button2.grid(row=1, column=0, pady=20)
        widget_button3 = Button(
            widget_right, text="CALCULAR AZIMUT", font=("Helvetica", 20), foreground="gray")
        widget_button3.grid(row=2, column=0, pady=20)
        widget_button4 = Button(
            widget_right, text="ERROR MEDIO Y DESVIACIÓN", font=("Helvetica", 20), foreground="gray")
        widget_button4.grid(row=3, column=0, pady=20)
        widget_button5 = Button(
            widget_right, text="CALCULAR AREA", font=("Helvetica", 20), foreground="gray")
        widget_button5.grid(row=4, column=0, pady=20)
    if (link == "/fun1"):
        # widget left

        widget_left = LabelFrame(left_side)
        widget_left.pack(fill='both', expand='yes')
        label_text = Label(widget_left, text="Coordenada inicial Norte (m)")
        label_text.place(y=100, x=100)
        coordinate_nort = Entry(widget_left)
        coordinate_nort.place(y=120, x=100)
        label_text2 = Label(widget_left, text="Coordenada inicial Este (m)")
        label_text2.place(y=150, x=100)
        coordinate_east = Entry(widget_left)
        coordinate_east.place(y=170, x=100)
        label_text3 = Label(widget_left, text="Angulo Azimut (grados)")
        label_text3.place(y=200, x=100)
        azimut = Entry(widget_left)
        azimut.place(y=220, x=100)
        label_text4 = Label(widget_left, text="Distancia (m)")
        label_text4.place(y=250, x=100)
        distance = Entry(widget_left)
        distance.place(y=270, x=100)
        back = Button(widget_left, text="Back", command=backButton)
        back.place(y=320, x=100)

        def getData():
            nort = float(coordinate_nort.get())
            east = float(coordinate_east.get())
            d = float(distance.get())
            a = float(azimut.get())
            text = nort+east+d+a
            radians = np.radians(a)
            coordinate = calc_Coordinate(nort, east, d, radians)
            ax.clear()
            ax.plot(coordinate), ax.grid(True)
            ax.set_xlabel('$p1$'),ax.set_ylabel('p2')
            ax.set_title('$p2 = $')
            line.draw()
            datos = Label(widget_left, text=coordinate)
            datos.place(y=400, x=100)
            return datos
    # back.grid( row=9 , column=0)
        next = Button(widget_left, text="Next", command=getData)
        next.place(y=320, x=180)
    # next.grid(column=1)

    # widget right
        widget_right = LabelFrame(right_side)
        widget_right.pack(fill="both", expand="yes")
        figure = plt.Figure(figsize=(8, 6), dpi=100)
        ax = figure.add_subplot(111)
        ax.grid(True), ax.set_xlabel('$x$'), ax.set_ylabel('$y(x)$')
        line = FigureCanvasTkAgg(figure, widget_right)
        line.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=1)

        return widget_left, widget_right


# text_panel = ttk.Label(left_side, position='center').grid()
# text_panel.grid

widgetSelector('/home')
# module
root.mainloop()
