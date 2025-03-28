import os
import time

txt_file = "requirements.txt"

if not os.path.exists(txt_file):
   print(f"Error: {txt_file} Not found!")
   exit()


with open(txt_file, "r") as file:
    packages = [line.strip() for line in file if line.strip()]


for package in packages:
   print(f"installing: {package}...")
   os.system(f'cmd /c "pip install {package}"')

time.sleep(1)


print("All packages installed! you can launch the 'balance Changer' .py file now! (PLEASE DO NOT TOUCH KEYBOARD OR MOUSE AT ALL!!)")

input("press Enter to exit...")