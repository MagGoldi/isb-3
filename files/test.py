import json  
import argparse 
import os  
import wget 
from prettytable import PrettyTable  


settings = {
	'initial_file': 'file.txt',  # путь к исходному файлу
	'encrypted_file': 'encrypted_file.txt',  # путь к зашифрованному файлу
	'decrypted_file': 'decrypted_file.txt',  # путь к расшифрованному файлу
	'symmetric_key': 'symmetric_key.txt',  # путь к симметричному ключу
	'public_key': 'public_key.pem',  # путь к открытому ключу
	'secret_key': 'secret_key.pem',  # путь к закрытому ключу
	'vec_init': 'iv.txt'
}
# gen  = Запускает режим генерации ключей
# enc  = Запускает режим шифрования
# dec  = Запускает режим дешифрования

parser = argparse.ArgumentParser()
parser.add_argument('mode', help='Режим работы')
args = parser.parse_args()

def print_info(text):
	print('\n')
	table = PrettyTable()
	table.field_names = ['Info']
	table.add_row([text])
	print(table)
	print('\n')
	pass

def gen():
	pass
def enc():
	pass
def enc():
	pass

def main():
	while True:
		if args.mode == "gen":
			print_info('Запущен режим создания ключей')

		elif args.mode == "enc":
			print_info('Запущен режим шифрования')

		elif args.mode == "dec":
			print_info('Запущен режим дешифрования')