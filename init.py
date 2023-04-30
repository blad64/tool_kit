import subprocess
import time

try:
    from colorama import init, Fore, Back, Style
    print("[+] La biblioteca está instalada")
except ModuleNotFoundError:
    subprocess.run(["pip", "install", "colorama"])
    from colorama import init, Fore, Back, Style

try:
    import git
    print("[+] La biblioteca está instalada")
except ModuleNotFoundError:
    subprocess.run(["pip", "install", "gitpython"])
    import git

try:
    import pyfiglet
    print("[+] La biblioteca está instalada")
except ModuleNotFoundError:
    subprocess.run(["pip", "install", "pyfiglet"])
    import pyfiglet

try:
    import os
    print("[+] La biblioteca está instalada")
except ModuleNotFoundError:
    subprocess.run(["pip", "install", "io"])
    import os

try:
    import webbrowser
    print("[+] La biblioteca está instalada")
except ModuleNotFoundError:
    subprocess.run(["pip", "install", "webbrowser"])
    import webbrowser


#fore reset
init(autoreset=True)

#url de clones
pyphisher = "https://github.com/KasRoudra/PyPhisher"


def program_main():

    #ui
    texto_ascii = pyfiglet.figlet_format("tool kit 1.0")
    print(Fore.RED  + Style.BRIGHT + texto_ascii)
    print(Fore.GREEN  + Style.BRIGHT + " ___________")
    print(Fore.GREEN  + Style.BRIGHT + "|           |")
    print(Fore.RED  + Style.BRIGHT +   "|  by blad  |")
    print(Fore.GREEN  + Style.BRIGHT + "|___________|")
    print(Fore.RESET)
    print(Fore.RED + Style.BRIGHT + "-------------")
    
    #selector
    print(Fore.RED + Style.BRIGHT + "[●]" + Style.NORMAL + Fore.YELLOW + " [1]-Pyphisher " + Fore.WHITE + "|"  + Fore.GREEN + " KasRoudra " + Fore.WHITE + "|" + Fore.CYAN + f" {pyphisher} " + Fore.RED + Style.BRIGHT + "[●]")
    print(Fore.RESET + Style.RESET_ALL)
    print(Fore.RED + Style.BRIGHT + "[●]" + Style.NORMAL + Fore.YELLOW + " [1]-Pyphisher " + Fore.WHITE + "|"  + Fore.GREEN + " KasRoudra " + Fore.WHITE + "|" + Fore.CYAN + f" {pyphisher} " + Fore.RED + Style.BRIGHT + "[●]")
    print(Fore.RESET + Style.RESET_ALL)
    print(Fore.RED + Style.BRIGHT + "[●]" + Style.NORMAL + Fore.YELLOW + " [1]-Pyphisher " + Fore.WHITE + "|"  + Fore.GREEN + " KasRoudra " + Fore.WHITE + "|" + Fore.CYAN + f" {pyphisher} " + Fore.RED + Style.BRIGHT + "[●]")
    print(Fore.RESET + Style.RESET_ALL)
    print(Fore.RED + Style.BRIGHT + "[●]" + Style.NORMAL + Fore.YELLOW + " [1]-Pyphisher " + Fore.WHITE + "|"  + Fore.GREEN + " KasRoudra " + Fore.WHITE + "|" + Fore.CYAN + f" {pyphisher} " + Fore.RED + Style.BRIGHT + "[●]")
    print(Fore.RESET + Style.RESET_ALL)
    

    #seleccion de tool
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "selecciona una herramienta")
    entrada = input(Fore.GREEN + "[@]:")

    if entrada == "1" or entrada == "01":
        op1()
    elif entrada == "2" or entrada == "02":
        op2()
    elif entrada == "3" or entrada == "03":
        op3()
    elif entrada == "4" or entrada == "04":
        op4()

        

def op1():
    try:
        print(Fore.YELLOW + "incializando...")
        time.sleep(0.2)
        subprocess.run(["python3", "PyPhisher/pyphisher.py"])
    except ModuleNotFoundError:
        subprocess.run(["git", "clone", "https://github.com/KasRoudra/PyPhisher"])
        print(Fore.YELLOW + "incializando...")
        time.sleep(0.2)
        subprocess.run(["python3", "PyPhisher/pyphisher.py"])
        
def op2():
    try:
        print(Fore.YELLOW + "incializando...")
        time.sleep(0.2)
        subprocess.run(["python3", "PyPhisher/pyphisher.py"])
    except ModuleNotFoundError:
        subprocess.run(["git", "clone", pyphisher])
        print(Fore.YELLOW + "incializando...")
        time.sleep(0.2)
        subprocess.run(["python3", "PyPhisher/pyphisher.py"])
        
def op3():
    try:
        print(Fore.YELLOW + "incializando...")
        time.sleep(0.2)
        subprocess.run(["python3", "PyPhisher/pyphisher.py"])
    except ModuleNotFoundError:
        subprocess.run(["git", "clone", pyphisher])
        print(Fore.YELLOW + "incializando...")
        time.sleep(0.2)
        subprocess.run(["python3", "PyPhisher/pyphisher.py"])
        
def op4():
    try:
        print(Fore.YELLOW + "incializando...")
        time.sleep(0.2)
        subprocess.run(["python3", "PyPhisher/pyphisher.py"])
    except ModuleNotFoundError:
        subprocess.run(["git", "clone", pyphisher])
        print(Fore.YELLOW + "incializando...")
        time.sleep(0.2)
        subprocess.run(["python3", "PyPhisher/pyphisher.py"])  
        

        
        

program_main()
        