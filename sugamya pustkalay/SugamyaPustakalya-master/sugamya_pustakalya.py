import os, sys, hashlib, base64, ftplib#, asyncio#, urllib.request
import requests
from xml.dom import minidom
from prettytable import PrettyTable

#requests.get('http://example.org', proxies=self.proxies)

class SugamyaPustakalya():
    
    KEY = 'D72551A2C3319E892DF355AAB1C55FCEEAE91A2236C39B931513155440537'
    URL = 'https://library.daisyindia.org/NALP/rest/NALPAPIService/getNALPData/'


    proxies = {
      'http': 'http://10.10.78.21:3128',
      'https': 'http://10.10.78.21:3128',
    }


    ### FUNCTIONS ###
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
        self.userid = ''
        self.password = ''
        
    def get_user_choice(self):
        # Let users know what they can do.

        print("\n\t***  SUGAMYA PUSTAKALYA  ***")
        print("\t**********************************************")

        print("\n[1] Latest books")
        print("[2] Popular books")
        print("[3] Search Books")
        print("[4] Book Categories")
        print("[5] Downloads")
        print("[6] Login")
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
            elif choice == '5':
                self.download_books()
            elif choice == 'q':
                print("\nThanks for using Reader. Bye.")
                sys.exit(0)
            elif choice == 'b':
                print("\nHome")
            else:
                print("\nInvalid choice.\n")
        
    # async def make_request(self, type, page):
    #     try:
    #         return requests.get(self.URL + type + '/page/' + page + '/limit/20/format/JSON?API_key=' + self.KEY, verify=False) # during production remove verify = false
    #     except Exception as e:
    #         print(e);


    def get_latest_books(self, page):
        # Get latest books from Sugamya Pustakalya
        try:
            # loop = asyncio.get_event_loop()
            # data = loop.run_until_complete(self.make_request('latest', str(page)))
            try:
                data = requests.get(self.URL + 'latest/page/' + str(page) +\
                                    '/limit/20/format/JSON?API_key=' + self.KEY,\
                                    verify=False)
            except:
                data = requests.get(self.URL + 'latest/page/' + str(page) +\
                    '/limit/20/format/JSON?API_key=' + self.KEY, proxies=self.proxies,\
                    verify=False)
                
        except Exception as e:
            print(e);
                 
                 
        if(data.status_code == 200):
            
            parsedData = minidom.parseString(data.text);
            books = parsedData.getElementsByTagName('result')
            if(len(books) == 0):
                print("No books found")
            else:
                all_ids = []
                t = PrettyTable(['AUTHOR', 'BRIEF-SYNOPSIS', 'DOWNLOAD-FORMAT','DTBOOK-SIZE', 'FREELY-AVAILABLE', 'ID', 'ISBN13', 'TITLE'])
                
                for book in books:
                    
                    row=[]
                    for child in book.childNodes:
                        
                      if(len(child.childNodes)!=0):
                        row.append(child.firstChild.nodeValue[:20])
                        
                      else:
                        row.append('NA')
         #--------------------------------------------#               
                    while len(t.field_names)!=len(row):
                        row.append('NA')
                    print row
         #--------------------------------------------#
         
                    t.add_row(row)
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
        # Get popular books from Sugamya Pustakalya
        try:
            
            try:
                data = requests.get(self.URL + "popularbooks/noOfTimesDelivered/1/\
                    startDate/2017-01-01/endDate/2017-12-15/page/1/limit/17/format/\
                    xml?API_key=" + self.KEY, verify=False) # during production remove verify = false
         
            except:
                data = requests.get(self.URL + "popularbooks/noOfTimesDelivered/1/\
                    startDate/2017-01-01/endDate/2017-12-15/page/1/limit/17/format/\
                    xml?API_key=" + self.KEY, proxies=self.proxies, verify=False) # during production remove verify = false
                         

        
        except Exception as e:
            print(e)
            
        if(data.status_code == 200):       
            parsedData = minidom.parseString(data.text);
            books = parsedData.getElementsByTagName('result')
            if(len(books) == 0):
                print("No books found")
            else:
                all_ids = []
                t = PrettyTable(['AUTHOR', 'BRIEF-SYNOPSIS', 'DOWNLOAD-FORMAT','DTBOOK-SIZE', 'FREELY-AVAILABLE', 'ID', 'ISBN13', 'TITLE'])
                
                for book in books:
                    row=[]
                    for child in book.childNodes:
                      if(len(child.childNodes)!=0):
                        row.append(child.firstChild.nodeValue[:20])
                      else:
                        row.append('NA')
                    t.add_row(row)
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
        # Get popular books from Sugamya Pustakalya
        
        try:
            
            try:
                data = requests.get(self.URL + "categorylist/page/1/limit/52/format/\
                                    xml?API_key=" + self.KEY, verify=False) # during production remove verify = false

            except:
                data = requests.get(self.URL + "categorylist/page/1/limit/52/format/\
                                    xml?API_key=" + self.KEY, proxies=self.proxies, verify=False) # during production remove verify = false
        
        except Exception as e:
            print(e)        
 
    
        if(data.status_code == 200):       
            parsedData = minidom.parseString(data.text);
            categories = parsedData.getElementsByTagName('title')
            if(len(categories) == 0):
                print("No books found")
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
            
            try:
                data = requests.get(self.URL + "category/" + category_name + "/page/1/\
                                    limit/52/format/xml?API_key=" + self.KEY, verify=False)
            
            except:
                data = requests.get(self.URL + "category/" + category_name + "/page/1/\
                                    limit/52/format/xml?API_key=" + self.KEY\
                                    , proxies=self.proxies, verify=False)
            
        except Exception as e:
            print(e) 

 
        if(data.status_code == 200):
            parsedData = minidom.parseString(data.text);
            books = parsedData.getElementsByTagName('result')
            if(len(books) == 0):
                print("No books found")
            else:
                all_ids = []
                t = PrettyTable(['AUTHOR', 'BRIEF-SYNOPSIS', 'DOWNLOAD-FORMAT','DTBOOK-SIZE', 'FREELY-AVAILABLE', 'ID', 'ISBN13', 'TITLE'])
                
                for book in books:
                    row=[]
                    for child in book.childNodes:
                      if(len(child.childNodes)!=0):
                        row.append(child.firstChild.nodeValue[:20])
                      else:
                        row.append('NA')
                    t.add_row(row)
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
            
            try:
                data = requests.get(self.URL + "authortitle/" + search + "/page/1/\
                                limit/25/format/xml?API_key=" + self.KEY, verify=False) # during production remove verify = false
         
            except:
                data = requests.get(self.URL + "authortitle/" + search + "/page/1/\
                                limit/25/format/xml?API_key=" + self.KEY,\
                                 proxies=self.proxies,verify=False) # during production remove verify = false
