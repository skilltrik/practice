import json
import os

task_file = 'tasks.json'

# Попытка поиска файла, если его нет - возвращает пустой список, иначе - происходит проверка на целостность (являются ли получаемые данные списком)
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

# Сохранение
def save(tasks: list):
    with open(task_file, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=2)