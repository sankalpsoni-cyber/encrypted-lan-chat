import socket
import threading
import pickle

from crypto_utils import *

HOST = '10.156.18.11'
PORT = 5555

KEY = b'12345678901234567890123456789012'


def mode_menu():

    print("\n====== E2E CHAT SYSTEM ======")
    print("1. Real-Time Chat")
    print("2. Manual Encrypt/Decrypt")
    print("3. Exit")

    return input("Choose Mode: ")


def realtime_chat():

    client = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    client.connect((HOST, PORT))

    print("\nConnected to secure chat.")

    def receive():

        while True:

            try:

                data = client.recv(4096)

                nonce, tag, ciphertext = pickle.loads(
                    data
                )

                message = decrypt_message(
                    nonce,
                    tag,
                    ciphertext,
                    KEY
                )

                print(f"\nFriend: {message}")

            except Exception as e:

                print("Receive Error:", e)
                client.close()
                break

    def write():

        while True:

            message = input("You: ")

            nonce, tag, ciphertext = encrypt_message(
                message,
                KEY
            )

            data = pickle.dumps(
                (nonce, tag, ciphertext)
            )

            print("\nEncrypted:", ciphertext)

            client.send(data)

    receive_thread = threading.Thread(
        target=receive
    )

    receive_thread.start()

    write_thread = threading.Thread(
        target=write
    )

    write_thread.start()


def manual_mode():

    while True:

        print("\n===== MANUAL MODE =====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Back")

        choice = input("Choose: ")

        if choice == "1":

            message = input("Enter Message: ")

            nonce, tag, ciphertext = encrypt_message(
                message,
                KEY
            )

            print("\n=== SEND THIS ===")
            print("NONCE:", nonce)
            print("TAG:", tag)
            print("CIPHERTEXT:", ciphertext)

        elif choice == "2":

            nonce = input("NONCE: ")
            tag = input("TAG: ")
            ciphertext = input("CIPHERTEXT: ")

            try:

                plaintext = decrypt_message(
                    nonce,
                    tag,
                    ciphertext,
                    KEY
                )

                print("\nDecrypted:", plaintext)

            except Exception as e:

                print("Decryption Failed:", e)

        elif choice == "3":
            break


while True:

    mode = mode_menu()

    if mode == "1":
        realtime_chat()

    elif mode == "2":
        manual_mode()

    elif mode == "3":
        break