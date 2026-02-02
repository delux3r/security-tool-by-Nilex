# Security Tool by Nilex

Security Tool by Nilex is a comprehensive cybersecurity toolkit that includes various modules to help with password security, cryptography, network scanning, and file integrity verification.

Features
 ## 1. Password Strength Checker

Purpose: Evaluate the strength of passwords to ensure they are secure.

Description: A lightweight and effective tool to check password robustness and prevent weak passwords from being used.

## 2. Password Generator

Purpose: Generate secure passwords easily.

Description: Creates simple yet strong passwords to enhance account security.

## 3. Cryptography

Purpose: Encrypt sensitive information securely.

Description: Uses symmetric encryption methods such as Fernet to protect your data.

## 4. Hash Cracker

Purpose: Test password hashes for vulnerabilities.

Description: Supports cracking passwords using popular tools like Hashcat and John the Ripper.

## 5. Port Scanner

Purpose: Scan IP addresses and domains for open ports.

Description: Identify potential entry points on networks and services.

## 6. Subdomain Finder

Purpose: Discover hidden or unknown subdomains.

Description: Helps in reconnaissance by finding mystery domain names associated with a target.

## 7. File Integrity Checker

Purpose: Verify if files have been tampered with.

Description: Ensures the authenticity and integrity of important files.

Installation
`git clone https://github.com/delux3r/security-tool-nilex.git`

`cd security-tool-nilex`

`pip install -r requirements.txt`

Usage

Each module can be run independently:

## Check password strength

`python password_strength_checker.py`

## Generate a secure password

`python password_generator.py`

## Encrypt/Decrypt using Fernet

`python cryptography_tool.py`

## Scan ports

`python port_scanner.py`

## Find subdomains

`python subdomain_finder.py`

## Verify file integrity

`python file_integrity_checker.py`
## All in one use this command

`python main.py`

## License

This project is licensed under the MIT License.
