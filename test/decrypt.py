#!/usr/bin/env python3
from cryptography.fernet import Fernet

from kdf import derive_key

passphrase = b"hunter2"
f = Fernet(derive_key(passphrase))
with open('encrypted.txt', 'rb') as file:
    encrypted = file.read()  # binary read

plaintext = f.decrypt(encrypted)  # binary output
# print(plaintext.decode())
encoded = plaintext.decode()
print(type(encoded))

with open('decrypt.txt', 'wb') as file:
    file.write(bytes(encoded,'utf-8'))  # binary write
    # file.write(plaintext.decode())
    