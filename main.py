'''
модуль будет переделан, вариант для тестерования
'''


import ctrl
import model.export_contacts as exp


path = 'out.csv'
# cah.delete_contact(path)
#exp.show_all_contacts(path)

if __name__ == '__main__':
	ctrl.main(path)
	
	# while True:
	# 	ls = cah.create_contact()
	# 	print(ls)
	# 	imp.import_csv(ls, path, 'a')
	# 	print(exp.show_all_contacts(path))
	# 	break

	#print(exp.show_selected_contact(path))
	
	#print(cah.delete_contact(path))
	#print(exp.show_all_contacts(path))
