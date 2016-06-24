#!/usr/bin/env python3


inFile = open('cat.jpg', 'rb')
outFile = open('copy.jpg', 'wb')

while True:
    data = inFile.read(1024)
    if not data:
        break
    outFile.write(data)

inFile.close()
outFile.close()