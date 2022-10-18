def Interface(i:str):
    match i:
        case "Welcome":
            print('='*50)
            print('Добро пожаловать в наш телефонный справочник')
        
        case "Menu":
            print('='*50)
            print('Варианты работы программы')
            print('-'*50)
            print('1. Создание и изменение данных')
            print('2. Чтение данных')
            print('3. Импорт данных')
            print('4. Выход из программы')
        
        case "Export":
            print('='*50)
            print('Варианты работы программы')
            print('-'*50)
            print('1. Вывод всех данных')
            print('2. Вывод информации о контакте по указанным фамилии и имени')
            print('3. Выход из программы')
        
        case "Mistake":
            print('-'*50)
            print('------ Ошибка -------')
            print('-'*50)
        
        case "Contact_action":
            print('='*50)
            print('Варианты работы программы')
            print('-'*50)
            print('1. Создать контакт')
            print('2. Удалить контакт')
            print('3. Выход из программы')
                
        case "End":
            print('='*50)
            print('Выберите дальнейшее действие')
            print('-'*50)
            print('1. Выход в главное меню')
            print('2. Выход из программы')