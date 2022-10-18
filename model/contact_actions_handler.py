import model.user_input as u_in
import model.export_contacts as exp
import model.import_contacts as imp_c

# создание контакта
def create_contact():
	ls = u_in.input_data()
	print('\t', '=' * 25)
	return ls
	

def delete_contact(path):
	list_contact = exp.read_data(path)
	print('Введите параметры удаления: ')
	name = u_in.check_input_string('Имя')
	surname = u_in.check_input_string('Фамилия')
	
	for person in list_contact:
		if name == person[0] and surname == person[1] in person:
			index = list_contact.index(person)
			list_contact.pop(index)
			print(f'Контакт {person[0]} {person[1]} успешно удалён.')
			imp_c.rewrite_csv(list_contact, path, 'w')
			return
	print('Контакт : {} {} не найден.'.format(surname, name)) 

