# hash_cracker.py
# NILEX Hash Cracker (Educational / Lab Use Only)

import os

def john_crack():
    hash_file = input("Path to hash file: ").strip()
    wordlist = input("Path to wordlist: ").strip()

    if not os.path.exists(hash_file) or not os.path.exists(wordlist):
        print("File not found.")
        return

    cmd = f"john --wordlist={wordlist} {hash_file}"
    os.system(cmd)

    print("\n[+] Cracked passwords:")
    os.system(f"john --show {hash_file}")


def hashcat_crack():
    hash_file = input("Path to hash file: ").strip()
    wordlist = input("Path to wordlist: ").strip()
    hash_mode = input("Hash mode (example: 0=MD5, 1000=NTLM): ").strip()

    if not os.path.exists(hash_file) or not os.path.exists(wordlist):
        print("File not found.")
        return

    cmd = f"hashcat -m {hash_mode} {hash_file} {wordlist} --force"
    os.system(cmd)


def hydra_attack():
    print("\n⚠️ LAB USE ONLY (DVWA / Metasploitable / HTB)")
    service = input("Service (ssh/ftp/http-post-form): ").strip()
    target = input("Target IP or domain: ").strip()
    user = input("Username: ").strip()
    wordlist = input("Password wordlist path: ").strip()

    if not os.path.exists(wordlist):
        print("Wordlist not found.")
        return

    cmd = f"hydra -l {user} -P {wordlist} {target} {service}"
    os.system(cmd)


def hash_cracker_menu():
    while True:
        print("\n--- Hash Cracker ---")
        print("1. John the Ripper (Offline)")
        print("2. Hashcat (Offline)")
        print("3. Hydra (Online – LAB ONLY)")
        print("4. Back")

        choice = input("Choose: ")

        if choice == "1":
            john_crack()
        elif choice == "2":
            hashcat_crack()
        elif choice == "3":
            hydra_attack()
        elif choice == "4":
            break
        else:
            print("Invalid choice")
