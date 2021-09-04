# -*- coding: utf-8 -*-
"""
The payloads menu.

@author: Mr. Shark Spam Bot
"""
import os
import sys
from lib import payload

NORMAL = '\033[0m'
GREEN = '\33[32m'
PURPLE = '\33[35m'
RED = '\033[91m'

PAYLOAD_TYPES = ['ShadowShark']
SHADOWSHARK = {'WindowsPayload': 'A full fledged Shadow Shark payload for Windows.',
'UnixPayload': 'A full fledged Shadow Shark payload for Unix.',
'OGPayload': 'The original Shadow Shark reverse shell.'}

def payload_type_menu(payload_type, payloads):
    '''The menu for a payload type.'''
    os.chdir(payload_type)
    while True:
        command = input(f'{GREEN}GlidingSword{NORMAL}/{PURPLE}Payloads{NORMAL}/{payload_type}> ')
        command = command.lower().strip()
        command = command.split()
        if len(command) == 0:
            continue
        if command[0] == 'list':
            for p in payloads.keys():
                print(p)
        if command[0] == 'back':
            os.chdir('..')
            return
        if command[0] == 'clear':
            print('[H[2J[3J')
        if command[0] == 'exit':
            sys.exit()
        if command[0] == 'help':
            print('Command Name        Command Usage        Command Description')
            print('------------        -------------        -------------------')
            print('back                back                 Go back one menu.')
            print('help                help                 Get help.')
            print('exit                exit                 Exit out of Gliding Sword.')
            print('clear               clear                Clear the screen.')
            print('list                list                 Show all the payloads.')
            print('use                 use PAYLOAD          Use a payload.')
        if command[0] == 'use':
            if len(command) == 1:
                print(f'{RED}[-] No payload to use.{NORMAL}')
                continue
            if len(command) >= 2:
                for p in payloads.keys():
                    if command[1] == p.lower():
                        info = payloads[p]
                        break
                if command[1] != p.lower():
                    print(f'{RED}[-] Invalid payload {command[1]}{NORMAL}.')
                    continue
                payload.Payload(p, payload_type, info).main()

def main():
    '''The payloads menu.'''
    os.chdir('Payloads')
    while True:
        command = input(f'{GREEN}GlidingSword{NORMAL}/{PURPLE}Payloads{NORMAL}> ')
        command = command.lower().strip()
        command = command.split()
        if len(command) == 0:
            continue
        if command[0] == 'list':
            for payload_type in PAYLOAD_TYPES:
                print(payload_type)
        if command[0] == 'back':
            os.chdir('..')
            return
        if command[0] == 'clear':
            print('[H[2J[3J')
        if command[0] == 'exit':
            sys.exit()
        if command[0] == 'help':
            print('Command Name        Command Usage        Command Description')
            print('------------        -------------        -------------------')
            print('back                back                 Go back one menu.')
            print('help                help                 Get help.')
            print('exit                exit                 Exit out of Gliding Sword.')
            print('clear               clear                Clear the screen.')
            print('list                list                 Show all the payload types.')
            print('use                 use PAYLOAD_TYPE     Use a payload type.')
        if command[0] == 'use':
            if len(command) == 1:
                print(f'{RED}[-] No payload type to use.{NORMAL}')
                continue
            if len(command) >= 2:
                for payload_type in PAYLOAD_TYPES:
                    if command[1] == payload_type.lower():
                        break
                if command[1] != payload_type.lower():
                    print(f'{RED}[-] Invalid payload type {command[1]}.{NORMAL}')
                    continue
                if payload_type == 'ShadowShark':
                    payload_type_menu(payload_type, SHADOWSHARK)
