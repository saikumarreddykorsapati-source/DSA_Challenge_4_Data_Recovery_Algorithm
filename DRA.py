import pyminizip
import os
from utils import folderscreator as fc, func
import sys

def main():

    print("\nChoose What action to perform : \n\n 1. Backup Single File \n 2. Recover Files \n 3. Backup Multiple Files \n\n --> Enter 0 to Exit \n")
								
    while True:
        try:
            action = int(input("Enter your option here =  "))
        except ValueError:
            print("Sorry, I didn't understand that.,press 0 to exit.\n")
            continue
        
        if action ==1:
            fc.singleZip()

        elif action ==2:
            print("Enter Input_File_name :" )
            fc.recZip()

        elif action ==3:
            print("Enter Input_Folder_name :" )
            fc.mulZip()
            
        elif action == 0:
            sys.exit("\n-> Successfully Exited from program, Thank You...")

        else:
            print("\nSelect any one option either 1 or 2, otherwise enter 0 to exit\n")
            continue

main()
