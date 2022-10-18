import csv
import exceptions.excepts as ex

def read_data(path):
	'''
	Функция, читает данные из файла в список
	'''
	ex.read_file_except(path)
	with open(path, "r") as file:
		reader = csv.reader(file)
		data_list = []
		for row in reader:
			data_list.append(row)
		return data_list
			

def show_all_contacts(path):
	'''
	Функция, выводит все контакты из указанного .csv файла.
	'''
	list_contact = read_data(path)
	
	print('''\t фамилия || имя || телефон''')
	print('\t', '=' * 25)
	for person in list_contact:
		print(f'\t {person[1]} || {person[0]} || {person[2]}')
	print('\t', '=' * 25)



def show_selected_contact(path):
	'''
	Функция, выводит информацию о контакте по указанным фамилии и имени
	'''
	
	list_contact = read_data(path)
	
	while True:
		name = input('Введите имя контакта: ')
		if not len(surname) < 3 and not surname.isspace():
			print('поле имя должно быть больше 3 букв и не пустым')
			break
	while True:
		surname = input('Введите фамилию контакта: ')
		if not len(name) < 3 and not name.isspace():
			print('поле фамилия должно быть больше 3 букв и не пустым')
			break
	
	for contact in list_contact:
		if name == contact[0] and surname == contact[1] in contact:
			index = list_contact.index(contact)
			print(index)
			return list_contact[index]
	print('Контакт : {} {} не найден.'.format(surname, name))

