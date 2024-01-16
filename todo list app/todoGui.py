import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from ttkthemes import ThemedTk

class TodoListApp(ThemedTk):
    def __init__(self):
        super().__init__()
        
        self.set_theme("radiance")
        self.geometry("400x450")
        self.title("To Do List App")

        self.big_frame = ttk.Frame(self)
        self.big_frame.pack(fill="both", expand=True)

        self.createWidget()

    def createWidget(self):
        self.taskInput = ttk.Entry(self.big_frame,width=30)
        self.taskInput.pack(pady=10)

        self.addBtn = ttk.Button(self.big_frame, text="Add task", command=self.addTask)
        self.addBtn.pack(pady=5)

        self.taskList = tk.Listbox(self.big_frame,selectmode=tk.SINGLE)
        self.taskList.pack(pady=5)

        self.buttonFrame = ttk.Frame(self.big_frame)
        self.buttonFrame.pack(pady=5)

        self.editBtn = ttk.Button(self.buttonFrame, text="Edit Text", command=self.editTask)
        self.editBtn.grid(row=0, column=0, padx=5)

        self.deleteBtn = ttk.Button(self.buttonFrame, text="Delete Text", command=self.deleteTask)
        self.deleteBtn.grid(row=0, column=1, padx=5)

        self.saveBtn = ttk.Button(self.big_frame, text="Save", command=self.saveTask)
        self.saveBtn.pack(pady=5)

        self.loadBtn = ttk.Button(self.big_frame, text="Load", command=self.loadTask)
        self.loadBtn.pack(pady=5)

    def addTask(self):
        task = self.taskInput.get()
        if task:
            self.taskList.insert(tk.END,task)
            self.taskInput.delete(0,tk.END)
        
    def editTask(self):
        taskIndex = self.taskList.curselection()
        if taskIndex:
            newTask = self.taskInput.get()
            if newTask:
                self.taskList.delete(taskIndex)
                self.taskList.insert(taskIndex, newTask)
                self.taskInput.delete(0, tk.END)

    def deleteTask(self):
        taskIndex = self.taskList.curselection()
        if taskIndex:
            self.taskList.delete(taskIndex)
        
    def saveTask(self):
        tasks = self.taskList.get(0, tk.END)
        if tasks:
            filePath = filedialog.asksaveasfilename(defaultextension=".txt")
            if filePath:
                with open(filePath,'w') as file:
                    for task in tasks:
                        file.write(task + "\n")
        
    def loadTask(self):
        filePath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if filePath:
            with open(filePath, 'r') as file:
                tasks = [line.strip() for line in file.readlines()]

            self.taskList.delete(0,tk.END)

            for task in tasks:
                self.taskList.insert(tk.END, task)

if __name__ == "__main__":
    app = TodoListApp()
    app.mainloop()