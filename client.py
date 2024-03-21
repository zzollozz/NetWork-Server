import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back

# init colors
init()

# set the available colors
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]

# choose a random color for the client
client_color = random.choice(colors)


SERVER_HOST = "127.0.0.1"
SERVER_PORT = 65432
separator_token = "<SEP>"


def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"[*] Присоединенный к {SERVER_HOST}:{SERVER_PORT}...")
    s.connect((SERVER_HOST, SERVER_PORT))
    print("[+] Cоединенный.")

    # запросить у клиента имя
    name = input("Enter your name: ")




    t = Thread(target=listen_for_messages)
    t.daemon = True
    t.start()




    while True:
        # входное сообщение, которое мы хотим отправить на сервер
        to_send = input()
        # способ выхода из программы
        if to_send.lower() == 'q':
            print("Сессия закрыта")
            break
        # добавляем дату и время, имя и цвет отправителя
        date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        to_send = f"{client_color}[{date_now}] {name}{separator_token}{to_send}{Fore.RESET}"
        # отправка сообщение
        s.send(to_send.encode())

