'''
модуль будет переделан, вариант для тестерования
'''


import model.add_contact as add
import model.import_contacts as imp
import model.export_contacts as exp


path = 'ou.csv'

if __name__ == '__main__':
	
	#ls = add.create_contact()
	#imp.import_csv(ls, path)
	
	print(exp.show_all_contacts(path))

	#print(exp.show_selected_contact(path))
	
	#print(exp.read_data(path))
