import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip  # Module for clipboard operations

class PasswordGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Random Password Generator")
        self.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        # Password Length Label and Entry
        length_label = ttk.Label(self, text="Password Length:")
        length_label.pack(pady=10)

        self.length_entry = ttk.Entry(self)
        self.length_entry.pack(pady=5)

        # Complexity Label and Scale
        complexity_label = ttk.Label(self, text="Password Complexity:")
        complexity_label.pack(pady=10)

        self.complexity_scale = ttk.Scale(self, from_=1, to=3, orient="horizontal", length=200)
        self.complexity_scale.set(2)  # Default complexity
        self.complexity_scale.pack(pady=5)

        # Complexity Level Label
        self.complexity_var = tk.StringVar()
        complexity_level_label = ttk.Label(self, textvariable=self.complexity_var, font=("Helvetica", 10, "bold"))
        complexity_level_label.pack(pady=5)

        # Generate Password Button
        generate_button = ttk.Button(self, text="Generate Password", command=self.generate_password)
        generate_button.pack(pady=10)

        # Display generated password
        password_label = ttk.Label(self, text="Generated Password:", font=("Helvetica", 10, "bold"))
        password_label.pack()

        self.password_text = tk.Text(self, height=1, width=30, font=("Courier", 12))
        self.password_text.pack(pady=5)

        # Copy to Clipboard Button
        copy_button = ttk.Button(self, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_button.pack(pady=20)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            complexity = int(self.complexity_scale.get())
        except ValueError:
            self.password_text.delete(1.0, tk.END)
            self.password_text.insert(tk.END, "Invalid input. Please enter valid numbers.")
            return

        if length <= 0:
            self.password_text.delete(1.0, tk.END)
            self.password_text.insert(tk.END, "Invalid input. Please enter a positive number for length.")
            return

        password = self.generate_random_password(length, complexity)
        self.password_text.delete(1.0, tk.END)
        self.password_text.insert(tk.END, password)

        complexity_labels = ["Low", "Medium", "High"]
        self.complexity_var.set(f"Complexity: {complexity_labels[complexity - 1]}")

    def generate_random_password(self, length, complexity):
        if complexity == 1:
            characters = string.ascii_letters
        elif complexity == 2:
            characters = string.ascii_letters + string.digits
        elif complexity == 3:
            characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def copy_to_clipboard(self):
        generated_password = self.password_text.get(1.0, tk.END).strip()
        if generated_password:
            pyperclip.copy(generated_password)

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()