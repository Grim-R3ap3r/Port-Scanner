import socket
from colorama import Fore
from time import sleep





solax = """
                   _                                              
                  | |                                             
  _ __   ___  _ __| |_ ______ ___  ___ __ _ _ __  _ __   ___ _ __ 
 | '_ \ / _ \| '__| __|______/ __|/ __/ _` | '_ \| '_ \ / _ \ '__|
 | |_) | (_) | |  | |_       \__ \ (_| (_| | | | | | | |  __/ |   
 | .__/ \___/|_|   \__|      |___/\___\__,_|_| |_|_| |_|\___|_|   
 | |                                                              
"""
print(solax)
sleep(0.60)

ip_inp = input("[+] ENTER THE TARGET IP : ")
ip = ip_inp
port_list = [21, 22, 53, 25, 50, 67, 69, 80, 110, 119, 123, 135, 143, 161, 389, 443, 989, 3386]

for port in port_list:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((ip, port))

    if result == 0:
        print(Fore.GREEN + "----------------------------")
        print(Fore.GREEN + '{ [+] Port : ', port, 'open }')
        print(Fore.GREEN + "----------------------------")
    else:
        print(Fore.RED + "----------------------------")
        print(Fore.RED + '{ [!] Port : ', port, 'closed } ')
        print(Fore.RED + "----------------------------")
        
        
input("[*] DONE SCANNING | PRESS ENTER TO  EXIT : ")