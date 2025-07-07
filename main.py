import json
import os

task_file = 'tasks.json'

def load():
    if not os.path.exists(task_file):
        return 'у вас пока нету файла с задачами'
    with open(task_file, 'r', encoding='utf-8') as file:
        return json.load(file)

def read(tasks):
    print('\n===================')
    for task in tasks:
        status = "✅" if task["completed"] else "❌"
        print(f'{task['id']}. {task['title']} {status}')
    print('===================')

def read_id(tasks, id):
    print('\n===================')
    for task in tasks:
        status = "✅" if task["completed"] else "❌"
        if task["id"] == id:
            print(f'{task['title']}. {status}\n{task['description']}. ')
    print('===================')

def add(tasks):
    title = input('Введите название: ')
    id  = max([task["id"] for task in tasks], default=0) + 1
    description = input('Введите описание: ')
    tags = input('Введите теги через запятую: ').split(',')
    tasks.append({'id': id, 'title': title, 'description': description, 'completed': False, 'tags': tags})

def complete(tasks, id):
    for task in tasks:
        if task['id'] == id:
            task['completed'] = True

def save(tasks):
    with open(task_file, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=2)

def delete(tasks, id):
    flag = False
    for i,task in enumerate(tasks):
        if task['id'] == id:
            del tasks[i]
            flag = True
        if flag:
            task['id'] -= 1

def main():
    tasks = load()
    while True:
        print('\n1. Показать все задачи. \n2. Показать конкретную задачу. \n3. Добавить задачу. \n4. Завершить задачу. \n5. Удалить задачу. \n6. Закончить сессию.')
        a = input('\nВыберите действие: ')
        if a == '1':
            read(tasks)
        elif a == '2':
            id = int(input('Введите номер задачи: '))
            read_id(tasks, id)
        elif a == '3':
            add(tasks)
        elif a == '4':
            id = int(input('Введите номер задачи: '))
            complete(tasks, id)
        elif a == '5':
            id = int(input('Введите номер задачи: '))
            delete(tasks, id)
        elif a == '6':
            break
        else:
            print('Неверный выбор.')
    save(tasks)

if __name__ == "__main__":
    main()