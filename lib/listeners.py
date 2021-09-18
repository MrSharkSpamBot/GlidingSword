# -*- coding: utf-8 -*-
"""
The listeners menu.

@author: Mr. Shark Spam Bot
"""
import os
import sys
from lib import listener

NORMAL = '\033[0m'
GREEN = '\33[32m'
BLUE = '\33[34m'
RED = '\033[91m'

LISTENERS = ['ShadowShark']

def main():
    '''The listeners menu.'''
    os.chdir('Listeners')
    while True:
        command = input(f'{GREEN}GlidingSword{NORMAL}/{BLUE}Listeners{NORMAL}> ')
        command = command.lower().strip()
        command = command.split()
        if len(command) == 0:
            continue
        if command[0] == 'list':
            for alistener in LISTENERS:
                print(alistener)
        if command[0] == 'back':
            os.chdir('..')
            return
        if command[0] == 'clear':
            print('[H[2J[3J', end='')
        if command[0] == 'exit':
            sys.exit()
        if command[0] == 'help':
            print('Command Name        Command Usage        Command Description')
            print('------------        -------------        -------------------')
            print('back                back                 Go back one menu.')
            print('help                help                 Get help.')
            print('exit                exit                 Exit out of Gliding Sword.')
            print('clear               clear                Clear the screen.')
            print('list                list                 Show all the listeners.')
            print('use                 use LISTENER         Use a listener.')
        if command[0] == 'use':
            if len(command) == 1:
                print(f'{RED}[-] No listener to use.{NORMAL}')
                continue
            if len(command) >= 2:
                for alistener in LISTENERS:
                    if command[1] == alistener.lower():
                        break
                if command[1] != alistener.lower():
                    print(f'{RED}[-] Invalid listener {command[1]}.{NORMAL}')
                    continue
                if alistener == 'ShadowShark':
                    listener.ShadowSharkListener().main()
