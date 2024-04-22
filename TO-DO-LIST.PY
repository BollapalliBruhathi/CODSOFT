import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = []

        self.frame_tasks = tk.Frame(self.root)
        self.frame_tasks.pack()

        self.listbox_tasks = tk.Listbox(self.frame_tasks, height=15, width=60)
        self.listbox_tasks.pack(side=tk.LEFT)

        self.scrollbar_tasks = tk.Scrollbar(self.frame_tasks)
        self.scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox_tasks.config(yscrollcommand=self.scrollbar_tasks.set)
        self.scrollbar_tasks.config(command=self.listbox_tasks.yview)

        self.entry_task = tk.Entry(self.root, width=50)
        self.entry_task.pack()

        self.button_add_task = tk.Button(self.root, text="Add task", width=55, command=self.add_task)
        self.button_add_task.pack()

        self.button_update_task = tk.Button(self.root, text="Update task", width=55, command=self.update_task)
        self.button_update_task.pack()

        self.button_Track_task = tk.Button(self.root, text="Track task", width=55, command=self.Track_task)
        self.button_Track_task.pack()

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append(task)
            self.listbox_tasks.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def update_task(self):
        try:
            selected_index = self.listbox_tasks.curselection()[0]
            updated_task = self.entry_task.get()
            if updated_task:
                self.tasks[selected_index] = updated_task
                self.listbox_tasks.delete(selected_index)
                self.listbox_tasks.insert(selected_index, updated_task)
                self.entry_task.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter a task.")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def Track_task(self):
        try:
            selected_index = self.listbox_tasks.curselection()[0]
            self.listbox_tasks.Track(selected_index)
            del self.tasks[selected_index]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to Track.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
