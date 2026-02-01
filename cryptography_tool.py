# cryptography_tool.py
# Simple Cryptography Tool (Encrypt & Decrypt)
# Algorithm: Fernet (symmetric encryption)

from cryptography.fernet import Fernet


def generate_key():
    """Generate and save a secret key"""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as secret.key")


def load_key():
    """Load the secret key"""
    return open("secret.key", "rb").read()


def encrypt_message(message):
    key = load_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    return encrypted


def decrypt_message(encrypted_message):
    key = load_key()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_message).decode()
    return decrypted


def main():
    while True:
        print("\n=== Cryptography Tool ===")
        print("1. Generate Key")
        print("2. Encrypt Message")
        print("3. Decrypt Message")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            generate_key()

        elif choice == "2":
            message = input("Enter message to encrypt: ")
            encrypted = encrypt_message(message)
            print("Encrypted Message:", encrypted)

        elif choice == "3":
            encrypted = input("Enter encrypted message: ")
            try:
                decrypted = decrypt_message(encrypted.encode())
                print("Decrypted Message:", decrypted)
            except Exception:
                print("Invalid encrypted message or wrong key!")

        elif choice == "4":
            print("Exiting... 🔐")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
