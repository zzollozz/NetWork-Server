import socket
from datetime import datetime

host = '127.0.0.1'
port = 65432


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Сервер запущен")
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        name_client = addr[0]
        print(f'Подключен клиент: {name_client}')
        while True:
            data = conn.recv(1024)
            message = str(data, 'utf-8')
            if not data:
                print(f"Соединение с клиентом {name_client} закрыто")
                break
            date = datetime.now().strftime("%H:%M:%S")
            print(f'Получено: от {name_client} в {date}\nсообщение:\n{repr(message)}')
            conn.sendall(bytes(f"Сервер получил сообщение {date} от {name_client}", 'utf-8'))



