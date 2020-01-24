# prototype code for binary clock.

from datetime import datetime
import time
import subprocess as sp
from itertools import zip_longest


while True:
    test = datetime.now()

    hour1 = bin(int(str(test.hour).zfill(2)[0]))[2:]
    hour2 = bin(int(str(test.hour).zfill(2)[1]))[2:]
    minute1 = bin(int(str(test.minute).zfill(2)[0]))[2:]
    minute2 = bin(int(str(test.minute).zfill(2)[1]))[2:]
    sec1 = bin(int(str(test.second).zfill(2)[0]))[2:]
    sec2 = bin(int(str(test.second).zfill(2)[1]))[2:]

    bintime = hour1.rjust(4, '0') + ' ' + hour2.rjust(4, '0') + ' ' + minute1.rjust(4, '0') + ' ' + minute2.rjust(4, '0') + ' ' + sec1.rjust(4, '0') + ' ' + sec2.rjust(4, '0')

    for x in zip_longest(*bintime.split(), fillvalue=' '):
        print (' '.join(x))

    time.sleep(1)
    sp.call('cls', shell=True)




