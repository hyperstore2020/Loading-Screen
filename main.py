# Does not have to be a for loop, could be any process. This was an example.
# Preview: https://i.imgur.com/Kz9kh9F.gif

import os
from colorama import init, Fore
clear = lambda: os.system('cls') # Change to 'clear' if not on Windows.
init()

do_stuff = 0
amount = int(input('Amount: '))

for x in range(amount):
  done = (((x + 1) / amount))
  do_stuff += 1 # Process will be quick.
  if done == 0.1:
    clear()
    print(f'{Fore.GREEN}■{Fore.WHITE}■■■■■■■■■ ' + str(int(done * 100)) + '%')
  elif done == 0.2:
    clear()
    print(f'{Fore.GREEN}■■{Fore.WHITE}■■■■■■■■ ' + str(int(done * 100)) + '%')
  elif done == 0.3:
    clear()
    print(f'{Fore.GREEN}■■■{Fore.WHITE}■■■■■■■ ' + str(int(done * 100)) + '%')
  elif done == 0.4:
    clear()
    print(f'{Fore.GREEN}■■■■{Fore.WHITE}■■■■■■ ' + str(int(done * 100)) + '%')
  elif done == 0.5:
    clear()
    print(f'{Fore.GREEN}■■■■■{Fore.WHITE}■■■■■ ' + str(int(done * 100)) + '%')
  elif done == 0.6:
    clear()
    print(f'{Fore.GREEN}■■■■■■{Fore.WHITE}■■■■ ' + str(int(done * 100)) + '%')
  elif done == 0.7:
    clear()
    print(f'{Fore.GREEN}■■■■■■■{Fore.WHITE}■■■ ' + str(int(done * 100)) + '%')
  elif done == 0.8:
    clear()
    print(f'{Fore.GREEN}■■■■■■■■{Fore.WHITE}■■ ' + str(int(done * 100)) + '%')
  elif done == 0.9:
    clear()
    print(f'{Fore.GREEN}■■■■■■■■■{Fore.WHITE}■ ' + str(int(done * 100)) + '%')
  elif done == 1.0:
    clear()
    print(f'{Fore.GREEN}■■■■■■■■■■ ' + str(int(done * 100)) + '%')
