import socket
from datetime import datetime


def client(host='127.0.0.1', port=65432,):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        message = input('Введите сообщение:\n>>>  ')
        s.connect((host, port))
        s.sendall(bytes(message, 'utf-8'))
        server_response = s.recv(1024)
        s_resp = str(server_response, 'utf-8')
        print(f'{datetime.now().strftime("%H:%M:%S:")}: ответ сервера: {repr(s_resp)}')


client()
