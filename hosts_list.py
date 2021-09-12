#!/usr/bin/env python3

import os

activeHosts = []
hostCount = 0

for x in range(1,255):
    result = os.system("ping -n 1 -w 1250 " + "192.168.1." + str(x))
    if result == 0:
        activeHosts.append("192.168.1." + str(x))
    os.system("cls")

print("Creating \"active_hosts.txt\" file...")

with open("active_hosts.txt", "w") as file:
    for host in activeHosts:
        hostCount += 1
        print(f"host #{hostCount}: {host}")
        file.write(f"host #{hostCount}: {host}\n")
