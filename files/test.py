import json  
import argparse 
import os  
import wget 
from prettytable import PrettyTable  
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


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

def generation(symmetric_k, public_k, secret_k):
	print('Длина ключа от 32 до 448 бит с шагом 8 бит')
	key_len = int(input('Введите длину ключа: '))

	while True:
		if key_len % 8 != 0 or key_len < 32 or key_len > 448:
			key_len = int(input('Введите длину ключа: '))
		else: break

	# генерация пары ключей для асимметричного алгоритма шифрования
	keys = rsa.generate_private_key(
		public_exponent=65537,
		key_size=2048
	)
	secret_key = keys
	public_key = keys.public_key()

	# сериализация открытого ключа в файл
	with open(public_k, 'wb') as public_out:
		public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
												 format=serialization.PublicFormat.SubjectPublicKeyInfo))
	# сериализация закрытого ключа в файл
	with open(secret_k, 'wb') as secret_out:
		secret_out.write(secret_key.private_bytes(encoding=serialization.Encoding.PEM,
													format=serialization.PrivateFormat.TraditionalOpenSSL,
													encryption_algorithm=serialization.NoEncryption()))

	# открываем файл с симметричным ключом
	with open(symmetric_k, 'rb') as key_file:
		key = key_file  # забираем его содержимое в переменную key
	text = bytes(str(key), 'UTF-8')
	c_text = public_key.encrypt(text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

	# перезаписываем в файл с симметричным ключом зашифрованный симметричный ключ
	with open(symmetric_k, 'wb') as key_file:
		key_file.write(c_text)

	print(f'Ключи асимметричного шифрования сериализованы по адресу: {public_k}\t{secret_k}')
	print(f"Ключ симметричного шифрования:\t{symmetric_k}")
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
			with open('settings.json', 'r') as json_file:
				settings_data = json.load(json_file)
			generation(settings_data['symmetric_key'], settings_data['public_key'], settings_data['secret_key'])
			break

		elif args.mode == "enc":
			print_info('Запущен режим шифрования')
			if not os.path.exists('setting.json'):
				with open('setting.json', 'w') as file:
					json.dump(settings, file)
			with open('settings.json', 'r') as json_file:
				settings_data = json.load(json_file)	
			enc()
			break	

		elif args.mode == "dec":
			print_info('Запущен режим дешифрования')
			if not os.path.exists('setting.json'):
				with open('setting.json', 'w') as file:
					json.dump(settings, file)
			with open('settings.json', 'r') as json_file:
				settings_data = json.load(json_file)	
			dec()
			break
		else:
			print("че то не то...")	
			break
	pass


