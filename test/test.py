'''
this is a argprase function snippet to add later 
'''
# import argparse
# parser = argparse.ArgumentParser(description='encrypt or decrypt a folder and push or pull from gitlab')
# parser.add_argument('-d', '--decrypt', action='store_true', help="decrypt working folder and files")
# parser.add_argument('-e', '--encrypt', action='store_true', help="encrypt working folder and files")
# parser.add_argument('-p', '--passphrase', help="passphrase to use for encryption and decryption")
# parser.add_argument('-push','--push', action='store_true', help="push gitlab repo")
# parser.add_argument('-pull','--pull', action='store_true', help="pull gitlab repo")
# args = parser.parse_args()
# if args.decrypt:
#     print("decrypt")
# elif args.encrypt:
#     print('encrypt')
# elif args.passphrase:
#     print('passphrase')
# elif args.push:
#     print('push')
# elif args.pull:
#     print('pull')
# else:
#     print('no arguments')
#     parser.print_help()
#     exit(1)
# ---------------------------------------------------------
# this script will get the files in the working folder and encrypt them
import os 
path = os.getcwd()
# current_dir = os.getcwd().replace('\\','/')
## print files in folder and subfolders 
folders = [x[0] for x in os.walk(path)]
for i in folders:
    files = [ f.path for f in os.scandir(i) if f.is_file() ]
    for x in files :
        x=x.replace('\\','/').replace('./','') 
        print(x)
#-------------------------------------------------------
# import os 
# os.mkdir("encrypted")




  


