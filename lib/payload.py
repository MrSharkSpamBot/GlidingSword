# -*- coding: utf-8 -*-
"""
The payload menu.

@author: Mr. Shark Spam Bot
"""
import socket
import sys
import secrets
import string
import random

class Payload:
    '''Menu for specified payload.'''
    def __init__(self, payload, payload_type, info):
        super().__init__()
        self.payload = payload
        self.payload_type = payload_type
        self.info = info
        self.lhost = ''
        self.lport = ''
        self.encryption = ''
        self.obfuscate = ''
        self.normal = '\033[0m'
        self.green = '\033[92m'
        self.green2 = '\33[32m'
        self.red = '\033[91m'
        self.purple = '\33[35m'

    def display_options(self):
        '''Display the options.'''
        print('{0: <18} '.format('Option Name') + '{0: <18} '.format('Option Value') + '{0: <18} '.format('Option Description'))
        print('{0: <18} '.format('-----------') + '{0: <18} '.format('------------') + '{0: <18} '.format('------------------'))
        print('{0: <18} '.format('LHOST') + '{0: <18} '.format(self.lhost) + '{0: <18} '.format('Your IP.'))
        print('{0: <18} '.format('LPORT') + '{0: <18} '.format(self.lport) + '{0: <18} '.format('The port to send the connection to.'))
        print('{0: <18} '.format('ENCRYPTION') + '{0: <18} '.format(self.encryption) + '{0: <18} '.format('The encryption used over TCP.'))
        print('{0: <18} '.format('OBFUSCATE') + '{0: <18} '.format(self.obfuscate) + '{0: <18} '.format('Whether or not to obfuscate the payload.'))

    def display_help(self):
        '''Display the commands.'''
        print('Command Name        Command Usage        Command Description')
        print('------------        -------------        -------------------')
        print('back                back                 Go back one menu.')
        print('info                info                 Get the payload info.')
        print('options             options              Check the options and their values.')
        print('help                help                 Get help.')
        print('generate            generate             Generate a payload.')
        print('exit                exit                 Exit out of Gliding Sword.')
        print('clear               clear                Clear the screen.')
        print('set                 set OPTION VALUE     Set a value for the specified option.')

    def valid_lhost(self):
        '''Validify the LHOST.'''
        try:
            socket.inet_aton(self.lhost)
        except socket.error:
            print(f'{self.red}[-] Invalid value for LHOST.{self.normal}')
            return False
        if self.lhost.count('.') != 3:
            print(f'{self.red}[-] Invalid value for LHOST.{self.normal}')
            return False

    def valid_lport(self):
        '''Validify the LPORT.'''
        if not self.lport.isdecimal():
            print(f'{self.red}[-] Invalid value for LPORT.{self.normal}')
            return False
        if not 0 < int(self.lport) <= 65535:
            print(f'{self.red}[-] Invalid value for LPORT.{self.normal}')
            return False

    def valid_encryption(self):
        if not self.encryption in ['hex', 'base64']:
            print(f'{self.red}[-] Invalid value for ENCRYPTION.{self.normal}')
            return False

    def valid_obfuscate(self):
        if not self.obfuscate in ['yes', 'no']:
            print(f"{self.red}[-] Invalid value for OBFUSCATE.{self.normal}")
            return False

    def generate(self):
        '''Generate the payload.'''
        if self.valid_lhost() is False:
            return
        if self.valid_lport() is False:
            return
        if self.valid_encryption() is False:
            return
        if self.valid_obfuscate() is False:
            return
        with open(self.payload + '.py', 'r') as payload:
            payload = payload.read()
        payload = payload.replace('IP', self.lhost, 1)
        payload = payload.replace('PORT', self.lport, 1)
        if self.encryption == 'base64':
            payload = payload.replace('hex', 'base64')
        if self.obfuscate == 'yes':
            for i in range(5):
                payload = f'{secrets.token_bytes()}\n' + payload
            letters = string.ascii_letters
            new_text = ''.join(random.choice(letters) for i in range(64))
            payload = payload.replace('new_text', new_text)
            rev_socket = ''.join(random.choice(letters) for i in range(64))
            payload = payload.replace('rev_socket', rev_socket)
            command = ''.join(random.choice(letters) for i in range(64))
            payload = payload.replace('command', command)
            output = ''.join(random.choice(letters) for i in range(64))
            payload = payload.replace('output', output)
            for i in range(5):
                payload = payload + f'{secrets.token_bytes()}\n'
        print(f'{self.green}[+] Successfully generated payload.{self.normal}\n')
        print(payload)

    def main(self):
        '''The menue for the payload.'''
        while True:
            command = input(f'{self.green2}GlidingSword{self.normal}/{self.purple}Payloads{self.normal}/{self.payload_type}/{self.payload}> ')
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
            if command[0] == 'generate':
                self.generate()
            if command[0] == 'exit':
                sys.exit()
            if command[0] == 'help':
                self.display_help()
            if command[0] == 'set':
                if len(command) == 1:
                    print(f'{self.red}[-] No option to set.{self.normal}')
                    continue
                if len(command) >= 2:
                    if not command[1] in ['lhost', 'lport', 'encryption', 'obfuscate']:
                        print(f'{self.red}[-] Invalid option {command[1]}.{self.normal}')
                        continue
                if len(command) == 2:
                    print(f'{self.red}[-] No value to set for option {command[1]}.{self.normal}')
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
                    if command[1] == 'obfuscate':
                        self.obfuscate = command[2]
                        if self.valid_obfuscate() is False:
                            self.obfuscate = ''
