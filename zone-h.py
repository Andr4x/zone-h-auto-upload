#!/usr/bin/python3
#Tool By Dr3xey
import os

os.system("cls||clear")

index = (r"""
________  _   _ _____      _   _
|__  / _ \| \ | | ____|    | | | |
  / / | | |  \| |  _| _____| |_| |
 / /| |_| | |\  | |__|_____|  _  |
/____\___/|_| \_|_____|    |_| |_|
Tool Created By Dr4xey
Twitter: @Dr4xeySecurity
""")

try:
    from colorama import Fore as F
except:
	print (index)
	print ("[!] Install: pip install colorama")
	exit()

try:
    import requests
except:
	print (index)
	print ("[!] Install: pip install requests")
	exit()


os.system("cls||clear")

print (F.GREEN + index + F.RESET)

nick = input("Nick:")
print ("")

with open('hackeds.txt','r') as pwn:
     brute = pwn.readlines()
     for ler in brute:
         r = requests.post("http://zone-h.com/notify/single", data={'defacer': nick, 'domain1': ler, 'hackmode': 1, 'reason': 1})
         vtx = "ERROR"
       	 if vtx in r.text:
            print (F.RED+"Zone-H Fail: "+ler+ F.RESET)
         else:
              print (F.GREEN+"Zone-H OK: "+ler+F.RESET)

###
