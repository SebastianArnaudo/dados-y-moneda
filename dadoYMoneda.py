import tkinter as tk
from tkinter import Frame
from calculo import moneda,d3Lados,d4Lados,d6Lados,d8Lados,d10aLados,d10bLados,d12Lados,d20Lados,d30Lados,d100Lados

def main():

    vInicio = tk.Tk()
    vInicio.title("Dados y Monedas")
    vInicio.geometry("300x400")

    def mon():

        def tirada():

            result = moneda()
            lTirada["text"] = result


        vMoneda=tk.Toplevel()
        vMoneda.title("Moneda")
        vMoneda.geometry("300x250")

        frameMoneda = Frame(vMoneda, bg= "brown")
        frameMoneda.pack(expand=True, fill="both")

        lTirada = tk.Label(frameMoneda,text="", fg= "white", bg= "brown")
        lTirada.place(x=100,y=100)

        bTirar = tk.Button(frameMoneda,text="Tirar",bg="Red1",fg="white", command= tirada)
        bTirar.place(x=90, y= 200)

    def d3():

        def tirada():

            result = d3Lados()
            lTirada["text"] = result


        vMoneda=tk.Toplevel()
        vMoneda.title("Dado de 3")
        vMoneda.geometry("300x250")

        frameMoneda = Frame(vMoneda, bg= "brown")
        frameMoneda.pack(expand=True, fill="both")

        lTirada = tk.Label(frameMoneda,text="", fg= "white", bg= "brown")
        lTirada.place(x=100,y=100)

        bTirar = tk.Button(frameMoneda,text="Tirar",bg="Red1",fg="white", command= tirada)
        bTirar.place(x=90, y= 200)

    def d4():

        def tirada():

            result = d4Lados()
            lTirada["text"] = result


        vMoneda=tk.Toplevel()
        vMoneda.title("Dado de 4")
        vMoneda.geometry("300x250")

        frameMoneda = Frame(vMoneda, bg= "brown")
        frameMoneda.pack(expand=True, fill="both")

        lTirada = tk.Label(frameMoneda,text="", fg= "white", bg= "brown")
        lTirada.place(x=100,y=100)

        bTirar = tk.Button(frameMoneda,text="Tirar",bg="Red1",fg="white", command= tirada)
        bTirar.place(x=90, y= 200)

    def d6():

        def tirada():

            result = d6Lados()
            lTirada["text"] = result


        vMoneda=tk.Toplevel()
        vMoneda.title("Dado de 6")
        vMoneda.geometry("300x250")

        frameMoneda = Frame(vMoneda, bg= "brown")
        frameMoneda.pack(expand=True, fill="both")

        lTirada = tk.Label(frameMoneda,text="", fg= "white", bg= "brown")
        lTirada.place(x=100,y=100)

        bTirar = tk.Button(frameMoneda,text="Tirar",bg="Red1",fg="white", command= tirada)
        bTirar.place(x=90, y= 200)

    def d8():

        def tirada():

            result = d8Lados()
            lTirada["text"] = result


        vMoneda=tk.Toplevel()
        vMoneda.title("Dado de 8")
        vMoneda.geometry("300x250")

        frameMoneda = Frame(vMoneda, bg= "brown")
        frameMoneda.pack(expand=True, fill="both")

        lTirada = tk.Label(frameMoneda,text="", fg= "white", bg= "brown")
        lTirada.place(x=100,y=100)

        bTirar = tk.Button(frameMoneda,text="Tirar",bg="Red1",fg="white", command= tirada)
        bTirar.place(x=90, y= 200)

    def d10a():

        def tirada():

            result = d10aLados()
            lTirada["text"] = result


        vMoneda=tk.Toplevel()
        vMoneda.title("Dado de 10")
        vMoneda.geometry("300x250")

        frameMoneda = Frame(vMoneda, bg= "brown")
        frameMoneda.pack(expand=True, fill="both")

        lTirada = tk.Label(frameMoneda,text="", fg= "white", bg= "brown")
        lTirada.place(x=100,y=100)

        bTirar = tk.Button(frameMoneda,text="Tirar",bg="Red1",fg="white", command= tirada)
        bTirar.place(x=90, y= 200)

    def d10b():

        def tirada():

            result = d10bLados()
            lTirada["text"] = result


        vMoneda=tk.Toplevel()
        vMoneda.title("Dado de 10")
        vMoneda.geometry("300x250")

        frameMoneda = Frame(vMoneda, bg= "brown")
        frameMoneda.pack(expand=True, fill="both")

        lTirada = tk.Label(frameMoneda,text="", fg= "white", bg= "brown")
        lTirada.place(x=100,y=100)

        bTirar = tk.Button(frameMoneda,text="Tirar",bg="Red1",fg="white", command= tirada)
        bTirar.place(x=90, y= 200)

    def d12():

        def tirada():

            result = d12Lados()
            lTirada["text"] = result


        vMoneda=tk.Toplevel()
        vMoneda.title("Dado de 12")
        vMoneda.geometry("300x250")

        frameMoneda = Frame(vMoneda, bg= "brown")
        frameMoneda.pack(expand=True, fill="both")

        lTirada = tk.Label(frameMoneda,text="", fg= "white", bg= "brown")
        lTirada.place(x=100,y=100)

        bTirar = tk.Button(frameMoneda,text="Tirar",bg="Red1",fg="white", command= tirada)
        bTirar.place(x=90, y= 200)

    def d20():

        def tirada():

            result = d20Lados()
            lTirada["text"] = result


        vMoneda=tk.Toplevel()
        vMoneda.title("Dado de 20")
        vMoneda.geometry("300x250")

        frameMoneda = Frame(vMoneda, bg= "brown")
        frameMoneda.pack(expand=True, fill="both")

        lTirada = tk.Label(frameMoneda,text="", fg= "white", bg= "brown")
        lTirada.place(x=100,y=100)

        bTirar = tk.Button(frameMoneda,text="Tirar",bg="Red1",fg="white", command= tirada)
        bTirar.place(x=90, y= 200)

    def d30():

        def tirada():

            result = d30Lados()
            lTirada["text"] = result


        vMoneda=tk.Toplevel()
        vMoneda.title("Dado de 30")
        vMoneda.geometry("300x250")

        frameMoneda = Frame(vMoneda, bg= "brown")
        frameMoneda.pack(expand=True, fill="both")

        lTirada = tk.Label(frameMoneda,text="", fg= "white", bg= "brown")
        lTirada.place(x=100,y=100)

        bTirar = tk.Button(frameMoneda,text="Tirar",bg="Red1",fg="white", command= tirada)
        bTirar.place(x=90, y= 200)

    def d100():

        def tirada():

            result = d100Lados()
            lTirada["text"] = result


        vMoneda=tk.Toplevel()
        vMoneda.title("Dado de 100")
        vMoneda.geometry("300x250")

        frameMoneda = Frame(vMoneda, bg= "brown")
        frameMoneda.pack(expand=True, fill="both")

        lTirada = tk.Label(frameMoneda,text="", fg= "white", bg= "brown")
        lTirada.place(x=100,y=100)

        bTirar = tk.Button(frameMoneda,text="Tirar",bg="Red1",fg="white", command= tirada)
        bTirar.place(x=90, y= 200)

    

    frameInicio = Frame(vInicio,bg="Purple")
    frameInicio.pack(expand= True, fill="both")

    lBienvenida = tk.Label(frameInicio,text="Bienvenido\n Elija la modalidad", fg="white",bg="Purple")
    lBienvenida.place(x=95,y=10)

    bMoneda = tk.Button(frameInicio,text="Moneda",bg="Green1",command= mon)
    bMoneda.place(x=115,y=50)

    bd3 = tk.Button(frameInicio,text= "Dadi 3 lados", bg= "Green1", command= d3)
    bd3.place(x=105,y=80)

    bD4 = tk.Button(frameInicio,text="Dado 4 lados",bg="Green1", command= d4)
    bD4.place(x=105,y=110)

    bD6 = tk.Button(frameInicio,text="Dado 6 lados",bg="Green1", command= d6)
    bD6.place(x=105,y=140)

    bD8 = tk.Button(frameInicio,text="Dado 8 lados",bg="Green1", command= d8)
    bD8.place(x=105,y=170)

    bD10a = tk.Button(frameInicio,text="Dado 10 lados (0 a 9)",bg="Green1", command= d10a)
    bD10a.place(x=83,y=200)
    
    bD10b = tk.Button(frameInicio,text="Dado 10 lados (1 a 10)",bg="Green1", command= d10b)
    bD10b.place(x=80,y=230)

    bD12 = tk.Button(frameInicio,text="Dado 12 lados",bg="Green1", command= d12)
    bD12.place(x=102,y=260)

    bD20 = tk.Button(frameInicio,text="Dado 20 lados",bg="Green1", command= d20)
    bD20.place(x=102,y=290)

    bD30 = tk.Button(frameInicio,text="Dado 30 lados",bg="Green1", command= d30)
    bD30.place(x=102,y=320)

    bD100 = tk.Button(frameInicio,text="Dado 100 lados",bg="Green1", command= d100)
    bD100.place(x=99,y=350)


    tk.mainloop()
if __name__ == "__main__":
    main()