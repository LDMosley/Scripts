'''
Inspired after reading an article by Jan Markowski  in the magazine 2600
here is a simple script to check if a password is  -- safe -- to use
without actually exposing the actual password.
'''

import hashlib
import requests
import sys

if len(sys.argv) != 2:
    print('Usage - Pass one argument.  The password you want to check. \nExample: '
        '"python passchk.py password"')
    sys.exit(1)

candidate = sys.argv[1]


passHash = hashlib.sha1(candidate.encode('utf-8'))

passHead = passHash.hexdigest()[:5]
passTail = passHash.hexdigest()[5:]
passList = []

url = 'https://api.pwnedpasswords.com/range/' + passHead

response = requests.get(url).text.split()

for item in response:
    passList.append(item.split(':')[0])

if passTail.upper() in passList:
    print(candidate + ' has been pwned! Do not use!')
else:
    print(candidate + ' is safe (for now)')






