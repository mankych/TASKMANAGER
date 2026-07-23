Exit = True
while Exit:
    file = open('Your tasks.txt', 'a')
    command = input( 'Enter command(add read or exit): ')
    if command.lower() == 'add':
    
        task = input('Enter a task: ')
        print(' You enter', task)
        file.write(task + '\n')
        file.close()
        
    elif command.lower() == 'read':
        try:
            file = open('Your tasks.txt','r')
            show = file.read()
            print(show)
            file.close()
        except FileNotFoundError:
            print('No tasks. Add one')
    elif command.lower() == 'exit':
        Exit = False
    else:
        print('Error enter only commands')
