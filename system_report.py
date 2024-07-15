#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Jaden Rivera 2/19/2023

import os
import platform
import subprocess  

def getCurrentDate():
    date = subprocess.run(["date"], stdout=subprocess.PIPE).stdout.decode()
    date = date.split()
    return date[5] + " " + date[2] + " " + date[1]

def getHostname():
    # Returns the hostname of the machine
    return platform.node()

def getDomain():
    domain = subprocess.run(["hostname", "-A"], stdout=subprocess.PIPE).stdout.decode() # Returns the domain of the machine
    domain = domain.split(" ") # Splits the string into a list
    return domain[0] 

def getIP():
    ip = subprocess.run(["hostname", "-I"], stdout=subprocess.PIPE).stdout.decode() # Returns the IP address of the machine
    ip = ip.split(" ")
    return ip[0] 

def getDefaultGateway():
    gateway = subprocess.run(["ip", "r"], stdout=subprocess.PIPE).stdout.decode() # Returns the default gateway of the machine
    gateway = gateway.split(" ")
    return gateway[2] 

def getNetworkMask():
    mask = subprocess.run(["ifconfig"], stdout=subprocess.PIPE).stdout.decode() # Returns network information of the machine
    mask = mask.split(" ")
    return mask[16] # Returns the network mask

def getDNS1():
    dns = subprocess.run(["cat", "/etc/resolv.conf"], stdout=subprocess.PIPE).stdout.decode() # Returns the DNS servers of the machine
    dns = dns.split() 
    return dns[7] # Returns the first DNS server

def getDNS2():
    dns = subprocess.run(["cat", "/etc/resolv.conf"], stdout=subprocess.PIPE).stdout.decode() # Returns the DNS servers of the machine
    dns = dns.split()
    return dns[9] # Returns the second DNS server

def getOS():
    return platform.system() # Returns the OS of the machine

def getOSVersion():
    version = subprocess.run(["cat", "/etc/os-release"], stdout=subprocess.PIPE).stdout.decode() # Returns the OS information of the machine
    version = version.split() and version.split("=") and version.split('"') # Splits the string by spaces, equal signs, and double quotes
    return version[3] # Returns the OS version

def getKernelVersion():
    version = subprocess.run(["uname", "-r"], stdout=subprocess.PIPE).stdout.decode() # Returns the kernel version of the machine
    return version

def getHardDriveCapacity():
    capacity = subprocess.run(["df", "-h", "/"], stdout=subprocess.PIPE).stdout.decode() # Returns the hard drive information of the machine
    capacity = capacity.split()
    return capacity[8] # Returns the hard drive capacity

def getAvailableHardDriveSpace():
    space = subprocess.run(["df", "-h", "/"], stdout=subprocess.PIPE).stdout.decode() # Returns the hard drive information of the machine
    space = space.split()
    return space[10] # Returns the available hard drive space

def getCPUModel():
    cpu = subprocess.run(["cat", "/proc/cpuinfo"], stdout=subprocess.PIPE).stdout.decode() # Returns the CPU information of the machine
    cpu = cpu.split(" ")
    return cpu[7] + " " + cpu[8] + " " + cpu[9] # Returns the CPU model

def getNumberofProcessors():
    processors = subprocess.run(["cat", "/proc/cpuinfo"], stdout=subprocess.PIPE).stdout.decode() # Returns the CPU information of the machine
    processors = processors.split() 
    return processors[2] # Returns the number of processors

def getNumberofCPUCores():
    cores = subprocess.run(["cat", "/proc/cpuinfo"], stdout=subprocess.PIPE).stdout.decode() # Returns the CPU information of the machine
    cores = cores.split()
    return cores[52] # Returns the number of CPU cores

def getTotalRAM():
    ram = subprocess.run(["cat", "/proc/meminfo"], stdout=subprocess.PIPE).stdout.decode() # Returns the RAM information of the machine
    ram = ram.split() 
    return ram[1] + " " + ram[2] # Returns the total RAM

def getAvailableRAM():
    ram = subprocess.run(["cat", "/proc/meminfo"], stdout=subprocess.PIPE).stdout.decode() # Returns the RAM information of the machine
    ram = ram.split()
    return ram[7] + " " + ram[8] # Returns the available RAM


def main():
    BOLD = '\033[1m'
    END = '\033[0m'
    EXTRA_TAB = '\t' + '\t'

    # Clears the screen
    os.system('clear')
    os.system('clear')
    # Prints the system report
    print("\t System Report - " + getCurrentDate())
    print(" ")

    print(BOLD + "Device Information" + END)
    print("Hostname: " + EXTRA_TAB + getHostname())
    print("Domain: " + EXTRA_TAB + getDomain())
    print(" ")

    print(BOLD + "Network Information" + END)
    print("IP Address: " + EXTRA_TAB + getIP())
    print("Default Gateway: " + "\t" + getDefaultGateway())
    print("Network Mask: " + EXTRA_TAB + getNetworkMask())
    print("DNS 1: " + EXTRA_TAB + "\t" + getDNS1())
    print("DNS 2: " + EXTRA_TAB + "\t" + getDNS2())
    print(" ")

    print(BOLD + "OS Information" + END)
    print("OS: " + EXTRA_TAB + "\t" + getOS())
    print("OS Version: " + EXTRA_TAB + getOSVersion())
    print("Kernel Version: " + "\t" + getKernelVersion())

    print(BOLD + "Storage Information" + END)
    print("Hard Drive Capacity: " + "\t" + getHardDriveCapacity())
    print("Available Space: " + "\t" + getAvailableHardDriveSpace())
    print(" ")

    print(BOLD + "Processor Information" + END)
    print("CPU Model: " + EXTRA_TAB + getCPUModel())
    print("Number of Processors: " + "\t" + getNumberofProcessors())
    print("Number of CPU Cores: " + "\t" + getNumberofCPUCores())
    print(" ")

    print(BOLD + "Memory Information" + END)
    print("Total RAM: " + EXTRA_TAB + getTotalRAM())
    print("Available RAM: " + EXTRA_TAB + getAvailableRAM())

if __name__ == "__main__":
    main()
