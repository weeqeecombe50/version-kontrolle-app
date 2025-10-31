import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title('Version Kontrolle App')
        self.create_widgets()

    def create_widgets(self):
        self.add_file_button = tk.Button(self.root, text='Datei hinzufügen', command=self.add_file)
        self.add_file_button.pack()

    def add_file(self):
        # Logik zum Hinzufügen einer Datei
        pass

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
