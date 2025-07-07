import json
import os
import re

task_file = 'tasks.json'

def load():
    if not os.path.exists(task_file):
        return []
    with open(task_file, 'r', encoding='utf-8') as file:
        return json.load(file)

def read(tasks):
    print('\n===================')
    for task in tasks:
        status = get_status(task)
        print(f"{task['id']}. {task['title']} {status}")
    print('===================')

def read_id(tasks):
    id = get_id()
    print('\n===================')
    for task in tasks:
        status = get_status(task)
        if task["id"] == id:
            print(f"{task['title']}. {status}\n{task['description']}. \n{task['tags']}")
    print('===================')

def add(tasks):
    title = input('Введите название: ')
    id  = max([task["id"] for task in tasks], default=0) + 1
    description = input('Введите описание: ')
    tags = get_tags()
    tasks.append({'id': id, 'title': title, 'description': description, 'completed': False, 'tags': tags})
    save(tasks)

def complete(tasks):
    id = get_id()
    for task in tasks:
        if task['id'] == id:
            task['completed'] = True
    save(tasks)

def save(tasks):
    with open(task_file, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=2)

def delete(tasks):
    id = get_id()
    tasks[:] = [task for task in tasks if task["id"] != id]
    save(tasks)

def get_id():
    try:
        id = int(input('Введите id задачи: '))
        return id
    except ValueError:
        print('Вы ввели некорректное значение')

def get_tags():
    raw = input('Введите теги через запятую: ')
    tags = re.split(r'\s*,\s*', raw.strip())
    return tags

def get_status(task):
    status = "✅" if task["completed"] else "❌"
    return status

def search_task(tasks):
    tags = get_tags()
    print('\n===================')
    for task in tasks:
        status = get_status(task)
        if any(tag in task["tags"] for tag in tags):
            print(f"{task['id']}. {task['title']} {status}")
    print('===================')

def main():
    tasks = load()
    while True:
        print('\n1. Показать все задачи. \n2. Показать конкретную задачу. \n3. Добавить задачу. \n4. Завершить задачу. \n5. Удалить задачу. \n6. Поиск по тегам. \n7. Закончить сессию.')
        a = input('\nВыберите действие: ')
        if a == '1':
            read(tasks)
        elif a == '2':
            read_id(tasks)
        elif a == '3':
            add(tasks)
        elif a == '4':
            complete(tasks)
        elif a == '5':
            delete(tasks)
        elif a == '6':
            search_task(tasks)
        elif a == '7':
            break
        else:
            print('Неверный выбор.')

if __name__ == "__main__":
    main()