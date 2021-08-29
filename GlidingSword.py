# -*- coding: utf-8 -*-
"""
The main menu.

@author: Mr. Shark Spam Bot
"""
import sys
from lib import listeners
from lib import payloads

NORMAL = '\033[0m'
GREEN = '\33[32m'

LISTENERS = ['ShadowShark']

def main():
    '''The main menu.'''
    while True:
        try:
            command = input(f'{GREEN}GlidingSword{NORMAL}> ')
            command = command.lower().strip()
            if len(command) == 0:
                continue
            if command == 'clear':
                print('[H[2J[3J')
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
    main()
