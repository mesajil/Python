import tkinter as tk
from client.usergui import Frame, add_top_menu

def main():
    root = tk.Tk()
    root.title('Catalogo de peliculas')
    # root.resizable(False, False) # No se podra modificar de tamano del root
    add_top_menu (root) # Crear el menu superior en el root

    frame = Frame(root)
    frame.mainloop()


if __name__ == "__main__":
    main()