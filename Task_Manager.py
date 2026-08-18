import json
import os


def load():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            return json.load(file)
    return []
def add(tasks):
    am = input('Введите задачу: ')
    tasks.append(am)
    save(tasks)
    print('Задача добавлена и сохранена!')
def save(tasks):
        with open('tasks.json','w',encoding='utf-8') as file:
            json.dump(tasks,file,indent = 4, ensure_ascii=False)
def delete(tasks):
    print(tasks)
    try:
        pop = int(input('Укажите индекс строки которую вы хотите удалить(начинается с 0)\n'))
    except ValueError:
        print('Введите только цифры')
        return
    if pop < 0 or pop > len(tasks):
        print('Вы ввели неправильный индекс строки')
    else:
        tasks.pop(pop)
        save(tasks)
        print('Вы успешно удалили строку')
def see(tasks):
    print(tasks)



tasks = load()
print('Выберите опцию: \n 1. Добавить команду \n 2. Удалить команду\n 3. Просмотреть все задачи \n 4. Выйти')
while True:
    choose = input()
    if choose == '1':
        add(tasks)
    elif choose == '2':
        delete(tasks)
    elif choose == '3':
        see(tasks)
    elif choose =='4':
        break
    else:
        print('Введите только доступную команду')
        