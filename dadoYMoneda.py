import tkinter as tk
from tkinter import Frame
import random

def main():

    vInicio = tk.Tk()
    vInicio.title("Dados y Monedas")
    vInicio.geometry("300x350")

    frameInicio = Frame(vInicio,bg="Purple")
    frameInicio.pack(expand= True, fill="both")

    lBienvenida = tk.Label(frameInicio,text="Bienvenido\n Elija la modalidad", fg="white",bg="Purple")
    lBienvenida.place(x=95,y=10)

    bMoneda = tk.Button(frameInicio,text="Moneda",bg="Green1")
    bMoneda.place(x=115,y=50)

    bD4 = tk.Button(frameInicio,text="Dado 4 lados",bg="Green1")
    bD4.place(x=105,y=80)

    bD6 = tk.Button(frameInicio,text="Dado 6 lados",bg="Green1")
    bD6.place(x=105,y=110)

    bD8 = tk.Button(frameInicio,text="Dado 8 lados",bg="Green1")
    bD8.place(x=105,y=140)

    bD10 = tk.Button(frameInicio,text="Dado 10 lados",bg="Green1")
    bD10.place(x=102,y=170)

    bD12 = tk.Button(frameInicio,text="Dado 12 lados",bg="Green1")
    bD12.place(x=102,y=200)

    bD20 = tk.Button(frameInicio,text="Dado 20 lados",bg="Green1")
    bD20.place(x=102,y=230)


    tk.mainloop()
if __name__ == "__main__":
    main()