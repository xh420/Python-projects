import time
import random
import os
import string
from colorama import init, Fore, Style
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.BLUE]
init()
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def animate_message(message, delay=0.06):
    built = ""
    for char in message:
        for _ in range(10): 
            clear()
            color = random.choice(colors)
            print(color + built)
        built += char
        clear()
        print(color + built)
        time.sleep(delay * 2)
def show_ascii_loop(ascii_lines, loop_delay=2, flicker_delay=0.1):
    charset = string.ascii_letters + string.punctuation + " "
    try:
        while True:
            for _ in range(1):
                clear()
                for line in ascii_lines:
                    color = random.choice(colors)
                    glitch = ''.join(random.choice(charset) if c != ' ' else ' ' for c in line)
                    print(glitch + color)
                time.sleep(flicker_delay)
            clear()
            for line in ascii_lines:
                print(line + color)
            time.sleep(loop_delay)

    except KeyboardInterrupt:
        print("\nAnimation stopped.")
animate_message("yeah everybody leaves.........")
animate_message("if they get the chance...... ")
animate_message("and this............... ")
animate_message("is my chance...")
time.sleep(1)
ascii_art = """                                  
     ████████████         ███████████      
   █████████████████   ████████████████ 
  ██████████████████████████████████████ 
  ██████████████████████████████████████
  ██████████████████████████████████████ 
   ████████████████████████████████████   
     ████████████████████████████████     
       ████████████████████████████       
          ███████████████████████          
             █████████████████              
               █████████████                 
                  ███████                  
""".strip("\n")
time.sleep(1)
show_ascii_loop(ascii_art.splitlines())
