import subprocess
import time
from subprocess import call
from colorama import init, Fore, Back, Style
import git
import pyfiglet
import os
from IPython.display import clear_output



#fore reset
init(autoreset=True)

#var


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

#vidphisher
vidphisher = "https://github.com/KasRoudra/VidPhisher"
vidphisher_ruta = "VidPhisher/vp.sh"
vidphisher_folder = "VidPhisher"

#sherlock

sherlock = "https://github.com/sherlock-project/sherlock"
sherlock_ruta = "sherlock/sherlock"
sherlock_folder = ""
requirements = "sherlock/requirements.txt"


def program_main():
    i = 0
    while i == 0:
        
        #ui
        name = "blad"
        texto_ascii = pyfiglet.figlet_format("tool kit 1.0")
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
        print(Fore.RED + Style.BRIGHT + "[●]" + Style.NORMAL + Fore.YELLOW + " [5]-Vid phisher " + Fore.WHITE + "|"  + Fore.GREEN + " KasRoudra " + Fore.WHITE + "|" + Fore.CYAN + f" {vidphisher} " + Fore.RED + Style.BRIGHT + "[●]")
        print(Fore.RESET + Style.RESET_ALL)
        print(Fore.RED + Style.BRIGHT + "[●]" + Style.NORMAL + Fore.YELLOW + " [6]-Sherlock " + Fore.WHITE + "|"  + Fore.GREEN + " Sherlock Project " + Fore.WHITE + "|" + Fore.CYAN + f" {sherlock} " + Fore.RED + Style.BRIGHT + "[●]")
        print(Fore.RESET + Style.RESET_ALL)
        

        #seleccion de tool
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "selecciona una herramienta:")
        entrada = input(Fore.GREEN + "[►]:")

        if entrada == "1" or entrada == "01":
            os.system('clear')
            i = 1
            option_selecter_python(pyphisher, pyphisher_ruta)
        elif entrada == "2" or entrada == "02":
            os.system('clear')
            i = 1
            option_selecter_shell(setsms, setsms_ruta)
        elif entrada == "3" or entrada == "03":
            os.system('clear')
            i = 1
            option_selecter_shell(zphisher, zphisher_ruta)
        elif entrada == "4" or entrada == "04":
            os.system('clear')
            i = 1
            option_selecter_python(sms_send, sms_send_ruta)
        elif entrada == "5" or entrada == "05":
            os.system('clear')
            i = 1
            option_selecter_python(vidphisher, vidphisher_ruta)
        elif entrada == "6" or entrada == "06":
            os.system('clear')
            i = 1
            sherlock_sign = pyfiglet.figlet_format("Sherlock")
            print(Fore.GREEN + Style.BRIGHT +sherlock_sign)
            print(Fore.GREEN + "escribe lo que quieres buscar:")
            user_search = input(Fore.GREEN + "[►]:")
            option_selecter_sherlock(sherlock, sherlock_ruta, requirements, user_search)

            
        else:
            os.system('clear')
            print(Fore.RED + "[●]" + " elije una de las opciones disponibles")
            i = 0
        
        
#sherlock ejecutar
def option_selecter_sherlock(repositorio, repositorio_ruta, req, username):
    if os.path.exists(repositorio_ruta):
        print(Fore.YELLOW + "incializando...")
        time.sleep(0.2)
    else:
        print(Fore.YELLOW + "clonando repositorio...")
        time.sleep(0.2)
        call(["git", "clone", repositorio])
        print(Fore.YELLOW + "incializando...")
        time.sleep(0.2)
        call(["python3", "-m", "pip", "install", "-r", req])
    call(["python3", repositorio_ruta, username])
    
    
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


program_main()
        