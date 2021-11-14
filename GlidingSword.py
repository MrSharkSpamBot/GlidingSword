# -*- coding: utf-8 -*-
"""
The main menu.

@author: Mr. Shark Spam Bot
"""
import os
import sys
import readline
from lib import listeners
from lib import payloads
from lib import colors

PATH = os.path.dirname(__file__)

def main():
    '''The main menu.'''
    while True:
        try:
            command = input(f'{colors.glidingsword}GlidingSword{colors.normal}> ')
            command = command.lower().strip()
            if len(command) == 0:
                continue
            if command == 'clear':
                print('[H[2J[3J', end='')
            if command == 'exit':
                sys.exit()
            if command == 'help':
                print('Command Name        Command Usage        Command Description')
                print('------------        -------------        -------------------')
                print('help                help                 Get help.')
                print('exit                exit                 Exit out of Gliding Sword.')
                print('clear               clear                Clear the screen.')
                print('payloads            payloads             Go to the payloads menu.')
                print('listeners           listeners            Go to the listeners menu.')
            if command == 'payloads':
                payloads.main()
            if command == 'listeners':
                listeners.main()
        except KeyboardInterrupt:
            os.chdir(PATH)
            print()
            continue

if __name__ == '__main__':
    print('''

\t░██████╗░██╗░░░░░██╗██████╗░██╗███╗░░██╗░██████╗░
\t██╔════╝░██║░░░░░██║██╔══██╗██║████╗░██║██╔════╝░
\t██║░░██╗░██║░░░░░██║██║░░██║██║██╔██╗██║██║░░██╗░
\t██║░░╚██╗██║░░░░░██║██║░░██║██║██║╚████║██║░░╚██╗
\t╚██████╔╝███████╗██║██████╔╝██║██║░╚███║╚██████╔╝
\t░╚═════╝░╚══════╝╚═╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░

\t░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░
\t██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗
\t╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║
\t░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║
\t██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝
\t╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░
\tCreated by Mr. Shark Spam Bot.

Listeners: 1
Payloads: 3
Payload Types: 1
    ''')
    os.chdir(PATH)
    main()
