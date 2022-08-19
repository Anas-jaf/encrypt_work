# encrypt
#!/usr/bin/env python3
from cryptography.fernet import Fernet
from kdf import derive_key

def encrypt (passphrase:bytes, file_name:str):
    # passphrase = b"hunter2"
    # TODO: make it return the encrypted data
    key = derive_key(passphrase, generate_salt=True)
    f = Fernet(key)

    with open(file_name, 'rb') as file:
        plaintext = file.read()  # binary read
    plaintext += b"Hey new data!"
    breakpoint()
    # with open(file_name, 'wb') as file:
    #     file.write(f.encrypt(plaintext))  # binary write
    

def decrypt(passphrase:bytes, file_name:str):
    # passphrase = b"hunter2"
    f = Fernet(derive_key(passphrase))
    with open(file_name, 'rb') as file:
        encrypted = file.read()  # binary read

    plaintext = f.decrypt(encrypted)  # binary output
    encoded = plaintext.decode()
    print(type(encoded))
    breakpoint()
    # with open(file_name, 'wb') as file:
    #     file.write(bytes(encoded,'utf-8'))  # binary write
    #     # TODO: make it return the decrypted data
        
encrypt(b"hunter2", "D:/programming/encrypt_work/test/work_folder/folder1/sub_plain_file1.txt")        

    
    