#!/usr/bin/env python3


def readFile(name, mode):

    file = open(name, mode)

    if mode == 'rb':
        data = b''
    else:
        data = ''

    while True:

        buffer = file.read(1024)
        if not buffer:
            break
        data += buffer

    file.close()

    return data

def writeFile(data, name, mode):

    file = open(name, mode)

    file.write(data)

    file.close()