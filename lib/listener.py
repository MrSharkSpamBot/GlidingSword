# -*- coding: utf-8 -*-
"""
The listener menu.

@author: Mr. Shark Spam Bot
"""
import socket
import sys
import subprocess
from lib import colors

class Listener:
    '''Menu for specified listener.'''
    def __init__(self, listener, arguments, info):
        super().__init__()
        self.listener = listener
        self.arguments = arguments
        self.info = info
        self.lhost = ''
        self.lport = ''

    def display_options(self):
        '''Display the options.'''
        print('{0: <18} '.format('Option Name') + '{0: <18} '.format('Option Value') + '{0: <18} '.format('Option Description'))
        print('{0: <18} '.format('-----------') + '{0: <18} '.format('------------') + '{0: <18} '.format('------------------'))
        print('{0: <18} '.format('LHOST') + '{0: <18} '.format(self.lhost) + '{0: <18} '.format('Your IP.'))
        print('{0: <18} '.format('LPORT') + '{0: <18} '.format(self.lport) + '{0: <18} '.format('The port to send the connection to.'))

    def display_help(self):
        '''Display the commands.'''
        print('Command Name        Command Usage        Command Description')
        print('------------        -------------        -------------------')
        print('back                back                 Go back one menu.')
        print('info                info                 Get the listener info.')
        print('options             options              Check the options and their values.')
        print('help                help                 Get help.')
        print('run                 run                  Run a listener.')
        print('exit                exit                 Exit out of Gliding Sword.')
        print('clear               clear                Clear the screen.')
        print('set                 set OPTION VALUE     Set a value for the specified option.')

    def valid_lhost(self):
        '''Validify the LHOST.'''
        try:
            socket.inet_aton(self.lhost)
        except socket.error:
            print(f'{colors.error}[-] Invalid value for LHOST.{colors.normal}')
            return False
        if self.lhost.count('.') != 3:
            print(f'{colors.error}[-] Invalid value for LHOST.{colors.normal}')
            return False

    def valid_lport(self):
        '''Validify the LPORT.'''
        if not self.lport.isdecimal():
            print(f'{colors.error}[-] Invalid value for LPORT.{colors.normal}')
            return False
        if not 0 < int(self.lport) <= 65535:
            print(f'{colors.error}[-] Invalid value for LPORT.{colors.normal}')
            return False

    def run(self):
        '''Run the listener.'''
        if self.valid_lhost() is False:
            return
        if self.valid_lport() is False:
            return
        try:
            subprocess.call(f'python3 {self.listener}.py {self.arguments[0]} {self.lhost} {self.arguments[1]} {self.lport} ')
        except KeyboardInterrupt:
            pass

    def main(self):
        '''The menu for the listener.'''
        while True:
            command = input(f'{colors.glidingsword}GlidingSword{colors.normal}/{colors.listeners}Listeners{colors.normal}/{self.listener}> ')
            command = command.lower().strip()
            command = command.split()
            if len(command) == 0:
                continue
            if command[0] == 'back':
                return
            if command[0] == 'clear':
                print('[H[2J[3J', end='')
            if command[0] == 'options':
                self.display_options()
            if command[0] == 'info':
                print(self.info)
            if command[0] == 'run':
                self.run()
            if command[0] == 'exit':
                sys.exit()
            if command[0] == 'help':
                self.display_help()
            if command[0] == 'set':
                if len(command) == 1:
                    print(f'{colors.error}[-] No option to set.{colors.normal}')
                    continue
                if len(command) >= 2:
                    if not command[1] in ['lhost', 'lport']:
                        print(f'{colors.error}[-] Invalid option {command[1]}.{colors.normal}')
                        continue
                if len(command) == 2:
                    print(f'{colors.error}[-] No value to set for option {command[1]}.{colors.normal}')
                    continue
                if len(command) == 3:
                    if command[1] == 'lhost':
                        self.lhost = command[2]
                        if self.valid_lhost() is False:
                            self.lhost = ''
                    if command[1] == 'lport':
                        self.lport = command[2]
                        if self.valid_lport() is False:
                            self.lport = ''

