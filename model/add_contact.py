


def input_data():
	while True:
		name = input('Введите имя: ')
		if not len(name) < 3 and not name.isspace():
			print('поле "имя" должно быть больше 3 букв и не пустым')
			break
	while True:
		surname = input('Введите фамилию: ')
		if not len(surname) < 3 and not surname.isspace():
			print('поле "фамилия" должно быть больше 3 букв и не пустым')
			break
	while True:
		phone = input('Введите номер телефона: ')
		if phone.isnumeric() and not surname.isspace():
			print('поле "телефон" должно быть из цифр и не пустым')
			break
	return [name, surname, phone]


def create_contact():
	ls = input_data()
	return ls
