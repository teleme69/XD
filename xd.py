import os,time
try:
  import requests
except ModuleNotFoundError:
  os.system("pip install requests")
  import requests


file_server = requests.get("https://raw.githubusercontent.com/Ahmed-XD/FILE/main/file_on.txt").text.strip()
random_server = requests.get("https://raw.githubusercontent.com/Ahmed-XD/FILE/main/random-on.txt").text.strip()
def intro():
  print('give star to our repo')
  os.system('git pull && clear')
  os.system('xdg-open https://github.com/Ahmed-XD/FILE')
  print('Join Our Facebook Group and support us')
  os.system('xdg-open https://m.facebook.com/groups/1247184652736578/')
  os.system('clear')
  
def install_part(file_name):
  os.system(f"curl -L https://github.com/Ahmed-XD/library/blob/main/{file_name}?raw=true -o {file_name}")

if os.path.exists("disable.so") and os.path.exists("x3.so") and os.path.exists("L.so"):
  os.remove("disable.so")
  os.remove("x3.so")
  os.remove("L.so")

intro()
install_part("disable.so")
install_part("x3.so")
install_part("L.so")
os.system("clear")



def run(file_server_text,random_server_text):
  print(f'[1] FILE CLONE [{server_text}]')
  print(f'[2] RANDOM CLONE [{server_text}]')
  choice = input('Choose : ')
  if int(choice) == 1:
    import disable
    if file_server_text == 'off':exit("File cloning tool is off")
    else:import x3
  else:
    import disable
    if random_server_text == 'off':exit("Random cloning tool is off")
    else:import L


run(file_server_text,random_server_text)
