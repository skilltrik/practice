import tasks, storage

def main():
    data_tasks = storage.load()
    while True:

        print('''
1. Показать все задачи.
2. Показать конкретную задачу.
3. Добавить задачу.
4. Завершить задачу.
5. Удалить задачу.
6. Поиск по тегам.
7. Закончить сессию.
''')
        a = input('Выберите действие: ')
        match a:
            case '1': tasks.read(data_tasks)
            case '2': tasks.read_id(data_tasks)
            case '3': tasks.add(data_tasks)
            case '4': tasks.complete(data_tasks)
            case '5': tasks.delete(data_tasks)
            case '6': tasks.search_task(data_tasks)
            case '7': break
            case _: print('Неверный выбор.')

if __name__ == "__main__":
    main()