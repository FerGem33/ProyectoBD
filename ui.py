import tkinter as tk
from tkinter import ttk, messagebox
from dao.pelicula_dao import obtener_peliculas, agregar_pelicula, actualizar_pelicula, eliminar_pelicula
from dao.genero_dao import obtener_generos, obtener_genero
from dao.actor_dao import obtener_actores, obtener_actor
from dao.director_dao import obtener_directores, obtener_director

def crear_combobox(frame, label, opciones):
    ttk.Label(frame, text=label).pack(anchor="w", padx=10)
    combo = ttk.Combobox(frame, values=[f"{o[0]} - {o[1]}" for o in opciones], state="readonly")
    combo.pack(fill="x", padx=10, pady=5)
    return combo

def tab_peliculas(tab):
    frame = ttk.LabelFrame(tab, text="Gestión de Películas")
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    tree = ttk.Treeview(frame, columns=("Id", "Nombre", "Genero", "Clasificación", "Duración", "Actor", "Director"), show="headings")
    tree.heading("Id", text="Id")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Genero", text="Genero")
    tree.heading("Clasificación", text="Clasificación")
    tree.heading("Duración", text="Duración")
    tree.heading("Actor", text="Actor")
    tree.heading("Director", text="Director")
    tree.pack(fill="both", padx=10, pady=10)

    def cargar_peliculas():
        for i in tree.get_children():
            tree.delete(i)
        for p in obtener_peliculas():
            row = (p[0], p[4], obtener_genero(p[1]), p[5], p[6], obtener_actor(p[2]), obtener_director(p[3]))
            tree.insert("", "end", values=row)

    cargar_peliculas()

    # Formulario
    combo_genero = crear_combobox(frame, "Género", obtener_generos())
    combo_actor = crear_combobox(frame, "Actor", obtener_actores())
    combo_director = crear_combobox(frame, "Director", obtener_directores())
    entry_nombre = ttk.Entry(frame)
    entry_clasificacion = ttk.Entry(frame)
    entry_duracion = ttk.Entry(frame)

    for label, widget in zip([
        "Nombre", "Clasificación", "Duración"],
        [entry_nombre, entry_clasificacion, entry_duracion]):
        ttk.Label(frame, text=label).pack(anchor="w", padx=10)
        widget.pack(fill="x", padx=10, pady=5)

    # Insertar
    def insertar():
        try:
            agregar_pelicula(
                entry_nombre.get(),
                entry_clasificacion.get(),
                int(entry_duracion.get()),
                int(combo_genero.get().split(" - ")[0]),
                int(combo_actor.get().split(" - ")[0]),
                int(combo_director.get().split(" - ")[0])
            )
            cargar_peliculas()
            messagebox.showinfo("Éxito", "Película insertada")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Actualizar
    def actualizar():
        try:
            seleccionado = tree.item(tree.selection())['values']
            if not seleccionado:
                return
            id_peli = seleccionado[0]
            actualizar_pelicula(
                id_peli,
                entry_nombre.get(),
                entry_clasificacion.get(),
                int(entry_duracion.get()),
                int(combo_genero.get().split(" - ")[0]),
                int(combo_actor.get().split(" - ")[0]),
                int(combo_director.get().split(" - ")[0])                
            )
            cargar_peliculas()
            messagebox.showinfo("Éxito", "Película actualizada")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Eliminar
    def eliminar():
        try:
            seleccionado = tree.item(tree.selection())['values']
            if not seleccionado:
                return
            eliminar_pelicula(int(seleccionado[0]))
            cargar_peliculas()
            messagebox.showinfo("Éxito", "Película eliminada")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Botones
    btn_frame = ttk.Frame(frame)
    btn_frame.pack(pady=10)
    ttk.Button(btn_frame, text="Insertar", command=insertar).grid(row=0, column=0, padx=5)
    ttk.Button(btn_frame, text="Actualizar", command=actualizar).grid(row=0, column=1, padx=5)
    ttk.Button(btn_frame, text="Eliminar", command=eliminar).grid(row=0, column=2, padx=5)

    # Autocompletar campos al seleccionar
    def al_seleccionar(event):
        try:
            seleccionado = tree.item(tree.selection())['values']
            if not seleccionado:
                return
            entry_nombre.delete(0, tk.END)
            entry_nombre.insert(0, seleccionado[1])
            entry_clasificacion.delete(0, tk.END)
            entry_clasificacion.insert(0, seleccionado[3])
            entry_duracion.delete(0, tk.END)
            entry_duracion.insert(0, seleccionado[4])
        except:
            pass

    tree.bind("<<TreeviewSelect>>", al_seleccionar)

def crear_interfaz():
    root = tk.Tk()
    root.title("Sistema de Cine")
    root.state("zoomed")

    tabs = ttk.Notebook(root)
    tabs.pack(fill="both", expand=True)

    tab_peliculas_frame = ttk.Frame(tabs)
    tabs.add(tab_peliculas_frame, text="Películas")
    tab_peliculas(tab_peliculas_frame)

    root.mainloop()

crear_interfaz()
