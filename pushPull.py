import os 
from datetime import datetime

now = datetime.now()   
dt_string = now.strftime("%d/%m/%Y-%H:%M:%S")

def push():
    os.system('git add -f work_folder')
    os.system(f"git commit -m {dt_string}")
    os.system('git push')
    print('push done')
def pull():
    os.system('git pull')
    print('pull done')
def status():
    os.system('git status')
    print('status done')
def log():
    os.system('git log')
    print('log done')
def branch():
    os.system('git branch')
    print('branch done')

