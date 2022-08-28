# encrypt
#!/usr/bin/env python3
from pydoc import describe
from cryptography.fernet import Fernet
from kdf import derive_key
from datetime import datetime
import os

def encrypt (passphrase:bytes, file_name:str):
    '''
    encrypt a file with a passphrase and return encrypted byte type string
    use wb to write binary string to file
    for exmaple: 
    data = encrypt(passphrase, file_name)
        with open(file_name, 'wb') as file:
            file.write(data)  # binary write
    '''
    key = derive_key(passphrase, generate_salt=True)
    f = Fernet(key)
    with open(file_name, 'rb') as file:
        plaintext = file.read()  # binary read
    now = datetime.now()
    # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")  
    # massage= f"\nencrypted at {dt_string}"
    # plaintext += bytes(massage,'utf-8')
    return f.encrypt(plaintext)
    

def decrypt(passphrase:bytes, file_name:str):
    '''
    decrypt a file with a passphrase and return the byte type string
    use wb to write binary string to file
    for exmaple: 
    data = decrypt(passphrase, file_name)
        with open(file_name, 'wb') as file:
            file.write(data)  # binary write    
    '''
    f = Fernet(derive_key(passphrase))
    with open(file_name, 'rb') as file:
        encrypted = file.read()  # binary read
    # breakpoint()
    plaintext = f.decrypt(encrypted)  # binary output
    try :
        encoded = plaintext.decode('utf-8')
        return bytes(encoded,'utf-8')
    except:          
        encoded = plaintext.decode('latin-1')
        return bytes(encoded,'latin-1')  

def dir(path=f'{os.getcwd()}/work_folder'):
    '''
    this function take a path variable and return a list of files in the path
    if no path is given it will use the work_folder in the current directory
    '''
    folders = [x[0] for x in os.walk(path)]
    l_files = []
    for i in folders:
        files = [ f.path for f in os.scandir(i) if f.is_file() ]
        for x in files :
            x = x.replace('\\','/').replace('./','')
            l_files += [x]
    return l_files
            
            
            
            