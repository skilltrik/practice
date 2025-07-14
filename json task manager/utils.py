from typing import Literal, Union

# Функция получает на вход словарь со значениями, а также уточнение, какое количество информации нужно получить из словаря
def info(task: dict, type: Literal['short', 'full'], status: str):
    if type == 'short':
        print(f"{task['id']}. {task['title']} {status}")
    else:
        print(f"{task['title']}. {status}\n{task['description']}. \n{task['tags']}")

# Просиходит проверка на пустую строку, в зависимости от типа данных, которые получила функция
def check_fields(task: Union[str, list]):
    if isinstance(task, str):
        task = task.strip()
        if task == '':
            task = '---'
        return task
    else:
        if task == ['']:
            task = ['---']
            return task
        else:
            # Чтобы теги не повторялись
            return set(task)