import json
import os
from datetime import datetime
import sys

TASKS_FILE = 'tasks.json'

def init_tasks_file():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w') as file:
            json.dump({"projects": [], "tasks": []}, file)

def read_data():
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

def write_data(data):
    with open(TASKS_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_project(project_name):
    data = read_data()
    projects = data["projects"]
    project_id = len(projects) + 1
    new_project = {
        "id": project_id,
        "name": project_name
    }
    projects.append(new_project)
    write_data(data)
    print(f"Project added successfully (ID: {project_id})")

def add_task(project_id, description):
    data = read_data()
    tasks = data["tasks"]

    # Check if the project exists
    project_exists = any(project['id'] == project_id for project in data['projects'])
    if not project_exists:
        print(f"Project with ID {project_id} does not exist.")
        return

    task_id = len(tasks) + 1
    new_task = {
        "id": task_id,
        "projectId": project_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    write_data(data)
    print(f"Task added successfully under project {project_id} (ID: {task_id})")

def update_task(task_id, new_description):
    data = read_data()
    tasks = data["tasks"]
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().isoformat()
            write_data(data)
            print(f"Task {task_id} updated successfully.")
            return
    print(f"Task with ID {task_id} not found.")

def delete_task(task_id):
    data = read_data()
    tasks = data["tasks"]
    tasks = [task for task in tasks if task['id'] != task_id]
    data["tasks"] = tasks
    write_data(data)
    print(f"Task {task_id} deleted successfully.")

def mark_task_status(task_id, status):
    data = read_data()
    tasks = data["tasks"]
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            write_data(data)
            print(f"Task {task_id} marked as {status}.")
            return
    print(f"Task with ID {task_id} not found.")

def list_tasks(project_id=None, status=None):
    data = read_data()
    tasks = data["tasks"]
    if project_id:
        tasks = [task for task in tasks if task['projectId'] == project_id]
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    for task in tasks:
        print(f"{task['id']}: {task['description']} [{task['status']}] (Created: {task['createdAt']}, Updated: {task['updatedAt']})")

def list_projects():
    data = read_data()
    projects = data["projects"]
    for project in projects:
        print(f"{project['id']}: {project['name']}")

        

# (Keep your existing code but remove the main() part and add a few callable functions)

# Call this to interact with your app programmatically.
def main_function(command, *args):
    if command == 'add-project':
        return add_project(*args)
    elif command == 'add-task':
        return add_task(*args)
    elif command == 'update-task':
        return update_task(*args)
    elif command == 'delete-task':
        return delete_task(*args)
    elif command == 'mark-in-progress':
        return mark_task_status(*args)
    elif command == 'mark-done':
        return mark_task_status(*args)
    elif command == 'list-tasks':
        return list_tasks(*args)
    elif command == 'list-projects':
        return list_projects()
    else:
        return f"Unknown command: {command}"


if __name__ == "__main__":
    main()