import os, sys, hashlib, base64, ftplib#, urllib.request
import requests
from xml.dom import minidom
from prettytable import PrettyTable
from contextlib import closing

from sugamya_pustakalya import SugamyaPustakalya 
from bookshare import Bookshare
# Reader is a terminal application that greets old friends warmly,
#   and remembers new friends.

def display_title_bar():
        # Clears the terminal screen, and displays a title bar.
        try:
            os.system('cls') 
        except:
            os.system('clear')
            
                         
        print("\t**********************************************")
        print("\t***  Reader - A terminal app for searching and downloading books!  ***")
        print("\t**********************************************")


def get_user_input():
        # Let users know what they can do.
        print("\n[1] Sugamya Pustakalya")
        print("[2] Bookshare")
        print("[3] Gutenberg")
        print("[4] Local Books")
        print("[q] Quit")
        return raw_input("What would you like to do? ") # change input to raw_input if using python 2.7

### MAIN PROGRAM ###

# a loop where users can choose what they'd like to do.
choice = ''
display_title_bar()

while choice != 'q':    
    
    choice = get_user_input()
    # Respond to the user's choice.
    display_title_bar()
    if choice == '1':
        sp = SugamyaPustakalya()
        sp.process_user_choice()
    elif choice == '2':
        bs = Bookshare()
        bs.process_user_choice()
    elif choice == '3':
        search_book()
    elif choice == '4':
        get_book_categories()
    elif choice == 'q':
        print("\nThanks for using Reader. Bye.")
    else:
        print("\nInvalid choice.\n")
