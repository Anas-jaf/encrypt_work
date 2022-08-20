#!/usr/bin/env python3
#! python3
# -*- coding: utf-8 -*-
import argparse
import crypt_mod 
import pushPull
# TODO: add gitpython support
# TODO: add the ability to push and pull using python ssh library paramiko and to set up ssh config file 
# TODO: test the script 
# TODO: publish to github
# TODO: make this code better later 
# TODO: add work_folder to .gitignore file 
# TODO: move to the next task


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='encrypt or decrypt a folder and push or pull from gitlab')
    parser.add_argument('-d', '--decrypt', action='store_true', help="decrypt working folder and files")
    parser.add_argument('-e', '--encrypt', action='store_true', help="encrypt working folder and files")
    parser.add_argument('-p', '--passphrase', help="passphrase to use for encryption and decryption")
    parser.add_argument('-path', '--path', help="path to the working folder")
    parser.add_argument('-push','--push', action='store_true', help="push gitlab repo")
    parser.add_argument('-pull','--pull', action='store_true', help="pull gitlab repo")
    args = parser.parse_args()
    
    if args.passphrase is None:
        args.passphrase = input("enter password: ")
    psswd = bytes(args.passphrase , 'utf-8')
    path= args.path

    '''
    check if there is path and if there is path enter in loop and encrypt or decrypt the files 
    in the folder and subfolders and push or pull the files to gitlab
    '''
    if args.encrypt:
        '''
        encrypt then push to gitlab
        '''
        for i in crypt_mod.dir(path):
            data = crypt_mod.encrypt(psswd,i)
            with open(i, 'wb') as file:
                file.write(data)
        pushPull.push()
        
    elif args.decrypt:
        '''
        pull then decrypt
        '''
        pushPull.pull()
        for i in crypt_mod.dir(path):
            data = crypt_mod.decrypt(psswd,i)
            with open(i, 'wb') as file:
                file.write(data)
    else:
        print('no arguments')
        parser.print_help()
        exit(1)