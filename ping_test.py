#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Jaden Rivera 2/3/2023

import subprocess
import os

def getDefaultGateway():
    gateway = subprocess.run(["ip", "r"], stdout=subprocess.PIPE).stdout.decode()
    gateway = gateway.split(" ")
    return gateway[2]

def testIP():
    ping = subprocess.Popen(['ping','129.21.3.17','-c','1','-W','2'],stdout=subprocess.DEVNULL)
    ping.wait()
    ping.poll()
    if ping.returncode == 0:
        print("Ping successful")
    else:
        print("Ping failed") 
    
def DefaultGatewayTest():
    ping = subprocess.run(["ping", getDefaultGateway(),'-c','1','-W','2'],stdout=subprocess.DEVNULL)
    if ping.returncode == 0:
        print("Default Gateway successful")
    else:
        print("Default Gateway unsuccessful")

def DNSTest():
    ping = subprocess.run(["ping", "www.google.com", '-c', '1'], stdout=subprocess.PIPE).stdout.decode()
    ping = ping.split(" ")
    if ping[1] == "www.google.com":
        print("DNS successful")
    else:
        print("DNS unsuccessful")


def main():
    os.system('clear')
    menu = 0
    while (menu != "5"):
        os.system('clear')
        menu = input("""Ping Test Troubleshooter\n
        Enter the number of the test you would like to run:
            1. Test for connectivity to Default Gateway
            2. Test for remote connectivity
            3. Test for DNS resolution
            4. Display gateway IP Address
            5. Exit\n""")
        if menu == "1":
            DefaultGatewayTest()
            input("Press enter to continue")
        elif menu == "2":
            testIP()
            input("Press enter to continue")
        elif menu == "3":
            DNSTest()
            input("Press enter to continue")
        elif menu == "4":
            print(getDefaultGateway())
            input("Press enter to continue")
        elif menu == "5":
            exit()
        else:
            print("Invalid input")
            input("Press enter to continue")

if __name__ == "__main__":
    main()
