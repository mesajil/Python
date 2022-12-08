import tkinter as tk
from tkinter import ttk, messagebox
import model.model_dao as dao
from model.model_dao import Pelicula

def add_top_menu (root):
    main_menu = tk.Menu(root)
    root.config (menu = main_menu) # Agregar menu al root
    menu_inicio = tk.Menu(main_menu, tearoff=0)
    menu_inicio.add_command (label="Crear Registro en BD", command=dao.crear_tabla)
    menu_inicio.add_command (label="Eliminar Registro en BD", command=dao.borrar_tabla)
    menu_inicio.add_command (label="Salir", command=root.destroy)

    main_menu.add_cascade (label="Inicio", menu=menu_inicio)
    main_menu.add_cascade (label="Consultas")
    main_menu.add_cascade (label="Configuracion")
    main_menu.add_cascade (label="Ayuda")

    
class Frame (tk.Frame):

    def __init__ (self, root = None):
        super().__init__(root)
        self.pack()
        self.config(height=320, width=500)
        self.id_pelicula = None
        self.formulario() # Agregar fomulario
        self.tabla_peliculas() # Agregar tabla
        self.reiniciar_campos() # Inicializar campos


    def formulario (self):
        """Agrega el formulario de la aplicacion"""
        
        # Labels
        self.label_nombre = tk.Label(self, text="Nombre:")
        self.label_nombre.config (font=('Arial', 12, 'bold'))
        self.label_nombre.grid (row=0, column=0, padx=10, pady=10)
        
        self.label_duracion = tk.Label(self, text="Duracion:")
        self.label_duracion.config (font=('Arial', 12, 'bold'))
        self.label_duracion.grid (row=1, column=0, padx=10, pady=10)
        
        self.label_genero = tk.Label(self, text="Genero:")
        self.label_genero.config (font=('Arial', 12, 'bold'))
        self.label_genero.grid (row=2, column=0, padx=10, pady=10)
    
        # Entries

        self.SV_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry (self, textvariable=self.SV_nombre)
        self.entry_nombre.config (width=50, font=('Arial', 12))
        self.entry_nombre.grid (row=0, column=1, padx=10, pady=10, columnspan=2)
        
        self.SV_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry (self, textvariable=self.SV_duracion)
        self.entry_duracion.config (width=50, font=('Arial', 12))
        self.entry_duracion.grid (row=1, column=1, padx=10, pady=10, columnspan=2)
        
        self.SV_genero = tk.StringVar()
        self.entry_genero = tk.Entry (self, textvariable=self.SV_genero)
        self.entry_genero.config (width=50, font=('Arial', 12))
        self.entry_genero.grid (row=2, column=1, padx=10, pady=10, columnspan=2)

        # Buttons

        self.btn_nuevo = tk.Button (self, text="Nuevo", command=self.nuevo_registro)
        self.btn_nuevo.config (width=20, font=('Arial', 12, 'bold'),
            fg="#DAD5D6", bg="#158645", cursor="hand2", activebackground="#35BD6F")
        self.btn_nuevo.grid (row=3, column=0, padx=10, pady=10)

        self.btn_guardar = tk.Button (self, text="Guardar", command=self.guardar_registro)
        self.btn_guardar.config (width=20, font=('Arial', 12, 'bold'),
            fg="#DAD5D6", bg="#1658A2", cursor="hand2", activebackground="#3586DF")
        self.btn_guardar.grid (row=3, column=1, padx=10, pady=10)

        self.btn_cancelar = tk.Button (self, text="Cancelar", command=self.reiniciar_campos)
        self.btn_cancelar.config (width=20, font=('Arial', 12, 'bold'),
            fg="#DAD5D6", bg="#BD152E", cursor="hand2", activebackground="#E15370")
        self.btn_cancelar.grid (row=3, column=2, padx=10, pady=10)
    

    def tabla_peliculas (self):
        
        # Table
        
        self.tabla = ttk.Treeview(self, columns=('Nombre', 'Duracion', 'Genero'))
        self.tabla.grid (row=4, column=0, columnspan=4, sticky='nse')

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='DURACION')
        self.tabla.heading('#3', text='GENERO')

        try:
            self.peliculas = dao.listar_registros()
            self.peliculas.reverse() # La lista va del elemento 1 a n
            for p in self.peliculas:
                self.tabla.insert('', 0, text=p[0], values=(p[1], p[2], p[3]))
        except:
            print("No hay tabla de peliculas.")

        # Scrollbar

        self.scrollbar = ttk.Scrollbar(self,
            orient='vertical', command=self.tabla.yview)
        self.scrollbar.grid(row=4, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scrollbar.set)

        # Buttons

        self.btn_editar = tk.Button (self, text="Editar", command=self.editar_registro)
        self.btn_editar.config (width=20, font=('Arial', 12, 'bold'),
            fg="#DAD5D6", bg="#158645", cursor="hand2", activebackground="#35BD6F")
        self.btn_editar.grid (row=5, column=0, padx=10, pady=10)

        self.btn_eliminar = tk.Button (self, text="Eliminar", command=self.eliminar_registro)
        self.btn_eliminar.config (width=20, font=('Arial', 12, 'bold'),
            fg="#DAD5D6", bg="#BD152E", cursor="hand2", activebackground="#E15370")
        self.btn_eliminar.grid (row=5, column=1, padx=10, pady=10)
    

    def nuevo_registro (self, nombre='', duracion='', genero=''):
        """Reinicia los campos entry y se
        coloca en modo edicion de registro"""

        self.SV_nombre.set(nombre)
        self.SV_duracion.set(duracion)
        self.SV_genero.set(genero)

        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')
        self.btn_nuevo.config(state='disabled')
        self.btn_guardar.config(state='normal')
        self.btn_cancelar.config(state='normal')
        self.btn_editar.config(state='disabled')
        self.btn_eliminar.config(state='disabled')

    
    def reiniciar_campos (self):
        """Se utiliza para reiniciar campos de la aplicacion"""
        self.SV_nombre.set('')
        self.SV_duracion.set('')
        self.SV_genero.set('')

        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')
        self.btn_nuevo.config(state='normal')
        self.btn_guardar.config(state='disabled')
        self.btn_cancelar.config(state='disabled')
        self.btn_editar.config(state='normal')
        self.btn_eliminar.config(state='normal')

        self.id_pelicula = None
        
        
    def guardar_registro (self):
        pelicula = Pelicula (self.SV_nombre.get(),
            self.SV_duracion.get(), self.SV_genero.get())
        if (self.id_pelicula == None):
            if (dao.guardar_registro (pelicula)):
                self.tabla_peliculas() # Reiniciar tabla
        else:
            dao.editar (pelicula, self.id_pelicula)
            self.tabla_peliculas() # Reiniciar tabla
        self.reiniciar_campos() # Reiniciar campos
        self.id_pelicula = None

    
    def editar_registro (self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            nombre = self.tabla.item(self.tabla.selection())['values'][0]
            duracion = self.tabla.item(self.tabla.selection())['values'][1]
            genero = self.tabla.item(self.tabla.selection())['values'][2]
            self.nuevo_registro(nombre, duracion, genero)
        except:
            title = 'Edicion de datos'
            message = 'Debe elegir una pelicula de la tabla.'
            messagebox.showerror(title, message)


    def eliminar_registro (self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            dao.eliminar(self.id_pelicula)
            self.id_pelicula = None
            self.tabla_peliculas() # Reiniciar tabla
        except:
            title = 'Elimninar pelicula'
            message = 'Debe elegir una pelicula de la tabla.'
            messagebox.showerror(title, message)


        