import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from ttkthemes import ThemedTk

class TodoListApp(ThemedTk):
    def __init__(self):
        super().__init__()
        
        self.set_theme("radiance")
        self.geometry("500x500")
        self.title("To Do List App")

        self.big_frame = ttk.Frame(self)
        self.big_frame.pack(fill="both", expand=True)

        self.createWidget()

    def createWidget(self):

        # Header Frame
        header_frame = tk.Frame(self.big_frame, bg='#F59F78')
        header_frame.pack(fill="x")

        # Header Label
        header_label = ttk.Label(header_frame, text="TO DO LIST", font=('Helvetica', 16), foreground='white', background='#F59F78')
        header_label.pack(pady=10)
        
        self.taskInputFrame = ttk.Frame(self.big_frame)
        self.taskInputFrame.pack(pady=5)

        self.taskInput = ttk.Entry(self.taskInputFrame,width=30)
        self.taskInput.grid(row=0,column=0,pady=10)

        self.addBtn = ttk.Button(self.taskInputFrame, text="Add task", command=self.addTask)
        self.addBtn.grid(row=0,column=1,padx=10, pady=5)

        self.taskTree = ttk.Treeview(self.big_frame, columns=('Task', 'Edit', 'Delete'))
        self.taskTree.column('#0', width=0, stretch=tk.NO)
        self.taskTree.column('Task', anchor=tk.W, width=150)
        self.taskTree.column('Edit', anchor=tk.W, width=50)
        self.taskTree.column('Delete', anchor=tk.W, width=50)

        self.taskTree.heading('#0', text='', anchor=tk.W)
        self.taskTree.heading('Task', text='Task', anchor=tk.W)
        self.taskTree.heading('Edit', text='', anchor=tk.W)
        self.taskTree.heading('Delete', text='', anchor=tk.W)

        self.taskTree.pack(pady=5)

        self.saveBtn = ttk.Button(self.big_frame, text="Save", command=self.saveTask)
        self.saveBtn.pack(pady=5)

        self.loadBtn = ttk.Button(self.big_frame, text="Load", command=self.loadTask)
        self.loadBtn.pack(pady=5)
        
            # Bind the Edit and Delete actions to the Treeview
        self.taskTree.bind('<ButtonRelease-1>', self.handle_treeview_click)

    def handle_treeview_click(self, event):
        item_id = self.taskTree.identify_row(event.y)
        if item_id:
            column = self.taskTree.identify_column(event.x)
            if column == '#2':
                self.editTask(item_id)
            elif column == '#3':
                self.deleteTask(item_id)

    def addTask(self):
        task = self.taskInput.get()
        if task:
            self.taskTree.insert('', 'end', text='', values=(task, 'Edit', 'Delete'))
            self.taskInput.delete(0, tk.END)
        
    def editTask(self, item):
        newTask = self.taskInput.get()
        if newTask:
            self.taskTree.item(item, values=(newTask, 'Edit', 'Delete'))
            self.taskInput.delete(0, tk.END)

    def deleteTask(self, item):
        self.taskTree.delete(item)

    def saveTask(self):
        tasks = [(self.taskTree.item(item, 'values')[0]) for item in self.taskTree.get_children()]
        if tasks:
            filePath = filedialog.asksaveasfilename(defaultextension=".txt")
            if filePath:
                with open(filePath, 'w') as file:
                    for task in tasks:
                        file.write(task + "\n")
        
    def loadTask(self):
        filePath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if filePath:
            for item in self.taskTree.get_children():
                self.taskTree.delete(item)
            with open(filePath, 'r') as file:
                tasks = [line.strip() for line in file.readlines()]

            for task in tasks:
                self.taskTree.insert('', 'end', text='', values=(task, 'Edit', 'Delete'))

if __name__ == "__main__":
    app = TodoListApp()
    app.mainloop()