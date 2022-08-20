import os
import random
import time

class renkler:
    PEMBE = '\033[95m'
    MAVI = '\033[94m'
    CAMGOBEGI = '\033[96m'
    YESIL = '\033[92m'
    SARI = '\033[93m'
    KIRMIZI = '\033[91m'
    DUZ = '\033[0m'
    KALIN = '\033[1m'
    ALTICIZILI = '\033[4m'


banner = """

 ___  ___  _______   ________  ________  ________        _____ ______   ________  ___  __    ___  ________   _______   ________  ___                                                         
|\  \|\  \|\  ___ \ |\   ____\|\   __  \|\   __  \      |\   _ \  _   \|\   __  \|\  \|\  \ |\  \|\   ___  \|\  ___ \ |\   ____\|\  \                                                        
\ \  \ \  \ \   __/|\ \  \___|\ \  \|\  \ \  \|\  \     \ \  \ \__\ \  \ \  \|\  \ \  \/  /|\ \  \ \  \  \  \ \   __/|\ \  \___|\ \  \                                                       
 \ \   __  \ \  \_|/_\ \_____  \ \   __  \ \   ____\     \ \  \ |__| \  \ \   __  \ \   ___  \ \  \ \  \  \  \ \  \_|/_\ \_____  \ \  \                                                      
  \ \  \ \  \ \  \_|\ \|____|\  \ \  \ \  \ \  \___|      \ \  \    \ \  \ \  \ \  \ \  \  \  \ \  \ \  \  \  \ \  \_|\ \|____|\  \ \  \                                                     
   \ \__\ \__\ \_______\____\_\  \ \__\ \__\ \__\          \ \__\    \ \__\ \__\ \__\ \__\  \__\ \__\ \__\  \__\ \_______\____\_\  \ \__\                                                    
    \|__|\|__|\|_______|\_________\|__|\|__|\|__|           \|__|     \|__|\|__|\|__|\|__| \|__|\|__|\|__| \|__|\|_______|\_________\|__|                                                    
                       \|_________|                                                                                      \|_________|                                                        
                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                           
                                                                                                                                                                                             
 ________  ________  ________  _______   ________          ___  __    ___  ___  ________  _______       ___    ___      ________  _______       ___    ___ ___       ________  ________      
|\   ____\|\   __  \|\   ___ \|\  ___ \ |\   ___ \        |\  \|\  \ |\  \|\  \|\_____  \|\  ___ \     |\  \  /  /|    |\   ____\|\  ___ \     |\  \  /  /|\  \     |\   __  \|\   ___  \    
\ \  \___|\ \  \|\  \ \  \_|\ \ \   __/|\ \  \_|\ \       \ \  \/  /|\ \  \ \  \ |___/  /\ \   __/|    \ \  \/  / /    \ \  \___|\ \   __/|    \ \  \/  / | \  \    \ \  \|\  \ \  \  \  \   
 \ \  \    \ \  \ \  \ \  \ \  \ \  \_|/_\ \  \  \ \       \ \   ___  \ \  \ \  \   /  / /\ \  \_|/__   \ \    / /      \ \  \    \ \  \_|/__   \ \    / / \ \  \    \ \   __  \ \  \  \  \  
  \ \  \____\ \  \ \  \ \  \_\  \ \  \_|\ \ \  \__\ \       \ \  \  \  \ \  \ \  \ /  /_/__\ \  \_|\ \   \/  /  /        \ \  \____\ \  \_|\ \   \/  /  /   \ \  \____\ \  \ \  \ \  \  \  \ 
   \ \_______\ \_______\ \_______\ \_______\ \_______\       \ \__\  \__\ \_______/ ________\ \_______\__/  / /           \ \_______\ \_______\__/  / /      \ \_______\ \__\ \__\ \__\  \__|
    \|_______|\|_______|\|_______|\|_______|\|_______|        \|__| \|__|\|_______|\|_______|\|_______|\___/ /             \|_______|\|_______|\___/ /        \|_______|\|__|\|__|\|__| \|__|
                                                                                                      \|___|/                                 \|___|/                                        

"""

selection_banner = """
*--------------------------------*
|       -İşlem Komut Tablosu-    |
|                                |
| çarpma : x                     |
| toplama : +                    |
| çıkarma : -                    |
| bölme : /                      |
|                                |
*--------------------------------*


"""


while True:

    print(renkler.KALIN)
    print(renkler.KIRMIZI + selection_banner)


    try:
        d1 = int(input(renkler.SARI + "DEĞER 1: "))
        i1 = str(input(renkler.MAVI + "İşlem: "))
        d2 = int(input(renkler.SARI + "DEĞER 2: "))


        if i1 == "x":
            output = d1 * d2
            print(renkler.YESIL + f"SONUÇ = {output}")
        
        if i1 == "/":
            try:
                output = d1 / d2
                print(renkler.YESIL + f"SONUÇ = {output}")
            except ZeroDivisionError:
                print(renkler.KIRMIZI + "\n0 İLE BİRŞEY BÖLÜNMEZ AKILLI")


        if i1 == "-":
            output = d1 - d2
            print(renkler.YESIL + f"SONUÇ = {output}")

        if i1 == "+":
            output = d1 + d2
        print(renkler.YESIL + f"SONUÇ = {output}\n\n")

    except ValueError:
        print(renkler.KIRMIZI + "LÜTFEN RAKAMSAL DEĞER GİRİNİZ. AKSİ TAKDİRDE PROGRAM ÇALIŞMAZ.")