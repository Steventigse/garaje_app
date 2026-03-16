import tkinter as tk
from ui.app_tkinter import AppGaraje


def main():

    root = tk.Tk()

    app = AppGaraje(root)

    root.mainloop()


if __name__ == "__main__":
    main()