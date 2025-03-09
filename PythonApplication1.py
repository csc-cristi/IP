import urllib.request
import json
import time
from colorama import init, Fore
import os
import random

init()

class Data:
    def __init__(self, city, region, country, loc, postal, timezone):
        self.city = city
        self.region = region
        self.country = country
        self.loc = loc
        self.postal = postal
        self.timezone = timezone

def genereaza_numar(start, end):
    return random.randint(start, end)

def blackjack():
     
     global fonduri
     fonduri= 100
     while fonduri > 0:
        while True:
            try:
                print(Fore.BLUE)
                print("   ___  __         __       _          __  ")
                print("  / _ )/ /__ _____/ /__    (_)__ _____/ /__")
                print(" / _  / / _ `/ __/  '_/   / / _ `/ __/  '_/")
                print("/____/_/\_,_/\__/_/\_\ __/ /\_,_/\__/_/\_\ ")
                print("                      |___/                ")
                print(" ")
                print(Fore.MAGENTA)
                pariu = int(input(f"You have {fonduri}$ . What is the ammount you want to gamble? "))
                print(" ")
                if pariu > fonduri:
                    print("Not enought money. ")
                    print(" ")
                    continue
                elif pariu <= 0:
                    print("Negative number. Try again.")
                    print(" ")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
                print(" ")

        suma = 0
        continua = True

        while continua:
            n = genereaza_numar(1, 14)
            suma += n
            print(Fore.CYAN)
            print(f"______________________")
            print(f"|                    |")
            print(f"|   {n }               |")
            print(f"|                    |")
            print(f"|                    |")
            print(f"|                    |")
            print(f"|                    |")
            print(f"|                    |")
            print(f"|                    |")
            print(f"|                    |")
            print(f"|              {n }    | ")
            print(f"|___________________ |")
            print(" ")
            print(f"{suma} / 21")
            
            print(Fore.MAGENTA)
            if suma > 21:
                print(" ")
                print(f"You lost {pariu} $")
                time.sleep(5)  
                os.system('cls' if os.name == 'nt' else 'clear')  
                fonduri -= pariu
                break
            else:
                optiune = input("Take a card (c) or stop (o)? ").strip().lower()
                print(" ")
                if optiune == 'o':
                    numar_computer = genereaza_numar(17, 21)
                    print(f"Oponent number: {numar_computer}")
                    print(" ")
                    print(f"{numar_computer} and {suma}")
                    if suma > numar_computer:
                        print(" ")
                        print(f"You won {pariu*3} $")
                        time.sleep(5)  
                        os.system('cls' if os.name == 'nt' else 'clear')  
                        fonduri += pariu*3
                    elif suma < numar_computer:
                        print(" ")
                        print(f"You lost {pariu} $")
                        time.sleep(5)  
                        os.system('cls' if os.name == 'nt' else 'clear')  
                        fonduri -= pariu
                    else:
                        print(" ")
                        print("Same number!")
                        time.sleep(5)  
                        os.system('cls' if os.name == 'nt' else 'clear')  
                    continua = False
                elif optiune != 'c':
                    print("Invalide option. Please select 'c' to take a card or 'o' to stop here.")

        if fonduri <= 0:
            print("Not enought money left. The game ends.")
            break
        

def iptracker():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(Fore.GREEN)
    print("██╗██████╗     ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ ")
    print("██║██╔══██╗    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗")
    print("██║██████╔╝       ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝  Made by Baba》Yaga")
    print("██║██╔═══╝        ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗")
    print("██║██║            ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║")
    print("╚═╝╚═╝            ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  V0.1.0")
    print(" ")
    print(f"{Fore.YELLOW}[{Fore.WHITE}0{Fore.YELLOW}] {Fore.RED}Back               {Fore.YELLOW}[{Fore.WHITE}1{Fore.YELLOW}] {Fore.RED}Continue"               )
    print(" ")
    print(Fore.GREEN)
    i = input("")
    print(" ")
    if i == "0":
        os.system('cls' if os.name == 'nt' else 'clear')
        main()
    elif i=="1":
     ip = input("Enter IP: ")
     url = f"https://ipinfo.io/{ip}/json"
    
    try:
        with urllib.request.urlopen(url) as response:
            responseData = response.read().decode('utf-8')
            ipInfo = json.loads(responseData)

            os.system('cls' if os.name == 'nt' else 'clear')

            
            time.sleep(2)
            print("[+] Request Successfully Made")
            print(" ")
            time.sleep(1)
            print("Loading [          ] 0%")
            time.sleep(1)
            print("Loading [####      ] 47%")
            time.sleep(3)
            print("Loading [#######   ] 66%")
            time.sleep(1)
            print("Loading [######### ] 89%")
            time.sleep(1)
            print("Loading [##########] 100%")
            time.sleep(1)
            print(" ")
            time.sleep(2)
            print("[!] Data Found")

            ipData = Data(
                city=ipInfo['city'],
                region=ipInfo['region'],
                country=ipInfo['country'],
                loc=ipInfo['loc'],
                postal=ipInfo['postal'],
                timezone=ipInfo['timezone']
            )
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

            print(" ")
            print(" ")
            print(" ")
            print("   [!] Target info [!]   ")
            print(" ")
            print(f"Country: {ipData.country}")
            print(f"City: {ipData.city}")
            print(f"Coordinates: {ipData.loc}")
            print(f"Region: {ipData.region}")
            print(f"Timezone: {ipData.timezone}")
            print("")
            print("[?] Thank you for using ")

            time.sleep(10)

    except Exception as ex:
        print(f"Error: {ex}")
    

def main():
    print(Fore.RED)
    print("   ▄███████▄    ▄█    █▄     ▄██████▄     ▄████████ ███▄▄▄▄    ▄█  ▀████    ▐████▀")
    print("  ███    ███   ███    ███   ███    ███   ███    ███ ███▀▀▀██▄ ███    ███▌   ████▀  ")
    print("  ███    ███   ███    ███   ███    ███   ███    █▀  ███   ███ ███▌    ███  ▐███    ")
    print("  ███    ███  ▄███▄▄▄▄███▄▄ ███    ███  ▄███▄▄▄     ███   ███ ███▌    ▀███▄███▀       Made by Baba》Yaga")
    print("▀█████████▀  ▀▀███▀▀▀▀███▀  ███    ███ ▀▀███▀▀▀     ███   ███ ███▌    ████▀██▄     ")
    print("  ███          ███    ███   ███    ███   ███    █▄  ███   ███ ███    ▐███  ▀███    ")
    print("  ███          ███    ███   ███    ███   ███    ███ ███   ███ ███   ▄███     ███▄  ")
    print(" ▄████▀        ███    █▀     ▀██████▀    ██████████  ▀█   █▀  █▀   ████       ███▄   V0.0.5")
    print(" ")
    print(" ")
    print(f"{Fore.YELLOW}[{Fore.WHITE}1{Fore.YELLOW}] {Fore.RED}IP Tracking        {Fore.YELLOW}[{Fore.WHITE}2{Fore.YELLOW}] {Fore.RED} Black Jack ")
    print(" ")
    x = input("")
    print(" ")

    if x == "1":
        iptracker()

    elif x == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        blackjack()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Invalid option. Please choose between 1 and 2.")
        main()

if __name__ == "__main__":
    main()

