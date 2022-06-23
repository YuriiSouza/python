#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
    print(site.read())
except:
    print("Pudim esta offline")
else:
    print("Pudim esta online")
