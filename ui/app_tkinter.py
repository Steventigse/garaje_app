import tkinter as tk
from tkinter import messagebox
from servicios.garaje_servicio import GarajeServicio


class AppGaraje:

    def __init__(self, root):

        self.root = root
        self.root.title("Sistema Básico de Gestión de Garaje")

        self.servicio = GarajeServicio()

        # Título
        titulo = tk.Label(root, text="Registro de Vehículos", font=("Arial", 14))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Etiquetas
        tk.Label(root, text="Placa").grid(row=1, column=0)
        tk.Label(root, text="Marca").grid(row=2, column=0)
        tk.Label(root, text="Propietario").grid(row=3, column=0)

        # Campos de texto
        self.entry_placa = tk.Entry(root)
        self.entry_marca = tk.Entry(root)
        self.entry_propietario = tk.Entry(root)

        self.entry_placa.grid(row=1, column=1)
        self.entry_marca.grid(row=2, column=1)
        self.entry_propietario.grid(row=3, column=1)

        # Botones
        boton_agregar = tk.Button(root, text="Agregar Vehículo", command=self.agregar_vehiculo)
        boton_limpiar = tk.Button(root, text="Limpiar", command=self.limpiar_campos)

        boton_agregar.grid(row=4, column=0, pady=10)
        boton_limpiar.grid(row=4, column=1)

        # Lista de vehículos
        self.lista = tk.Listbox(root, width=50)
        self.lista.grid(row=5, column=0, columnspan=2, pady=10)

    # Función para agregar vehículo
    def agregar_vehiculo(self):

        placa = self.entry_placa.get()
        marca = self.entry_marca.get()
        propietario = self.entry_propietario.get()

        if placa and marca and propietario:

            self.servicio.agregar_vehiculo(placa, marca, propietario)

            self.actualizar_lista()

            self.limpiar_campos()

        else:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")

    # Actualizar lista
    def actualizar_lista(self):

        self.lista.delete(0, tk.END)

        for vehiculo in self.servicio.listar_vehiculos():
            self.lista.insert(tk.END, vehiculo)

    # Limpiar campos
    def limpiar_campos(self):

        self.entry_placa.delete(0, tk.END)
        self.entry_marca.delete(0, tk.END)
        self.entry_propietario.delete(0, tk.END)