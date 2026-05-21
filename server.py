import socket
import threading

HOST = '0.0.0.0'
PORT = 5555

clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()

print("Server started...")


def handle_client(client):

    while True:

        try:
            message = client.recv(4096)

            for c in clients:

                if c != client:
                    c.send(message)

        except:

            clients.remove(client)
            client.close()
            break


def receive():

    while True:

        client, address = server.accept()

        print(f"Connected with {address}")

        clients.append(client)

        thread = threading.Thread(
            target=handle_client,
            args=(client,)
        )

        thread.start()


receive()
