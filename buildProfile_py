import tkinter as tk
from tkinter import ttk

class BuildProfileWidget:
    def __init__(self, root):
        self.root = root
        self.root.title("Build Profile")
        self.create_widgets()

    def create_widgets(self):
        self.root.configure(bg="#F0F0F0")

        label_title = ttk.Label(self.root, text="Let's build your profile!", font=("Helvetica", 16), background="#F0F0F0")
        label_title.grid(row=0, column=0, columnspan=2, pady=(30, 0))

        self.create_input_field("Username", "Enter your username", 1)
        self.create_input_field("Date of birth", "DD/MM/YYYY", 2)
        self.create_input_field("Gender", "Enter your gender", 3)
        self.create_input_field("Branch of study", "Enter your branch of study", 4)
        self.create_input_field("Year of Study", "Enter your year of study", 5)

        button_done = ttk.Button(self.root, text="Done", command=self.done_button_clicked)
        button_done.grid(row=6, column=0, columnspan=2, pady=(16, 0))
        button_done.config(width=20)

    def create_input_field(self, label_text, hint_text, row):
        label = ttk.Label(self.root, text=label_text, background="#F0F0F0")
        label.grid(row=row, column=0, pady=(12, 0), padx=16, sticky="w")

        entry = ttk.Entry(self.root)
        entry.insert(0, hint_text)
        entry.grid(row=row, column=1, pady=(12, 0), padx=16, sticky="w")

    def done_button_clicked(self):
        # Add your logic here for handling the "Done" button click
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = BuildProfileWidget(root)
    root.mainloop()
