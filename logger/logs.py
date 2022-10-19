from datetime import datetime as dt

# логирование ошибочного ввода данных пользователем
def input_logger(data):
    time = dt.now().strftime('%D  %H:%M')
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write(f'{data}, {time} \n')
