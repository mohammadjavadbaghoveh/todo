from datetime import datetime
import json
import os
tasks = []
STATES = dict(
    pending=' ',
    done= ' ',
    caneled=' ',
    postpond=' ',
)

def save():
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)

def add(text):
    tasks.append(dict(
        text=text or input('task: ') or 'untitled task',
        state='pending',
        date=datetime.now().date().isoformat(),
    ))
    save()

def edit():
    print('edit')

def postpone():
    print('delay/postpone')

def mark():
    print('mark')

def flag():
    print('flag')

def load():
    global tasks
    try:
        with open('tasks.json', 'w') as f:
            tasks = json.load(f)
    except:
        pass

def show():
    os.system('cls||clear')
    print('show')
    for task in tasks:
        print(
        '',
        STATES[task['state']],
        task ['text']
    )
def help():
    print('help')

def menu():
    while True:
        show()
        cmd, args = [*input('> ').split(' ', 1),''][:2]
        arg = args if args else ''
        match cmd:
            case 'a':
                add(arg)
            case 'e':
                edit()
            case 'p':
                postpone()
            case 'c':
                mark()
            case 'd':
                mark()
            case 'f':
                flag()
            case 'l':
                load()
            case 'r':
                show()
            case 's':
                save()
            case 'h':
                help()
            case 'x':
                exit()
            case _:
                print('Invalid command!')

if __name__ == '__main__':
    load()
    menu()
