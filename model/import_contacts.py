import csv


def import_csv(data, path):
	with open(path, 'a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(data)

