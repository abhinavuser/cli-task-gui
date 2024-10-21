import customtkinter as ctk
import app  # Ensure this imports your app module

class TaskManagerApp:
    def __init__(self, master):
        self.master = master
        master.title("Task Manager")

        # Configure main frame
        self.frame = ctk.CTkFrame(master)
        self.frame.pack(padx=20, pady=20)

        self.label = ctk.CTkLabel(self.frame, text="Task Manager", font=("Arial", 24, "bold"))
        self.label.pack(pady=(0, 20))

        # Project Entry
        self.project_name_entry = ctk.CTkEntry(self.frame, placeholder_text="Project Name", width=250)
        self.project_name_entry.pack(pady=10)

        self.add_project_button = ctk.CTkButton(self.frame, text="Add Project", command=self.add_project)
        self.add_project_button.pack(pady=5)

        # Task Entry
        self.task_description_entry = ctk.CTkEntry(self.frame, placeholder_text="Task Description", width=250)
        self.task_description_entry.pack(pady=10)

        self.project_id_entry = ctk.CTkEntry(self.frame, placeholder_text="Project ID (for Task)", width=250)
        self.project_id_entry.pack(pady=10)

        self.add_task_button = ctk.CTkButton(self.frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=10)

        # Output label for messages
        self.output_label = ctk.CTkLabel(self.frame, text="", font=("Arial", 14))
        self.output_label.pack(pady=10)

        self.project_dropdown = ctk.CTkComboBox(self.frame, values=[], width=250)
        self.project_dropdown.pack(pady=10)


        # Configure the theme
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("green")

    def add_project(self):
        project_name = self.project_name_entry.get()
        if project_name:
            response = app.main_function('add-project', project_name)
            self.output_label.configure(text=response)
            self.project_name_entry.delete(0, ctk.END)
            self.animate_label(self.output_label)

    def add_task(self):
        try:
            project_id = int(self.project_id_entry.get())
            description = self.task_description_entry.get()
            response = app.main_function('add-task', project_id, description)
            self.output_label.configure(text=response)
            self.project_id_entry.delete(0, ctk.END)
            self.task_description_entry.delete(0, ctk.END)
            self.animate_label(self.output_label)
        except ValueError:
            self.output_label.configure(text="Invalid project ID.")

    def animate_label(self, label):
        original_color = label.cget("text_color")
        label.configure(text_color="orange")
        label.after(200, lambda: label.configure(text_color=original_color))

if __name__ == "__main__":
    root = ctk.CTk()
    app = TaskManagerApp(root)
    root.mainloop()
