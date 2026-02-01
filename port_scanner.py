# port_scanner.py
# Simple Nmap Port Scanner

import subprocess

def scan_target(target):
    print("\n[+] Starting Nmap scan...")
    try:
        command = ["nmap", "-F", target]
        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )
        print(result.stdout)
    except FileNotFoundError:
        print("[-] Nmap is not installed!")
    except Exception as e:
        print("[-] Error:", e)
