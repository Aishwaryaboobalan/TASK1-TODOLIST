import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self,project):
        self.project=project
        self.project.title("To-Do List App")

        self.tasks=[]

        self.task_entry=tk.Entry(project, width=40)
        self.task_entry.pack(pady=10)

        self.add_task_button=tk.Button(project, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

        self.task_listbox=tk.Listbox(project, width=50)
        self.task_listbox.pack(pady=10)

        self.delete_task_button=tk.Button(project, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack()

        self.refresh_tasks()

    def add_task(self):
        task=self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.refresh_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_task_index=self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.refresh_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

def main():
    root=tk.Tk()
    app=TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
