import os
import shutil
import tkinter as tk
from tkinter import filedialog

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("PRZERZUCACZKA v.2.1")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.source1_label = tk.Label(self, text="Folder źródłowy 1:")
        self.source1_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.source1_entry = tk.Entry(self)
        self.source1_entry.grid(row=0, column=1, padx=5, pady=5)
        self.source1_button = tk.Button(self, text="Wybierz folder", command=self.choose_source1)
        self.source1_button.grid(row=0, column=2, padx=5, pady=5)

        self.source2_label = tk.Label(self, text="Folder źródłowy 2:")
        self.source2_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.source2_entry = tk.Entry(self)
        self.source2_entry.grid(row=1, column=1, padx=5, pady=5)
        self.source2_button = tk.Button(self, text="Wybierz folder", command=self.choose_source2)
        self.source2_button.grid(row=1, column=2, padx=5, pady=5)

        self.source3_label = tk.Label(self, text="Folder źródłowy 3:")
        self.source3_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.source3_entry = tk.Entry(self)
        self.source3_entry.grid(row=2, column=1, padx=5, pady=5)
        self.source3_button = tk.Button(self, text="Wybierz folder", command=self.choose_source3)
        self.source3_button.grid(row=2, column=2, padx=5, pady=5)

        self.source4_label = tk.Label(self, text="Folder źródłowy 4:")
        self.source4_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.source4_entry = tk.Entry(self)
        self.source4_entry.grid(row=3, column=1, padx=5, pady=5)
        self.source4_button = tk.Button(self, text="Wybierz folder", command=self.choose_source4)
        self.source4_button.grid(row=3, column=2, padx=5, pady=5)

        self.source5_label = tk.Label(self, text="Folder źródłowy 5:")
        self.source5_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.source5_entry = tk.Entry(self)
        self.source5_entry.grid(row=4, column=1, padx=5, pady=5)
        self.source5_button = tk.Button(self, text="Wybierz folder", command=self.choose_source5)
        self.source5_button.grid(row=4, column=2, padx=5, pady=5)

        self.destination_label = tk.Label(self, text="Folder docelowy:")
        self.destination_label.grid(row=5 , column=0, padx=5, pady=5, sticky="w")
        self.destination_entry = tk.Entry(self)
        self.destination_entry.grid(row=5, column=1, padx=5, pady=5)
        self.destination_button = tk.Button(self, text="Wybierz folder", command=self.choose_destination)
        self.destination_button.grid(row=5, column=2, padx=5, pady=5)

        self.move_button = tk.Button(self, text="Przenieś pliki", command=self.move_files)
        self.move_button.grid(row=6, column=1, padx=5, pady=5)

    def choose_source1(self):
        folder_path = filedialog.askdirectory()
        self.source1_entry.delete(0, tk.END)
        self.source1_entry.insert(0, folder_path)

    def choose_source2(self):
        folder_path = filedialog.askdirectory()
        self.source2_entry.delete(0, tk.END)
        self.source2_entry.insert(0, folder_path)

    def choose_source3(self):
        folder_path = filedialog.askdirectory()
        self.source3_entry.delete(0, tk.END)
        self.source3_entry.insert(0, folder_path)

    def choose_source4(self):
        folder_path = filedialog.askdirectory()
        self.source4_entry.delete(0, tk.END)
        self.source4_entry.insert(0, folder_path)

    def choose_source5(self):
        folder_path = filedialog.askdirectory()
        self.source5_entry.delete(0, tk.END)
        self.source5_entry.insert(0, folder_path)

    def choose_destination(self):
        folder_path = filedialog.askdirectory()
        self.destination_entry.delete(0, tk.END)
        self.destination_entry.insert(0, folder_path)

    def move_files(self):
        sources = [self.source1_entry.get(), self.source2_entry.get(), self.source3_entry.get(),
                   self.source4_entry.get(), self.source5_entry.get()]
        destination = self.destination_entry.get()

        for source in sources:
            if source:
                for file_name in os.listdir(source):
                    source_path = os.path.join(source, file_name)
                    destination_path = os.path.join(destination, file_name)
                    shutil.move(source_path, destination_path)
                    print(f"{file_name} przeniesiono pomyślnie.")

        tk.messagebox.showinfo(title="Przeniesiono pliki", message="Pliki zostały przeniesione do wybranego folderu.")

root = tk.Tk()
app = Application(master=root)
app.mainloop()

