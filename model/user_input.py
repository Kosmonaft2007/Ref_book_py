import logs


# ввод данных пользователем
def input_data():
	name = check_input_string('имя')
	surname = check_input_string('фамилия')
	phone = check_input_digit('телефон')
	return [name, surname, phone]

# ввод данных и проверка строковых данных(оптимизация кода)
def check_input_string(desc: str):
	while True:
		val = input('Введите данные в поле "{}": '.format(desc))
		if len(val) < 3 or val.isspace() or not val.isalpha():
			print('поле "{}" должно быть больше 3 БУКВ и не пустым.'.format(desc))
			logs.input_logger('Пользователь ввел некорректные данные')
			continue
		return val

# ввод данных и проверка числовых данных(оптимизация кода)
def check_input_digit(desc: str):
	while True:
		val = input('Введите данные в поле "{}": '.format(desc))
		if not val.isdigit() or val.isspace():
			print('поле "{}" должно быть из ЦИФР и не пустым.'.format(desc))
			logs.input_logger('Пользователь ввел некорректные данные')
			continue
		return val
