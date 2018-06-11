import os, sys, hashlib, base64, ftplib#, urllib.request
import requests
from xml.dom import minidom
from prettytable import PrettyTable

### Class for BOOKSHARE  ###

class Bookshare():

    KEY = 'xj4d2vektus5sdgqwtmq3tdc'
    URL = 'https://api.bookshare.org/book/'


    def display_title_bar(self):
        # Clears the terminal screen, and displays a title bar.
        try:
            os.system('cls') 
        except:
            os.system('clear')
                  
        print("\t**********************************************")
        print("\t***  Reader - A terminal app for searching and downloading books!  ***")
        print("\t**********************************************")

    def __init__(self):
        self.userid =''
        self.password =''

    def get_user_choice(self):
        # Let users know what they can do.
        print("\n\t***  BOOKSHARE  ***")
        print("\t**********************************************")

        print("\n[1] Latest books")
        print("[2] Popular books")
        print("[3] Search Books")
        print("[4] Book Categories")
        print("[5] Login")
        print("[b] Go Back")
        print("[q] Quit")
        
        return raw_input("What would you like to do? ") # change input to raw_input if using python 2.7

    def process_user_choice(self):
        choice = ''
        self.display_title_bar()

        while choice != 'b':    
            # Respond to the user's choice.
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1':
                self.get_latest_books(1)
            elif choice == '2':
                self.get_popular_books(1)
            elif choice == '3':
                self.search_book(1)
            elif choice == '4':
                self.get_book_categories(1)
            elif choice == 'q':
                print("\nThanks for using Reader. Bye.")
                sys.exit(0)
            elif choice == 'b':
                print("\nHome")
            else:
                print("\nInvalid choice.\n")
        

    def get_latest_books(self, page):
        # Get latest books from bookshare.org
        try:
            data = requests.get(self.URL + "latest/format/xml/page/" + str(page) + "?api_key=" + self.KEY, verify=False) # during production remove verify = false
        except Exception as e:
            print(e);
        if(data.status_code == 200):       
            parsedData = minidom.parseString(data.text);
            books = parsedData.getElementsByTagName('result')
            if(len(books) == 0):
                print("No books found")
            else:
                all_ids = []
                t = PrettyTable(['ID', 'AUTHOR', 'TITLE'])
                for book in books:
                    t.add_row([book.getElementsByTagName('id')[0].firstChild.nodeValue, book.getElementsByTagName('author')[0].firstChild.nodeValue, book.getElementsByTagName('title')[0].firstChild.nodeValue[:25]])
                    all_ids.append(book.getElementsByTagName('id')[0].firstChild.nodeValue)
                t.align = "l"
                print(t)
                response = ''
                while(response not in all_ids and response != 'b' and response != 'n'):
                    if(response != ''):
                        print("\nInvalid choice, try again")
                    print("\nEnter a book ID to search and download")
                    print("\nEnter n to display next page")
                    print("Enter b to go back")
                    response = raw_input("\nResponse: ")
                if(response  == 'n'):
                    self.get_latest_books(page + 1)
                elif(response != 'b'):
                    self.get_book_id(response)
        else:
            print("Error, server replied with", data.status_code)


    def get_popular_books(self, page):
        # Get popular books from bookshare.org
        try:
            data = requests.get(self.URL + "popular/format/xml?api_key=" + self.KEY, verify=False) # during production remove verify = false
        except Exception as e:
            print(e)
        if(data.status_code == 200):       
            parsedData = minidom.parseString(data.text)
            books = parsedData.getElementsByTagName('result')
            if(len(books) == 0):
                print("No books found")
            else:
                all_ids = []
                t = PrettyTable(['ID', 'AUTHOR', 'TITLE'])
                for book in books:
                    t.add_row([book.getElementsByTagName('id')[0].firstChild.nodeValue, book.getElementsByTagName('author')[0].firstChild.nodeValue, book.getElementsByTagName('title')[0].firstChild.nodeValue])
                    all_ids.append(book.getElementsByTagName('id')[0].firstChild.nodeValue)
                t.align = "l"
                print(t)
                response = ''
                while(response not in all_ids and response != 'b' and response != 'n'):
                    if(response != ''):
                        print("\nInvalid choice, try again")
                    print("\nEnter a book ID to search and download")
                    print("\nEnter n to display next page")
                    print("Enter b to go back")
                    response = raw_input("\nResponse: ")
                if(response  == 'n'):
                    self.get_latest_books(page + 1)
                elif(response != 'b'):
                    self.get_book_id(response)
        else:
            print("Error, server replied with", data.status_code)


    def get_book_categories(self, page):
        # Get popular books from bookshare.org
        try:
            data = requests.get("https://api.bookshare.org/reference/category/list/format/xml?api_key=" + self.KEY, verify=False) # during production remove verify = false
        except Exception as e:
            print(e)
        if(data.status_code == 200):       
            parsedData = minidom.parseString(data.text);
            categories = parsedData.getElementsByTagName('name')
            if(len(categories) == 0):
                print("No categories found")
            else:
                print("BOOK CATEGORIES")
                all_categories = []
                for category in categories:
                    print(category.firstChild.nodeValue)
                    all_categories.append(category.firstChild.nodeValue)
                response = ''
                while(response not in all_categories and response != 'b' and response != 'n'):
                    if(response != ''):
                        print("\nInvalid choice, try again")
                    print("\nEnter a book ID to search and download")
                    print("\nEnter n to display next page")
                    print("Enter b to go back")
                    response = raw_input("\nResponse: ")
                if(response  == 'n'):
                    self.get_latest_books(page + 1)
                elif(response != 'b'):
                    self.get_book_id(response)
        else:
            print("Error, server replied with", data.status_code)


    def category_search(self, category_name, page):
        # Get books of a particular category

        try:
            data = requests.get(self.URL + "search/category/" + category_name + "/format/xml?api_key=" + self.KEY, verify=False)
        except Exception as e:
            print(e)
        if(data.status_code == 200):
            parsedData = minidom.parseString(data.text);
            books = parsedData.getElementsByTagName('result')
            if(len(books) == 0):
                print("No books found")
            else:
                all_ids = []
                t = PrettyTable(['ID', 'AUTHOR', 'TITLE'])
                for book in books:
                    t.add_row([book.getElementsByTagName('id')[0].firstChild.nodeValue, book.getElementsByTagName('author')[0].firstChild.nodeValue, book.getElementsByTagName('title')[0].firstChild.nodeValue])
                    all_ids.append(book.getElementsByTagName('id')[0].firstChild.nodeValue)
                t.align = "l"
                print(t)
                response = ''
                while(response not in all_ids and response != 'b' and response != 'n'):
                    if(response != ''):
                        print("\nInvalid choice, try again")
                    print("\nEnter a book ID to search and download")
                    print("\nEnter n to display next page")
                    print("Enter b to go back")
                    response = raw_input("\nResponse: ")
                if(response  == 'n'):
                    self.get_latest_books(page + 1)
                elif(response != 'b'):
                    self.get_book_id(response)
        else:
            print("Error, server replied with", data.status_code)

    def search_book(self, page):
        # Search books by Title/Author from user given user input
        search = raw_input("Enter book Title/Author: ")
        try:
            data = requests.get(self.URL + "search/" + search + "/format/xml?api_key=" + self.KEY, verify=False)# during production remove verify = false
        except Exception as e:
            print(e)
        if(data.status_code == 200):       
            parsedData = minidom.parseString(data.text);
            books = parsedData.getElementsByTagName('result')
            if(len(books) == 0):
                print("No books found")
            else:
                all_ids = []
                t = PrettyTable(['ID', 'AUTHOR', 'TITLE'])
                for book in books:
                    t.add_row([book.getElementsByTagName('id')[0].firstChild.nodeValue, book.getElementsByTagName('author')[0].firstChild.nodeValue, book.getElementsByTagName('title')[0].firstChild.nodeValue])
                    all_ids.append(book.getElementsByTagName('id')[0].firstChild.nodeValue)
                t.align = "l"
                print(t)
                response = ''
                while(response not in all_ids and response != 'b' and response != 'n'):
                    if(response != ''):
                        print("\nInvalid choice, try again")
                    print("\nEnter a book ID to search and download")
                    print("\nEnter n to display next page")
                    print("Enter b to go back")
                    response = raw_input("\nResponse: ")
                if(response  == 'n'):
                    self.get_latest_books(page + 1)
                elif(response != 'b'):
                    self.get_book_id(response)
        else:
            print("Error, server replied with", data.status_code)

    def get_book_id(self, id):
        # Search a particular book by ID
        try:
            data = requests.get(self.URL + "id/" + id + "/format/xml?api_key=" + self.KEY, verify=False)# during production remove verify = false
        except Exception as e:
            print(e)
        if(data.status_code == 200):       
            parsedData = minidom.parseString(data.text);
            title = parsedData.getElementsByTagName('title')[0].firstChild.nodeValue
            author = parsedData.getElementsByTagName('author')[0].firstChild.nodeValue
            synopsis = parsedData.getElementsByTagName('brief-synopsis')[0]
            print("\nTitle: " + title)
            print("Author: " + author)
            if(len(synopsis.childNodes) != 0):
                print("Synopsis: " + synopsis.firstChild.nodeValue)
            response = ''
            while(response != 'd' and response != 'b'):
                if(response != ''):
                    print("\nInvalid choice")
                print("\n[d] To download book")
                print("[b] To go back")
                response = raw_input("Response: ")
            if(response != 'b'):
                self.book_download(id)
        else:
            print("Error, server replied with", data.status_code)

    def book_download(self, id):
        # Download a book
        try:
            m = hashlib.md5.new(self.password).digest()
            data = requests.get("https://api.bookshare.org/download/content/" + id + "/version/1/for/sidbhakar@gmail.com?api_key=" + self.KEY, verify=False)# during production remove verify = false
        except Exception as e:
            print(e)
        if(data.status_code == 200):       
            parsedData = minidom.parseString(data.text);

    def login():
        USERID = raw_input("User ID/ Email: ")
        PASSWORD = raw_input("Password: ")