#        , proxies=self.proxies
        except Exception as e:
            print(e)         

            
        if(data.status_code == 200):       
            parsedData = minidom.parseString(data.text);
            books = parsedData.getElementsByTagName('result')
            if(len(books) == 0):
                print("No books found")
            else:
                all_ids = []
                t = PrettyTable(['AUTHOR', 'BRIEF-SYNOPSIS', 'DTBOOK-SIZE','FREELY-AVAILABLE', 'ID', 'ISBN13', 'PUBLISHER', 'TITLE'])
                
                for book in books:
                    row=[]
                    for child in book.childNodes:
                      if(len(child.childNodes)!=0):
                        row.append(child.firstChild.nodeValue[:20])
                      else:
                        row.append('NA')
                    t.add_row(row)
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
            
            try:
                data = requests.get(self.URL + "id/" + id + "/page/1/limit/25/format/\
                                xml?API_key=" + self.KEY, verify=False)# during production remove verify = false
 
            except:
                data = requests.get(self.URL + "id/" + id + "/page/1/limit/25/format/\
                                xml?API_key=" + self.KEY, proxies=self.proxies, verify=False)# during production remove verify = false
        
#        , proxies=self.proxies
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
                self.book_download_request(id)
        else:
            print("Error, server replied with", data.status_code)

    def book_download_request(self, id):
        # Download a book
        # if(self.userid == '' or self.password == ''):
        #     self.login()
        try:
            authString = "26353" + ':' "9m85twwz"
            encoded = base64.b64encode(bytearray(authString.encode())).decode()
            print(id)
            headers = {'Authorization': 'Basic ' + encoded, "page" : "1", "limit" : "1", "format" : "xml", "API_key" : self.KEY, "bookId" : id, "formatId" : '6'}
            
            try:
                data = requests.post("https://library.daisyindia.org/NALP/rest/\
                                 NALPAPIService/raiseBookDownloadRequest", headers = headers, \
                                 verify=False)
            except:
                data = requests.post("https://library.daisyindia.org/NALP/rest/\
                                 NALPAPIService/raiseBookDownloadRequest", headers = headers, \
                                 proxies=self.proxies,verify=False)
