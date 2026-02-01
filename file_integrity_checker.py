# file_integrity_checker.py
# File Integrity Checker using SHA256
# NILEX Security Tools

import hashlib
import os

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as f:
            for block in iter(lambda: f.read(4096), b""):
                sha256.update(block)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def generate_file_hash():
    file_path = input("Enter file path: ").strip()

    if not os.path.isfile(file_path):
        print("[-] File not found!")
        return

    file_hash = calculate_hash(file_path)
    hash_file = file_path + ".hash"

    with open(hash_file, "w") as f:
        f.write(file_hash)

    print("[+] Hash generated successfully!")
    print(f"[+] Hash: {file_hash}")
    print(f"[+] Saved to: {hash_file}")

def verify_file_integrity():
    file_path = input("Enter file path: ").strip()
    hash_file = file_path + ".hash"

    if not os.path.isfile(file_path) or not os.path.isfile(hash_file):
        print("[-] File or hash file not found!")
        return

    current_hash = calculate_hash(file_path)

    with open(hash_file, "r") as f:
        saved_hash = f.read().strip()

    if current_hash == saved_hash:
        print("[✓] File integrity OK (No changes detected)")
    else:
        print("[✗] WARNING! File has been modified!")
