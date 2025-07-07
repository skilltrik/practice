import storage
import re
import utils

def read(data_tasks: list):
    for task in data_tasks:
        utils.info(task, 'short', get_status(task))

def read_id(data_tasks: list):
    task_id = get_id()
    for task in data_tasks:
        if task["id"] == task_id:
            utils.info(task, 'full', get_status(task))

def add(data_tasks: list):
    task_id  = max([task["id"] for task in data_tasks], default=0) + 1
    title = utils.check_fields(input('Введите название: '))
    description = utils.check_fields(input('Введите описание: '))
    tags = get_tags()
    task = {
        'id': task_id,
        'title':title,
        'description':description,
        'completed': False,
        'tags': tags
    }
    data_tasks.append(task)
    storage.save(data_tasks)

def complete(data_tasks: list):
    task_id = get_id()
    for task in data_tasks:
        if task['id'] == task_id:
            task['completed'] = True
    storage.save(data_tasks)

def delete(data_tasks: list):
    task_id = get_id()
    data_tasks[:] = [task for task in data_tasks if task["id"] != task_id]
    storage.save(data_tasks)

def search_task(data_tasks: list):
    tags = get_tags()
    for task in data_tasks:
        if any(tag in task["tags"] for tag in tags):
            utils.info(task, 'short', get_status(task))

def get_id():
    while True:
        try:
            task_id = int(input('Введите id задачи: '))
            return task_id
        except ValueError:
            print('Вы ввели некорректное значение')

def get_tags():
    raw = input('Введите теги через запятую: ')
    raw_tags = re.split(r'\s*,\s*', raw.strip())
    tags = utils.check_fields(raw_tags)
    return list(tags)

def get_status(task: dict):
    status = "✅" if task["completed"] else "❌"
    return status