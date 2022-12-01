import tkinter as tk

def main_menu (root):
    main_menu = tk.Menu(root)
    root.config (menu = main_menu) # Agregar menu al root
    menu_inicio = tk.Menu(main_menu, tearoff=0)
    menu_inicio.add_command (label="Crear Registro en BD")
    menu_inicio.add_command (label="Eliminar Registro en BD")
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
        self.formulario() # Agregar fomulario
        self.f_cancelar() # Inicializar campos

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

        self.str_var_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry (self, textvariable=self.str_var_nombre)
        self.entry_nombre.config (width=50, font=('Arial', 12))
        self.entry_nombre.grid (row=0, column=1, padx=10, pady=10, columnspan=2)
        
        self.str_var_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry (self, textvariable=self.str_var_duracion)
        self.entry_duracion.config (width=50, font=('Arial', 12))
        self.entry_duracion.grid (row=1, column=1, padx=10, pady=10, columnspan=2)
        
        self.str_var_genero = tk.StringVar()
        self.entry_genero = tk.Entry (self, textvariable=self.str_var_genero)
        self.entry_genero.config (width=50, font=('Arial', 12))
        self.entry_genero.grid (row=2, column=1, padx=10, pady=10, columnspan=2)

        # Buttons

        self.btn_nuevo = tk.Button (self, text="Nuevo", command=self.f_nuevo)
        self.btn_nuevo.config (width=20, font=('Arial', 12, 'bold'),
            fg="#DAD5D6", bg="#158645", cursor="hand2", activebackground="#35BD6F")
        self.btn_nuevo.grid (row=3, column=0, padx=10, pady=10)

        self.btn_guardar = tk.Button (self, text="Guardar", command=self.f_guardar)
        self.btn_guardar.config (width=20, font=('Arial', 12, 'bold'),
            fg="#DAD5D6", bg="#1658A2", cursor="hand2", activebackground="#3586DF")
        self.btn_guardar.grid (row=3, column=1, padx=10, pady=10)

        self.btn_cancelar = tk.Button (self, text="Cancelar", command=self.f_cancelar)
        self.btn_cancelar.config (width=20, font=('Arial', 12, 'bold'),
            fg="#DAD5D6", bg="#BD152E", cursor="hand2", activebackground="#E15370")
        self.btn_cancelar.grid (row=3, column=2, padx=10, pady=10)
    
    
    def f_nuevo (self):
        
        self.str_var_nombre.set('')
        self.str_var_duracion.set('')
        self.str_var_genero.set('')

        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')
        self.btn_nuevo.config(state='disabled')
        self.btn_guardar.config(state='normal')
        self.btn_cancelar.config(state='normal')

    
    def f_cancelar (self):

        self.str_var_nombre.set('')
        self.str_var_duracion.set('')
        self.str_var_genero.set('')

        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')
        self.btn_nuevo.config(state='normal')
        self.btn_guardar.config(state='disabled')
        self.btn_cancelar.config(state='disabled')
        
    def f_guardar (self):

        self.f_cancelar() # Reiniciar campos