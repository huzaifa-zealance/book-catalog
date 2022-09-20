'''
A auto execute program to configure 
python paths in a linux env and setup the 
web application server
'''

import subprocess
import os, sys

python_path = subprocess.check_output("which python3", shell=True).strip()
python_path = python_path.decode('utf-8')
print(python_path)


print("BOOK CATALOG : Please create a user for login")
cmd1_1 = f"{python_path} manage.py createsuperuser"
os.system(cmd1_1)

print("BOOK CATALOG : Configuring migratins")
cmd1_1 = f"{python_path} manage.py makemigrations"
os.system(cmd1_1)
cmd1_2 = f"{python_path} manage.py migrate"
os.system(cmd1_2)

print("BOOK CATALOG : Initiating the server")
cmd2 = f"{python_path} manage.py runserver localhost:8000"
os.system(cmd2)