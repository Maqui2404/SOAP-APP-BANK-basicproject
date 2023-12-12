import tkinter as tk
from tkinter import messagebox
from zeep import Client

def deposit():
    try:
        amount = int(amount_entry.get())
        response = client.service.deposit('usuario1', amount)
        messagebox.showinfo("Depósito exitoso", response)
    except Exception as e:
        messagebox.showerror("Error", f"Error al realizar el depósito: {e}")

def withdraw():
    try:
        amount = int(amount_entry.get())
        response = client.service.withdraw('usuario1', amount)
        messagebox.showinfo("Retiro exitoso", response)
    except Exception as e:
        messagebox.showerror("Error", f"Error al realizar el retiro: {e}")

# Crear cliente SOAP
url = 'http://localhost:8000/?wsdl'
client = Client(url)

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Servicio SOAP")

# Etiqueta e input para ingresar la cantidad
amount_label = tk.Label(root, text="Cantidad:")
amount_label.pack()

amount_entry = tk.Entry(root)
amount_entry.pack()

# Botones para depositar y retirar
deposit_button = tk.Button(root, text="Depositar", command=deposit)
deposit_button.pack()

withdraw_button = tk.Button(root, text="Retirar", command=withdraw)
withdraw_button.pack()

# Ejecutar la interfaz
root.mainloop()
