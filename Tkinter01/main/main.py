import tkinter as tk
from client.gui import Frame, main_menu

def main():
    root = tk.Tk()
    root.title('Catalogo de peliculas')
    # root.resizable(False, False) # No se podra modificar de tamanio del root
    main_menu (root) # Crear el menu superior en el root

    frame = Frame(root)
    frame.mainloop()


if __name__ == "__main__":
    main()