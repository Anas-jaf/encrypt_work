#!/bin/bash

''' this is a script to rsync the files from the local machine to the remote machine using debian wsl'''
cd /mnt/d/programming/encrypt_work
rsync -avuzh kali@192.168.1.105:/opt/encrypt_work/work_folder/ work_folder/