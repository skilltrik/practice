import json
import os

task_file = 'tasks.json'

def load():
    if not os.path.exists(task_file):
        return []
    with open(task_file, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            assert isinstance(data, list)
            return data
        except (json.JSONDecodeError, AssertionError):
            print("Ошибка: tasks.json повреждён.")
            return []

def save(tasks):
    with open(task_file, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=2)