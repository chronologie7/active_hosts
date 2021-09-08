#!/usr/bin/env python3

import os

activeHosts = []

for x in range(1,255):
    result = os.system("ping -n 1 -w 500 " + "192.168.1." + str(x))
    if result == 0:
        activeHosts.append("192.168.1." + str(x))

print(activeHosts)