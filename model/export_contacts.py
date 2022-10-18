import csv
import exceptions.excepts as ex
import model.user_input as u_in


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
	print('Введите параметры поиска: ')
	name = u_in.check_input_string('Имя')
	surname = u_in.check_input_string('Фамилия')
	
	for person in list_contact:
		if name == person[0] and surname == person[1] in person:
			index = list_contact.index(person)
			print(index)
			return list_contact[index]
	print('Контакт : {} {} не найден.'.format(surname, name))


