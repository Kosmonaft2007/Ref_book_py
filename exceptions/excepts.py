import os
import sys


def read_file_except(file_path):
	if not os.path.exists(file_path):
		print(f'файл не найден или некорректно указан путь: {file_path}')
		sys.exit()


def digit():
	while(True):
		i = input("Введите выбранный пункт: ")
		if i.isdigit(): return float(i)
		print("Вам надо ввести число")



