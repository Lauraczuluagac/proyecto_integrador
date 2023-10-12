import streamlit as st
import tkinter as tk


def calcular():
    try:
        resultado.set(eval(entrada.get()))
    except:
        resultado.set("Error")


# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Variable para mostrar el resultado
resultado = tk.StringVar()

# Crear una entrada de texto
entrada = tk.Entry(ventana, width=30)
entrada.grid(row=0, column=0, columnspan=4)

# Crear botones para números y operaciones
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in botones:
    tk.Button(ventana, text=button, padx=20, pady=20, command=lambda b=button: entrada.insert(
        'end', b) if b != '=' else calcular()).grid(row=row_val, column=col_val)
    col_val += 1
if col_val > 3:
    col_val = 0
    row_val += 1

# Botón Clear
tk.Button(ventana, text='Clear', padx=20, pady=20, command=lambda: entrada.delete(
    0, 'end')).grid(row=row_val, column=col_val)

# Mostrar el resultado
tk.Label(ventana, textvariable=resultado, padx=20,
         pady=20).grid(row=row_val + 1, columnspan=4)

ventana.mainloop()
st.header("Aplicacón 2")
