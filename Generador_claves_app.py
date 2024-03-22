from tkinter import *
import secrets
import string


root = Tk()
root.title("Generador de claves")
root.geometry("280x100")

my_frame = Frame(root, width=300, height=300)
my_frame.pack()

pw = StringVar()

cuadro_clave = Entry(my_frame, textvariable=pw)
cuadro_clave.grid(padx=10, pady=10)

def generar_clave():
    mayusculas = string.ascii_letters.upper()
    minusculas = string.ascii_letters.lower()
    numeros = string.digits
    car_especiales = string.punctuation

    alfabeto = mayusculas + minusculas + numeros + car_especiales

    clave_long = 12

    while True:
        clave = ''
        for i in range(clave_long):
            clave += ''.join(secrets.choice(alfabeto))
        if sum(char in numeros for char in clave) >= 2 and sum(char in car_especiales for char in clave) >= 2 and sum(char in minusculas for char in clave) >= 1 and sum(char in mayusculas for char in clave) >= 1:
            break
    pw.set(clave)

boton_generar = Button(root, text="Generar nueva clave", command=generar_clave)
boton_generar.pack(padx=10, pady=10)

menu_barra = Menu(root)
root.config(menu=menu_barra)

def menu_desplegable(event):
    opciones_menu.post(event.x_root, event.y_root)

opciones_menu = Menu(menu_barra, tearoff=0)
menu_barra.add_cascade(label="Opciones", menu=opciones_menu)
opciones_menu.add_command(label="Cortar", command=lambda: cuadro_clave.event_generate("<<Cut>>"))
opciones_menu.add_command(label="Copiar", command=lambda: cuadro_clave.event_generate("<<Copy>>"))
opciones_menu.add_command(label="Pegar", command=lambda: cuadro_clave.event_generate("<<Paste>>"))

cuadro_clave.bind("<Button-3>", menu_desplegable)

root.mainloop()