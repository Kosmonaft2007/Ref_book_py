import csv


def import_csv(data, path, rec_mode):
	with open(path, rec_mode, newline='') as file:
		writer = csv.writer(file)
		writer.writerow(data)

def rewrite_csv(data_list, path, rec_mode):
	with open(path, rec_mode, newline='') as file:
		for person in data_list:
			for text in person:
				if person.index(text) == (len(person) - 1):
					file.write(text)
					break
				file.write(text + ',')
			file.write('\n')