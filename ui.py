import tkinter as tk
from tkinter import ttk
import style
from operations import obtener_datos

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Conexión Oracle - App Moderna")
        self.geometry("500x400")
        self.configure(bg=style.COLORS["bg"])
        self.resizable(False, False)

        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="Lista de Clientes", bg=style.COLORS["bg"],
                                    fg=style.COLORS["fg"], font=("Segoe UI", 14, "bold"))
        self.title_label.pack(pady=20)

        self.tree = ttk.Treeview(self, columns=("Nombre",), show="headings", height=10)
        self.tree.heading("Nombre", text="Nombre")
        self.tree.column("Nombre", anchor="center", width=450)
        self.tree.pack(pady=10)

        self.style_tree()

    def style_tree(self):
        style_tree = ttk.Style()
        style_tree.theme_use("clam")
        style_tree.configure("Treeview",
                             background=style.COLORS["entry_bg"],
                             foreground=style.COLORS["fg"],
                             rowheight=25,
                             fieldbackground=style.COLORS["entry_bg"],
                             font=style.FONT)
        style_tree.configure("Treeview.Heading",
                             background=style.COLORS["accent"],
                             foreground="white",
                             font=("Segoe UI", 10, "bold"))

    def load_data(self):
        datos = obtener_datos()
        for nombre, in datos:
            self.tree.insert("", "end", values=(nombre,))
