import time
import random
import ctypes
from colorama import init, Fore, Style
ctypes.windll.kernel32.SetConsoleTitleW("Три в одном")
print(Fore.BLUE + Style.BRIGHT + '''
██████╗░██╗░░░██╗  ██████╗░███╗░░░███╗██╗████████╗██████╗░░█████╗░
██╔══██╗╚██╗░██╔╝  ██╔══██╗████╗░████║██║╚══██╔══╝██╔══██╗██╔══██╗
██████╦╝░╚████╔╝░  ██║░░██║██╔████╔██║██║░░░██║░░░██████╔╝██║░░██║
██╔══██╗░░╚██╔╝░░  ██║░░██║██║╚██╔╝██║██║░░░██║░░░██╔══██╗██║░░██║
██████╦╝░░░██║░░░  ██████╔╝██║░╚═╝░██║██║░░░██║░░░██║░░██║╚█████╔╝
╚═════╝░░░░╚═╝░░░  ╚═════╝░╚═╝░░░░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░''')
print(Style.RESET_ALL)
def spaces(kolvo: int):
	for x in range(kolvo):
		print()
kolvo = 1
user_name = str(input(Fore.RED + "Введите ваше имя: "))
while True:
	if kolvo == 1:
		pass
	elif kolvo == 2:
		spaces(3)
	print(Fore.GREEN + f"Здравствуй {user_name}! Я могу для тебя быть калькулятором, игрой в Камень, Ножницы, Бумага, и я могу быть для тебя печенькой с предсказанием)")
	choice = str(input(Fore.YELLOW + "1 - Калькулятор\n2 - Камень,Ножницы,Бумага\n3 - Печенье с предсказанием\n4 - Выйти из приложения\nВведите ваш выбор: "))
	if choice == "1":
		kalvulator = 1
		while True:
			if kalvulator == 1:
				kalvulator = 2
			elif kalvulator == 2:
				spaces(3)
			kolvo = 2
			print(Fore.RED + "Чтобы выйти, пропишите exit")
			primer = input(Fore.YELLOW + "Введите пример: ")
			if primer == "exit" or "quit":
				break
			print(Fore.RED + f"Результат: {eval(primer)}")
			try:
				pass
			except:
				raise Exception("ERROR")
	elif choice == "2":
		print(Fore.BLACK + "Чтобы выйти, пропишите exit")
		count_player = 0
		count_bot = 0
		kamen = 1
		def win():
			global count_player
			print()
			count_player += 1
			print(Fore.YELLOW + f"Счёт: {count_player}:{count_bot}")
		def proig():
			global count_bot
			print()
			count_bot += 1
			print(Fore.YELLOW + f"Счёт: {count_player}:{count_bot}")
		while True:
			if kamen == 1:
				kamen = 2
			elif kamen == 2:
				spaces(3)
			print(Fore.BLACK + "P.S. Чтобы ход удался, напишите название хода ровно так, как написанно в примере")
			spaces(1)
			player_hod = str(input(Fore.GREEN + "Вы можете походить только тремя ходами:\nКамень\nНожницы\nБумага\n Введите ваш выбор: "))
			bot_hod = random.choice(["Камень", "Ножницы", "Бумага"])
			def choices():
				global player_hod
				global bot_hod
				print(Fore.YELLOW + f"Ваш ход: {player_hod}\nХод компьютера: {bot_hod}")
			if player_hod == "Камень" and bot_hod == "Камень":
				print(Fore.BLACK + "Ничья")
				choices()
				continue
			elif player_hod == "Ножницы" and bot_hod == "Камень":
				print(Fore.RED + "Вы проиграли")
				choices()
				proig()
				continue
			elif player_hod == "Бумага" and bot_hod == "Камень":
				print(Fore.GREEN + "Вы выйграли")
				choices()
				win()
				continue
			elif player_hod == "Камень" and bot_hod == "Ножницы":
				print(Fore.GREEN + "Вы выйграли")
				choices()
				win()
				continue
			elif player_hod == "Ножницы" and bot_hod == "Ножницы":
				print(Fore.BLACK + "Ничья")
				choices()
				continue
			elif player_hod == "Камень" and bot_hod == "Бумага":
				print(Fore.BLACK + "Вы проиграли")
				choices()
				proig()
				continue
			elif player_hod == "Ножницы" and bot_hod == "Бумага":
				print(Fore.GREEN + "Вы выйграли")
				choices()
				win()
				continue
			elif player_hod == "Бумага" and bot_hod == "Бумага":
				print(Fore.BLACK + "Ничья")
				choices()
				continue
			elif player_hod == "exit":
				break
	elif choice == "3":
		off = False
		cook = 1
		while not off:
			if cook == 1:
				cook = 2
			elif cook == 2:
				spaces(3)
			with open('predz.txt') as f:
				values = f.read().splitlines()
			answer = random.choice(values)
			print(Fore.YELLOW + "Хммм....")
			time.sleep(1.8)
			print(Fore.YELLOW + "Думаю....")
			time.sleep(1.6)
			print(Fore.RED + answer)
			spaces(2)
			on = False
			while not on:
				ask = str(input(Fore.MAGENTA + "Вы хотите продолжить? \ny/n\n"))
				if ask == "y":
					on = True
					continue
				elif ask == "n":
					off = True
					break
				else:
					print("Неккоректный выбор")
					
	elif choice == "4":
		break
