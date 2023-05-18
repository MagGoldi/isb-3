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
def dec():
	pass

def main():
	while True:
		if args.mode == "gen":
			print_info('Запущен режим создания ключей')
			if not os.path.exists('setting.json'):
				with open('setting.json', 'w') as file:
					json.dump(settings, file)
			with open('settings.json', 'w') as json_file:
				settings_data = json.load(json_file)
			gen()
			break

		elif args.mode == "enc":
			print_info('Запущен режим шифрования')
			if not os.path.exists('setting.json'):
				with open('setting.json', 'w') as file:
					json.dump(settings, file)
			with open('settings.json', 'w') as json_file:
				settings_data = json.load(json_file)	
			enc()
			break	

		elif args.mode == "dec":
			print_info('Запущен режим дешифрования')
			if not os.path.exists('setting.json'):
				with open('setting.json', 'w') as file:
					json.dump(settings, file)
			with open('settings.json', 'w') as json_file:
				settings_data = json.load(json_file)	
			dec()
			break
		else:
			print("че то не то...")	
			break
	pass


