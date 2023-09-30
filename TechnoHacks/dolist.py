import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []
        
        # Create and set up the GUI
        self.create_widgets()
        
    def create_widgets(self):
        # Entry widget for task input
        self.task_entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.task_entry.pack(pady=10)
        
        # Button to add tasks
        add_button = tk.Button(self.root, text="Add Task", command=self.add_task, font=("Helvetica", 12))
        add_button.pack(pady=10)
        
        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.root, font=("Helvetica", 14), selectbackground="#a6a6a6")
        self.task_listbox.pack(pady=20)
        
        # Button to delete selected task
        delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task, font=("Helvetica", 12))
        delete_button.pack(pady=10)
        
        # Button to clear all tasks
        clear_all_button = tk.Button(self.root, text="Clear All", command=self.clear_all_tasks, font=("Helvetica", 12))
        clear_all_button.pack(pady=10)
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")
    
    def clear_all_tasks(self):
        self.tasks = []
        self.update_task_list()
    
    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert(tk.END, f"{i}. {task}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