#        , proxies=self.proxies

        except Exception as e:
            print(e)

        if(data.status_code == 200):
            parsedData = minidom.parseString(data.text)
            message = parsedData.getElementsByTagName('message')[0]
            print(message.firstChild.nodeValue)
        else:
            print("Error, server replied with", data.status_code) 

    def download_books(self):
        # download books that are ready for downloading
        try:
            authString = "26353" + ':' "9m85twwz"
            encoded = base64.b64encode(bytearray(authString.encode())).decode()
            print(id)
            headers = {'Authorization': 'Basic ' + encoded, "page" : "1", "limit" : "10", "format" : "xml", "API_key" : self.KEY}
            try:
                data = requests.post("https://library.daisyindia.org/NALP/rest/\
                                     NALPAPIService/fetchUserDownloadRequests", headers = headers,\
                                     verify=False)
            except:
                data = requests.post("https://library.daisyindia.org/NALP/rest/\
                                     NALPAPIService/fetchUserDownloadRequests", headers = headers,\
                                      proxies=self.proxies,verify=False)
#        , proxies=self.proxies
            
        except Exception as e:
            print(e)

        if(data.status_code == 200):
            parsedData = minidom.parseString(data.text)
            print(parsedData.toxml())
            count = 1
            all_urls = {}
            books = parsedData.getElementsByTagName('result')
            t = PrettyTable(['ID', 'TITLE', 'STATUS'])
            for book in books:
                status = book.getElementsByTagName('available-to-download')[0].firstChild.nodeValue
                t.add_row([count, book.getElementsByTagName('title')[0].firstChild.nodeValue, status])
                if(status == 'Available for Download'):
                    all_urls[str(count)] = book.getElementsByTagName('downloadUrl')[0].firstChild.nodeValue
                count += 1
            t.align = "l"
            print(t)
            response = ''
            while(response not in all_urls and response != 'b'):
                if(response != ''):
                    print("\nInvalid choice")
                print("\nEnter Book ID to download an available book")
                print("[b] To go back")
                response = raw_input("Response: ")

            if(response != 'b'):
                path = ''
                url = all_urls[response].split('/')
                host = url[2].split(':')[0]
                port = url[2].split(':')[1]
                filename = url[4]
                ftp = ftplib.FTP(host) 
                ftp.login("26353", "9m85twwz") 
                ftp.cwd(path)
                ftp.retrbinary("RETR " + url[3] + "/" + url[4], open(filename, 'wb').write)
                ftp.quit()
                # proxy = urllib.request.ProxyHandler({'http': 'proxy22.iitd.ac.in:3128'})
                # opener = urllib.request.build_opener(proxy)
                # urllib.request.install_opener(opener)
                # with closing(urllib.request.urlopen(all_urls[response])) as r:
                #     with open('file', 'wb') as f:
                #         shutil.copyfileobj(r, f)
        else:
            print("Error, server replied with", data.status_code)

    def login(self):
        USERID = raw_input("User ID/ Email: ")
        PASSWORD = raw_input("Password: ")


