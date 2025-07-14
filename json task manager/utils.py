from typing import Literal, Union

def info(task: dict, type: Literal['short', 'full'], status: str):
    if type == 'short':
        print(f"{task['id']}. {task['title']} {status}")
    else:
        print(f"{task['title']}. {status}\n{task['description']}. \n{task['tags']}")

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
            return set(task)