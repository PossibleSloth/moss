#!/usr/bin/python

import requests
import socket
import sys
import os

SERVER = "moss.stanford.edu"
PORT = 7690

USERID = ""

def sendfile(filename, fileid, lang, sock):
    with open(filename, 'r') as fd:
        content = fd.read()
    size = len(content)

    print("uploading %s" %filename)

    sock.send("file %d %s %d %s\n" %(fileid, lang, size, filename))
    sock.send(content)

def getfiles(basedir, extension):
    a = os.listdir(basedir)
    print(a)

def main():
    # options
    directory = 1
    lang = "javascript"
    optm = 10
    optx = 0
    optc = ""
    optn = 250
    bindex = 0


    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER, PORT))

    sock.send("moss %s\n" %USERID)
    sock.send("directory %d\n" %directory)
    sock.send("X %d\n" %optx)
    sock.send("maxmatches %d\n" %optm)
    sock.send("show %d\n" %optn)

    sock.send("language %s\n" %lang )
    response = sock.recv(1024)

    if response=="no":
        sock.send("end\n")
        print("Unsupported language")
        exit()

    print("uploading files")

getfiles("downloads", "js")
