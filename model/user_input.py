
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
		if len(val) < 3 or val.isspace():
			print('поле "{}" должно быть больше 3 букв и не пустым.'.format(desc))
			continue
		return val

# ввод данных и проверка числовых данных(оптимизация кода)
def check_input_digit(desc: str):
	while True:
		val = input('Введите данные в поле "{}": '.format(desc))
		if not val.isnumeric() or val.isspace():
			print('поле "{}" должно быть из цифр и не пустым.'.format(desc))
			continue
		return val