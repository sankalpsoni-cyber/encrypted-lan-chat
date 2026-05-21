from crypto_utils import *

key = b'12345678901234567890123456789012'

while True:

    print("\n1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":

        message = input("Enter message: ")

        nonce, tag, ciphertext = encrypt_message(
            message,
            key
        )

        print("\n=== SEND THIS TO FRIEND ===")
        print("NONCE:", nonce)
        print("TAG:", tag)
        print("CIPHERTEXT:", ciphertext)

    elif choice == "2":

        nonce = input("Enter NONCE: ")
        tag = input("Enter TAG: ")
        ciphertext = input("Enter CIPHERTEXT: ")

        try:

            plaintext = decrypt_message(
                nonce,
                tag,
                ciphertext,
                key
            )

            print("\nDecrypted Message:", plaintext)

        except Exception as e:

            print("Decryption Failed:", e)

    elif choice == "3":
        break