#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Jaden Rivera 3/20/2023

#
# Install the following modules
#
# python3 -m pip install python-geoip-python3
# python3 -m pip install python-geoip-geolite2
#

import os, re
import subprocess
from geoip import geolite2

def getCurrentDate():
    date = subprocess.run(["date"], stdout=subprocess.PIPE).stdout.decode()
    date = date.split()
    return date[1] + " " + date[2] + ", " + date[5]

def openfile(file):
    with open(file, 'r') as f:
        return f.read()

def getIPs(file):
    data = openfile(file)
    ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}', data)
    # if the IPs are the same, remove the duplicates
    ips = list(dict.fromkeys(ips))
    # sort the IPs in descending order by how  many times they appear
    ips.sort(key=lambda x: data.count(x), reverse=True)
    # return only the IPs with 10 or more failed password attempts
    ips = [i for i in ips if data.count(i) >= 10]
    return ips

def getGeoIP(ip):
    match = geolite2.lookup(ip)
    if match is not None:
        return match.country
    
def IPcount(ip):
    count = 0
    for i in ip:
        count += 1
    return count

def main():
    BOLD = '\033[1m'
    END = '\033[0m'
    EXTRA_TAB = '\t' + '\t'

    os.system("clear")

    file = input("Enter the file name: ")

    os.system("clear")

    print(BOLD + "Attacker Report " + END + "- " + getCurrentDate())

    print("\n")
    
    print("Count:", "\tIP:", "\t\tCountry:")

    # get the IPs from the file
    for i in getIPs(file):
        # get the number of times the IP appears in the file
        final = str(openfile(file).count(i))

        # print the IP and the number of times it appears with the country
        print(final + "\t" + i + "\t" + str(getGeoIP(i)))

    print("\n")
    print("Number of failed password attempts: ", openfile(file).count("Failed password"))
    print("Number of unique IPs: ", IPcount(getIPs(file)))
    
    

if __name__ == "__main__":
    main()