class ShadowSharkListener:
    '''Menu for specified listener.'''
    def __init__(self):
        super().__init__()
        self.lhost = ''
        self.lport = ''
        self.encryption = ''

    def display_options(self):
        '''Display the options.'''
        print('{0: <18} '.format('Option Name') + '{0: <18} '.format('Option Value') + '{0: <18} '.format('Option Description'))
        print('{0: <18} '.format('-----------') + '{0: <18} '.format('------------') + '{0: <18} '.format('------------------'))
        print('{0: <18} '.format('LHOST') + '{0: <18} '.format(self.lhost) + '{0: <18} '.format('Your IP.'))
        print('{0: <18} '.format('LPORT') + '{0: <18} '.format(self.lport) + '{0: <18} '.format('The port to send the connection to.'))
        print('{0: <18} '.format('ENCRYPTION') + '{0: <18} '.format(self.encryption) + '{0: <18} '.format('The encryption used over TCP.'))

    def display_help(self):
        '''Display the commands.'''
        print('Command Name        Command Usage        Command Description')
        print('------------        -------------        -------------------')
        print('back                back                 Go back one menu.')
        print('info                info                 Get the listener info.')
        print('options             options              Check the options and their values.')
        print('help                help                 Get help.')
        print('run                 run                  Run a listener.')
        print('exit                exit                 Exit out of Gliding Sword.')
        print('clear               clear                Clear the screen.')
        print('set                 set OPTION VALUE     Set a value for the specified option.')

    def valid_lhost(self):
        '''Validify the LHOST.'''
        try:
            socket.inet_aton(self.lhost)
        except socket.error:
            print(f'{colors.error}[-] Invalid value for LHOST.{colors.normal}')
            return False
        if self.lhost.count('.') != 3:
            print(f'{colors.error}[-] Invalid value for LHOST.{colors.normal}')
            return False

    def valid_lport(self):
        '''Validify the LPORT.'''
        if not self.lport.isdecimal():
            print(f'{colors.error}[-] Invalid value for LPORT.{colors.normal}')
            return False
        if not 0 < int(self.lport) <= 65535:
            print(f'{colors.error}[-] Invalid value for LPORT.{colors.normal}')
            return False

    def valid_encryption(self):
        if not self.encryption in ['hex', 'base64']:
            print(f'{colors.error}[-] Only hex and base64 encryptions are supported.{colors.normal}')
            return False

    def run(self):
        '''Run the listener.'''
        if self.valid_lhost() is False:
            return
        if self.valid_lport() is False:
            return
        if self.valid_encryption() is False:
            return
        try:
            subprocess.call(f'python3 ShadowShark.py -lh {self.lhost} -lp {self.lport} -e {self.encryption}', shell=True)
        except KeyboardInterrupt:
            pass

    def main(self):
        '''The menu for the listener.'''
        while True:
            command = input(f'{colors.glidingsword}GlidingSword{colors.normal}/{colors.listeners}Listeners{colors.normal}/ShadowShark> ')
            command = command.lower().strip()
            command = command.split()
            if len(command) == 0:
                continue
            if command[0] == 'back':
                return
            if command[0] == 'clear':
                print('[H[2J[3J', end='')
            if command[0] == 'options':
                self.display_options()
            if command[0] == 'info':
                print('This tool is a full fledged reverse TCP handler used to interact with Shadow Shark payloads. Created by Mr. Shark Spam Bot.')
            if command[0] == 'run':
                self.run()
            if command[0] == 'exit':
                sys.exit()
            if command[0] == 'help':
                self.display_help()
            if command[0] == 'set':
                if len(command) == 1:
                    print(f'{colors.error}[-] No option to set.{colors.normal}')
                    continue
                if len(command) >= 2:
                    if not command[1] in ['lhost', 'lport', 'encryption']:
                        print(f'{colors.error}[-] Invalid option {command[1]}.{colors.normal}')
                        continue
                if len(command) == 2:
                    print(f'{colors.error}[-] No value to set for option {command[1]}.{colors.normal}')
                    continue
                if len(command) == 3:
                    if command[1] == 'lhost':
                        self.lhost = command[2]
                        if self.valid_lhost() is False:
                            self.lhost = ''
                    if command[1] == 'lport':
                        self.lport = command[2]
                        if self.valid_lport() is False:
                            self.lport = ''
                    if command[1] == 'encryption':
                        self.encryption = command[2]
                        if self.valid_encryption() is False:
                            self.encryption = ''
