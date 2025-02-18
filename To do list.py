import json
from datetime import datetime

class TaskItem:
    def _init_(self, name, details, importance, due_date):
        self.name = name
        self.details = details
        self.importance = importance
        self.due_date = due_date

    def to_dict(self):
        return {
            'name': self.name,
            'details': self.details,
            'importance': self.importance,
            'due_date': self.due_date
        }

    @staticmethod
    def from_dict(data):
        return TaskItem(data['name'], data['details'], data['importance'], data['due_date'])

class TaskManager:
    def _init_(self):
        self.task_list = []

    def add_task(self, name, details, importance, due_date):
        task = TaskItem(name, details, importance, due_date)
        self.task_list.append(task)
        print(f'Task "{name}" has been added to your list.')

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.task_list):
            removed_task = self.task_list.pop(task_index)
            print(f'Task "{removed_task.name}" has been removed from your list.')
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if not self.task_list:
            print("Your task list is currently empty.")
        else:
            sorted_tasks = sorted(self.task_list, key=lambda x: x.importance)
            print("Your task list:")
            for index, task in enumerate(sorted_tasks):
                print(f"{index}. [Importance: {task.importance}] {task.name} - {task.details} (Due: {task.due_date})")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump([task.to_dict() for task in self.task_list], file)
        print(f'Tasks have been saved to {filename}.')

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.task_list = [TaskItem.from_dict(task) for task in json.load(file)]
            print(f'Tasks have been loaded from {filename}.')
        except FileNotFoundError:
            print(f'The file {filename} does not exist.')
        except json.JSONDecodeError:
            print('There was an error reading the JSON from the file.')

def main():
    task_manager = TaskManager()
    
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Display Tasks")
        print("4. Save Tasks")
        print("5. Load Tasks")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ")
        
        if choice == '1':
            name = input("Enter the task name: ")
            details = input("Enter the task details: ")
            importance = int(input("Enter the task importance (1-5, 1 being the highest): "))
            due_date = input("Enter the task due date (YYYY-MM-DD): ")
            task_manager.add_task(name, details, importance, due_date)
        elif choice == '2':
            task_manager.display_tasks()
            task_index = int(input("Enter the task index to delete: "))
            task_manager.delete_task(task_index)
        elif choice == '3':
            task_manager.display_tasks()
        elif choice == '4':
            filename = input("Enter the filename to save tasks (e.g., tasks.json): ")
            task_manager.save_to_file(filename)
        elif choice == '5':
            filename = input("Enter the filename to load tasks (e.g., tasks.json): ")
            task_manager.load_from_file(filename)
        elif choice == '6':
            print("Exiting the Task Manager application.")
            break
        else:
            print("Invalid selection. Please choose a valid option.")

if _name_ == "_main_":
    main()