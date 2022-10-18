'''
модуль будет переделан, вариант для тестерования
'''


import model.contact_actions_handler as cah
import model.import_contacts as imp
import model.export_contacts as exp


path = 'out.csv'

if __name__ == '__main__':
	
	while True:
		ls = cah.create_contact()
		print(ls)
		imp.import_csv(ls, path, 'a')
		print(exp.show_all_contacts(path))

	#print(exp.show_selected_contact(path))
	
	#print(cah.delete_contact(path))
	#print(exp.show_all_contacts(path))
