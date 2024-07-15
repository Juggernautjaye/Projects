#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Jaden Rivera 3/7/2023

import os
import subprocess
from pathlib import Path
import time

"""

Shortcut Creator

"""

def getCurrentDirectory():
    
        # returns the current directory
        return Path.cwd()

def getTargetPath(targetfile):

    # returns the path of the target file
    return Path.home() / targetfile

def listsym():

    # lists all symlinks in the current directory
    sym = subprocess.run(["find", ".", "-type", "l"], stdout=subprocess.PIPE).stdout.decode()
    return sym

def findFile(targetfile):

    # current directory
    here = Path(".")

    # looks in the current directory and all subdirectories for the target file
    file = here.glob("**/" + targetfile)

    # loop through the files
    for f in file:

        # return the file if it exists
        return f

def createShortcut(targetfile):

    # create a shortcut if the file exists
    if findFile(targetfile) != None:

        # create the shortcut
        sym = subprocess.run(["ln", "-s", findFile(targetfile), targetfile + ".lnk"], stdout=subprocess.PIPE).stdout.decode()

        # return the shortcut
        return sym
    
    # if the file doesn't exist
    elif findFile(targetfile) == None:

        # create the file and then create the shortcut
        os.system("touch " + targetfile)

        # create the shortcut
        sym = subprocess.run(["ln", "-s", findFile(targetfile), targetfile + ".lnk"], stdout=subprocess.PIPE).stdout.decode()

        # return the shortcut
        return sym
    else:
        return "Shortcut creation failed"

def removeShortcut(targetfile):

    # if the shortcut doesn't exist
    if findFile(targetfile) == None:

        # return an error
        return "Shortcut does not exist"
    else:

        # unlink the file
        return os.unlink(Path.home() / (targetfile + ".lnk"))
    

def main():
    os.system("clear")
    menu = 0

    BOLD = "\033[1m"
    END = "\033[0m"

    while (menu != "5"):
        os.system("clear")

        # Display the menu
        menu = print("""\tShortcut Creator\n
        1. Create a shortcut
        2. Remove a shortcut
        3. List all shortcuts""")

        # Get the user's input
        menu = input("Enter a number (1-3) to create/remove/list shortcuts or (q/Q) to quit the program: ")

        print("\n")

        # Create a shortcut
        if menu == "1":

            # Get the target file
            targetfile = input("Enter the name of the file you would like to create a shortcut for: ")

            # Check if the user wants to create a shortcut for the file
            tmp = input("Found " + BOLD + str(findFile(targetfile)) + END + ". Is this the file you would like to create a shortcut for? (y/n): ")

            # If the user wants to create a shortcut for the file
            if tmp == "y":

                # Display a message
                print("Creating shortcut for " + targetfile + "...")

                time.sleep(3)

                # Create the shortcut
                createShortcut(targetfile)

                print("Shortcut created")
                print("\n")

            # If the user doesn't want to create a shortcut for the file
            elif tmp == "n":
                # Return to the menu
                print("\n")

        if menu == "2":
            # Get the target file
            targetfile = input("Enter the name of the file you would like to remove a shortcut for: ")

            # Check if the user wants to remove a shortcut for the file
            tmp = input("Found " + BOLD + str(findFile(targetfile)) + END + ". Is this the file you would like to remove a shortcut for? (y/n): ")

            # If the user wants to remove a shortcut for the file
            if tmp == "y":
                # Display a message
                print("Removing shortcut for " + targetfile + " ...")

                # Wait 3 seconds
                time.sleep(3)

                # Remove the shortcut
                removeShortcut(targetfile)

                print("Shortcut removed")
                print("\n")

            # If the user doesn't want to remove a shortcut for the file
            elif tmp == "n":
                # Return to the menu
                print("\n")

        if menu == "3":
            # if a shortcut is created add it to the list
            print("Your current directory is: " + str(getCurrentDirectory()) + "\n")

            # Counts the number of symbolic links created
            array = ""
            for i in listsym():
                array += i
            arr = array.count("\n")
            array = str(arr)

            print("Number of symbolic links: " + array)
            print("\n")

            # List all symbolic links
            print(BOLD + "Symbolic links:  \t Target Path:" + END + "\n")

            # Loop through the symbolic links
            list = ""
            for i in listsym():
                list += i
                list = list.join("\n")
            
            print(str(listsym()) + "\t" + str(getTargetPath(list)))

            # Print the symbolic links and their target paths
            print("\n")
            input("Press enter to continue")
        if menu == "quit" or menu == "Q" or menu == "q":
            exit()
        else:
            print("Invalid input")
            print("\n")

if __name__ == "__main__":
    main()
