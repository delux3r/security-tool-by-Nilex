# main.py
# NILEX Security Tools

from password_generator import generate_password
from password_strength_checker import check_password_strength
from port_scanner import scan_target
from file_integrity_checker import generate_file_hash, verify_file_integrity
from cryptography.fernet import Fernet
import os

# ----------------- Colors -----------------
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# ----------------- Utils -----------------
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ----------------- Cryptography -----------------
def load_key():
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        return None

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)
    print(f"{Colors.OKGREEN}Key generated and saved as secret.key{Colors.ENDC}")

def encrypt_message(message):
    key = load_key()
    if not key:
        print(f"{Colors.WARNING}Generate a key first!{Colors.ENDC}")
        return
    f = Fernet(key)
    print(f"{Colors.OKGREEN}Encrypted:{Colors.ENDC}",
          f.encrypt(message.encode()).decode())

def decrypt_message(message):
    key = load_key()
    if not key:
        print(f"{Colors.WARNING}Generate a key first!{Colors.ENDC}")
        return
    f = Fernet(key)
    try:
        print(f"{Colors.OKGREEN}Decrypted:{Colors.ENDC}",
              f.decrypt(message.encode()).decode())
    except Exception:
        print(f"{Colors.FAIL}Wrong key or invalid message!{Colors.ENDC}")

def cryptography_menu():
    while True:
        print(f"\n{Colors.OKCYAN}--- Cryptography Tool ---{Colors.ENDC}")
        print("1. Generate Key")
        print("2. Encrypt Message")
        print("3. Decrypt Message")
        print("4. Back")
        c = input("Choose: ")

        if c == "1":
            generate_key()
        elif c == "2":
            encrypt_message(input("Message: "))
        elif c == "3":
            decrypt_message(input("Encrypted: "))
        elif c == "4":
            break
        else:
            print("Invalid choice")

# ----------------- Password Menus -----------------
def password_generator_menu():
    try:
        length = int(input("Password length: "))
        print("Password:", generate_password(length))
    except:
        print("Invalid input")

def password_strength_menu():
    pwd = input("Password: ")
    print("Strength:", check_password_strength(pwd))

# ----------------- Port Scanner -----------------
def port_scanner_menu():
    target = input("Target IP / Domain: ")
    scan_target(target)

# ----------------- File Integrity -----------------
def file_integrity_menu():
    while True:
        print(f"\n{Colors.OKCYAN}--- File Integrity Checker ---{Colors.ENDC}")
        print("1. Generate File Hash")
        print("2. Verify File Integrity")
        print("3. Back")
        c = input("Choose: ")

        if c == "1":
            generate_file_hash()
        elif c == "2":
            verify_file_integrity()
        elif c == "3":
            break
        else:
            print("Invalid choice")

# ----------------- MAIN -----------------
def main():
    clear()
    print(f"{Colors.HEADER}{Colors.BOLD}")
    print("███▄    █  ██▓ ██▓    ▓█████  ▒██   ██▒")
    print(" ██ ▀█   █ ▓██▒▓██▒    ▓█   ▀  ▒▒ █ █ ▒░")
    print("▓██  ▀█ ██▒▒██▒▒██░    ▒███    ░░  █   ░")
    print("▓██▒  ▐▌██▒░██░▒██░    ▒▓█  ▄   ░ █ █ ▒ ")
    print("▒██░   ▓██░░██░░██████▒░▒████▒ ▒██▒ ▒██▒")
    print(f"{Colors.ENDC}")

    while True:
        print(f"\n{Colors.BOLD}=== NILEX Security Tools ==={Colors.ENDC}")
        print("1. Password Generator")
        print("2. Password Strength Checker")
        print("3. Cryptography Tool")
        print("4. Nmap Port Scanner")
        print("5. File Integrity Checker")
        print("6. Exit")

        choice = input("Select: ")

        if choice == "1":
            password_generator_menu()
        elif choice == "2":
            password_strength_menu()
        elif choice == "3":
            cryptography_menu()
        elif choice == "4":
            port_scanner_menu()
        elif choice == "5":
            file_integrity_menu()
        elif choice == "6":
            print("Bye 👋 Stay secure!")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
