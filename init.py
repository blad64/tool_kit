import subprocess
import time
from subprocess import call

try:
    from colorama import init, Fore, Back, Style
    print("[+] La biblioteca está instalada")
except ModuleNotFoundError:
    print("[+] Instalando bibloteca...")
    subprocess.run(["sudo", "pip", "install", "colorama"])
    from colorama import init, Fore, Back, Style

try:
    import git
    print("[+] La biblioteca está instalada")
except ModuleNotFoundError:
    print("[+] Instalando bibloteca...")
    subprocess.run(["sudo", "pip", "install", "gitpython"])
    import git

try:
    import pyfiglet
    print("[+] La biblioteca está instalada")
except ModuleNotFoundError:
    print("[+] Instalando bibloteca...")
    subprocess.run(["sudo", "pip", "install", "pyfiglet"])
    import pyfiglet

try:
    import os
    print("[+] La biblioteca está instalada")
except ModuleNotFoundError:
    print("[+] Instalando bibloteca...")
    subprocess.run(["sudo", "pip", "install", "io"])
    import os
try:
    from IPython.display import clear_output
    print("[+] La biblioteca está instalada")
except ModuleNotFoundError:
    print("[+] Instalando bibloteca...")
    subprocess.run(["sudo", "pip", "install", "IPython"])
    from IPython.display import clear_output


#fore reset
init(autoreset=True)

#url de clones

#pyphisher 1
pyphisher = "https://github.com/KasRoudra/PyPhisher"
pyphisher_ruta = "PyPhisher/pyphisher.py"
pyphisher_folder = pyphisher

#darksms 2
setsms = "https://github.com/Darkmux/DarkSMS"
setsms_ruta = "DarkSMS/darksms.sh"
setsms_folder = "DarkSMS"

#zphisher
zphisher = "https://github.com/htr-tech/zphisher"
zphisher_ruta = "zphisher/zphisher.sh"
zphisher_folder = "zphisher"

#smssend
sms_send = "https://github.com/blad64/sms-send"
sms_send_ruta = "sms-send/main.py"
sms_send_folder = "sms-send"

def program_main():
    i = 0
    while i == 0:
        #ui
        name = "blad"
        texto_ascii = pyfiglet.figlet_format("tool kit 1.1")
        print(Fore.RED  + Style.BRIGHT + texto_ascii)
        print(Fore.GREEN  + Style.BRIGHT + " ___________")
        print(Fore.GREEN  + Style.BRIGHT + "|           |")
        print(Fore.RED  + Style.BRIGHT +   f"|  by {name}  |")
        print(Fore.GREEN  + Style.BRIGHT + "|___________|")
        print(Fore.RED + Style.BRIGHT + "-------------")
        
        #selector
        print(Fore.RED + Style.BRIGHT + "[●]" + Style.NORMAL + Fore.YELLOW + " [1]-Pyphisher " + Fore.WHITE + "|"  + Fore.GREEN + " KasRoudra " + Fore.WHITE + "|" + Fore.CYAN + f" {pyphisher} " + Fore.RED + Style.BRIGHT + "[●]")
        print(Fore.RESET + Style.RESET_ALL)
        print(Fore.RED + Style.BRIGHT + "[●]" + Style.NORMAL + Fore.YELLOW + " [2]-SetSMS " + Fore.WHITE + "|"  + Fore.GREEN + " Darkmux " + Fore.WHITE + "|" + Fore.CYAN + f" {setsms} " + Fore.RED + Style.BRIGHT + "[●]")
        print(Fore.RESET + Style.RESET_ALL)
        print(Fore.RED + Style.BRIGHT + "[●]" + Style.NORMAL + Fore.YELLOW + " [3]-Zphisher " + Fore.WHITE + "|"  + Fore.GREEN + " htr-tech " + Fore.WHITE + "|" + Fore.CYAN + f" {zphisher} " + Fore.RED + Style.BRIGHT + "[●]")
        print(Fore.RESET + Style.RESET_ALL)
        print(Fore.RED + Style.BRIGHT + "[●]" + Style.NORMAL + Fore.YELLOW + " [4]-Sms send " + Fore.WHITE + "|"  + Fore.GREEN + " Blad " + Fore.WHITE + "|" + Fore.CYAN + f" {sms_send} " + Fore.RED + Style.BRIGHT + "[●]")
        print(Fore.RESET + Style.RESET_ALL)
        

        #seleccion de tool
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "selecciona una herramienta:")
        entrada = input(Fore.GREEN + "[►]:")

        if entrada == "1" or entrada == "01":
            clear_output()
            i = 1
            option_selecter_python(pyphisher, pyphisher_ruta)
        elif entrada == "2" or entrada == "02":
            clear_output()
            i = 1
            option_selecter_shell(setsms, setsms_ruta)
        elif entrada == "3" or entrada == "03":
            clear_output()
            i = 1
            option_selecter_shell(zphisher, zphisher_ruta)
        elif entrada == "4" or entrada == "04":
            clear_output()
            i = 1
            option_selecter_python(sms_send, sms_send_ruta)
        else:
            print(Fore.RED + "[●]" + " elije una de las opciones disponibles")
            i = 0

        
#python ejecutar
def option_selecter_python(repositorio, repositorio_ruta):
    
    if os.path.exists(repositorio_ruta):
        print(Fore.YELLOW + "incializando...")
        time.sleep(0.2)
        call(["python3", repositorio_ruta])
    else:
        print(Fore.YELLOW + "clonando repositorio...")
        time.sleep(0.2)
        call(["git", "clone", repositorio])
        print(Fore.YELLOW + "incializando...")
        time.sleep(0.2)
        call(["python3", repositorio_ruta])


#shell ejecutar
def option_selecter_shell(repositorio, repositorio_ruta):
    
    if os.path.exists(repositorio_ruta):
        print(Fore.YELLOW + "incializando...")
        time.sleep(0.5)
        call(["sudo","bash", repositorio_ruta])
        return
    else:
        print(Fore.YELLOW + "clonando repositorio...")
        time.sleep(0.5)
        call(["sudo", "git", "clone", repositorio])
        time.sleep(0.5)
        call(["sudo", "chmod", "777", repositorio_ruta])
        time.sleep(0.5)
        print(Fore.YELLOW + "incializando...")
        time.sleep(0.5)
        call(["sudo", "bash", repositorio_ruta])
        return

        
        

program_main()
        