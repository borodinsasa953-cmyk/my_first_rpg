master_password = input('Введите ключ доступа: ')
if master_password == 'sashadauN12.':
    print('Доступ разрешен')
    while True:
            state = 'main_menu'
            if state == 'main_menu':
                print('МЕНЕДЖЕР ПАРОЛЕЙ')
                print('----------------------')
                print('1. Добавить пароль')
                print('2. Просмотреть пароли')
                print('3.Выход')
                choice = input('Выберите действие: ')
                if choice == '1':
                    ps = input(' Введите социальную сеть, игру, и т.п. : ')
                    login = input('Введите логин: ')
                    password = input('Введите пароль: ')
                    with open('password.txt','a', encoding='utf-8') as file:
                        file.write(f'{ps}: Логин: {login}. Пароль: {password}, \n')
                    print('Пароль успешно добавлен!')
                elif choice == '2':
                    try:
                        with open('password.txt', 'r', encoding='utf-8') as file:
                            print(file.read())
                    except FileNotFoundError:
                        print('Паролей еще нет!')
                elif choice == '3':
                    print('Выход...')
                    break
                else:
                    print('Такого действия нет!')
else:
    print('Доступ запрещен.')
    
                
