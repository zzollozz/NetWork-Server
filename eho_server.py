import socket
from datetime import datetime
from threading import Thread

host = '0.0.0.0'
port = 65432

separator_token = "<SEP>"   # чтобы разделить имя клиента и сообщение

client_sockets = set()

def listen_for_client(cs):

    while True:
        try:
            # продолжайте прослушивать сообщение из сокета `cs`
            msg = cs.recv(1024).decode()
        except Exception as e:
            # client no longer connected
            # remove it from the set
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)
        else:
            # если мы получили сообщение, замените <SEP>
            # token with ": " для красивой печати
            msg = msg.replace(separator_token, ": ")

        for client_socket in client_sockets:
            # и отправить сообщение
            client_socket.send(msg.encode())



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((host, port))
    s.listen()

    while True:
        client_socket, client_address = s.accept()
        print(f"[+] {client_address} connected.")

        client_sockets.add(client_socket)

        t = Thread(target=listen_for_client, args=(client_socket,))
        t.daemon = True
        t.start()






