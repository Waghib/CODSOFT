import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
import random, string

class PasswordGeneratorApp(ThemedTk):
    def __init__(self):
        super().__init__()
        
        self.set_theme("breeze")
        self.geometry("500x420")
        self.title("Password Generator")

        self.big_frame = ttk.Frame(self)
        self.big_frame.pack(fill="both", expand=True)

        self.createWidget()

    def createWidget(self):
        
        # Header Frame
        header_frame = tk.Frame(self.big_frame, bg='#3DAEE9')
        header_frame.pack(fill="x")

        # Header Label
        header_label = ttk.Label(header_frame, text="RANDOM PASSWORD GENERATOR", font=('Helvetica', 16), foreground='white', background='#3DAEE9')
        header_label.pack(pady=10)
        
        self.buttonFrame = ttk.Frame(self.big_frame)
        self.buttonFrame.pack(pady=5)

        self.labelFrame = ttk.Frame(self.buttonFrame)
        self.labelFrame.pack(pady=5)

        # Label and input for name 
        self.nameLabel = ttk.Label(self.labelFrame, text="Enter your name: ", font=('Helvetica', 14))
        self.nameLabel.grid(row=0, column=0, pady=10)
        self.nameInput = ttk.Entry(self.labelFrame,width=30)
        self.nameInput.grid(row=0,column=1,padx=10, pady=10)

        # Label and input for password length
        self.passLengthLabel = ttk.Label(self.labelFrame, text="Enter password length: ", font=('Helvetica', 14))
        self.passLengthLabel.grid(row=1, column=0, pady=10)
        self.passLengthInput = ttk.Entry(self.labelFrame,width=30)
        self.passLengthInput.grid(row=1,column=1,padx=10, pady=10)

        # Label and output for password generated
        self.passGenerated = ttk.Label(self.labelFrame, text="Generated password: ", font=('Helvetica', 14))
        self.passGenerated.grid(row=2, column=0, pady=10)
        self.passGeneratedOutput = ttk.Entry(self.labelFrame,width=30)
        self.passGeneratedOutput.grid(row=2,column=1,padx=10, pady=10)

        # Complexity label and scale
        self.complexityLabel = ttk.Label(self.labelFrame, text="Complexity: ", font=('Helvetica', 14))
        self.complexityLabel.grid(row=3, column=0, pady=10)
        self.complexityScale = ttk.Scale(self.labelFrame,from_=1, to=3, orient="horizontal", length=200)
        self.complexityScale.set(2)  # Default complexity
        self.complexityScale.grid(row=3,column=1,padx=10, pady=10)

        # Generate Password Button
        generate_button = ttk.Button(self.buttonFrame, text="Generate Password", command=self.generatePass)
        generate_button.pack(pady=20)

        # Copy to clipboard Button
        copyButton = ttk.Button(self.buttonFrame, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copyButton.pack()

        # Label to indicate password copied to clipboard
        self.copyStatusLabel = ttk.Label(self.buttonFrame, text="", font=('Helvetica', 9), foreground='red')
        self.copyStatusLabel.pack(pady=10)

    def generatePass(self):
        try:
            length = int(self.passLengthInput.get())
            complexity = int(self.complexityScale.get())
        except ValueError:
            self.passGeneratedOutput.delete(0, tk.END)  # Clear the Entry widget
            self.show_error_message("Invalid input. Please enter valid numbers.")
            return

        if length < 0:
            self.show_error_message("Invalid input. Please enter a positive number for length.")
            return
        elif length == 0:
            self.passGeneratedOutput.delete(0, tk.END)  # Clear the Entry widget
            self.show_error_message("Invalid input. Please enter a number greater than 0.")
            return

        password = self.generate_random_password(length, complexity)
        self.passGeneratedOutput.delete(0, tk.END)  # Clear the Entry widget
        self.passGeneratedOutput.insert(tk.END, password)
        
    def show_error_message(self, message):
        messagebox.showerror("Error", message)

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
        generated_password = self.passGeneratedOutput.get().strip()
        if generated_password:
            self.clipboard_clear()
            self.clipboard_append(generated_password)
            self.update()
            self.copyStatusLabel.config(text="Password copied to clipboard")
            self.after(3000, self.reset_copy_status)  # Reset status after 3 seconds

    def reset_copy_status(self):
        self.copyStatusLabel.config(text="")

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()