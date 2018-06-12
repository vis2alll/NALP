# uncompyle6 version 3.1.2
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.13 (default, Nov 23 2017, 15:37:09) 
# [GCC 6.3.0 20170406]
# Embedded file name: /home/osboxes/Downloads/UIFramework/examples/reader.py
# Compiled at: 2018-04-24 12:27:42
from console.ui.menu_window import Menu, MenuItem
from sugamya_pustakalya import SugamyaPustakalya
from bookshare import Bookshare
from console.core.event_type import EventType
from _enums import BOOKLIST_WINDOW, LOGIN_WINDOW,DEFAULT_WINDOW

#-------------
from login import _login
from local_books import downloaded_files

class process_choice_selection():

    def __init__(self, window_name=None):
        self._event = None
        self.window_name = window_name
        self.reader_menu_lst = None
        self.lvl = 0
        self.menu_lvl=""
        self.sp=None
        self.login_lvl=""
        self.login =_login()
        self.count=0



    def choice_selection(self, _event, choice):


        self._event=_event
        app=_event.app
        
        choice = str(choice)
        if choice == '1':
            
            if self.sp==None:
                self.sp = SugamyaPustakalya(self)
                
                
#                _event.app.editor.focus(DEFAULT_WINDOW)
#                _event.current_window.buffer._text = "hellooow3"
#                _event.current_window.buffer.emit(EventType.TEXT_CHANGED)                
                
                if not self.login.login_lvl=="sp":
                    self.login.login_process(self,_event,"sp")

                                    
#                else:
#                    self.get_user_input( app,self.reader_menu_lst)
#                    app.editor.message('Invalid credentials ')
                    
#                    return
#                    self.choice_selection( self._event, choice)
                    
                    
            else:
                
                
                self.menu_lvl="1"
                
                lst = [
                         MenuItem('Latest books', '1', lambda app: self.sp_choice_selection(app, '1')),
                         MenuItem('Popular books', '2', lambda app: self.sp_choice_selection(app, '2')),
                         MenuItem('Search Books', '3', lambda app: self.sp_choice_selection(app, '3')),
                         MenuItem('Book Categories', '4', lambda app: self.sp_choice_selection(app, '4')),
                         MenuItem('Downloads', '5', lambda app: self.sp_choice_selection(app, '5')),
        #                     MenuItem('Login', '6', lambda app: self.sp_choice_selection(app, '6')),
                         MenuItem('Go Back', 'b', lambda app: self.sp_choice_selection(app, 'b')),
                         MenuItem('quits', 'q', lambda app: self.sp_choice_selection(app, 'q'))
                     ]
        
                
                if  self.login.login_lvl=="sp":
                    self.get_user_input(app,lst)
#                    if self.count==0:
#                        self.count+=1
#                        app.editor.message('loged in sugamya pustkalaya  ')

                else:
#                    self.sp=None
#                    self.login =_login()
                    app.editor.message( 'ELSE,READER in sp: ' )
        
        elif choice == '2':
            self.menu_lvl="2"
            app.editor.message('bookshare ')
            bs = Bookshare()
            bs.process_user_choice()
                
        elif choice == '3':
            self.menu_lvl="3"
            app.editor.message('gutenberg ')
        elif choice == '4':
            self.menu_lvl="4"
            app.editor.message('local books ')
        elif choice == 'q':
            self.menu_lvl="1"
            try:
                self.sp=None
                self.login =_login()
#                self._event.current_window.buffer._files=[[""]]
                self._event.current_window.buffer.reset()
#                self._event.current_window.buffer._files=downloaded_files()
                
            except:
                pass
#            app.editor.message('\nThanks for using Reader. Bye.')
        else:
            app.editor.message('\nInvalid choice.\n ')


    def sp_choice_selection(self, app, choice):
        if choice == '1':
            self.menu_lvl="1-1"
#            self.sp = SugamyaPustakalya(self)
#            app.editor.message("fetching books...")
            self.sp.book_repo=[]
            self.sp.latest_page=1
            self.sp.get_latest_books()
            
        elif choice == '2':
            self.menu_lvl="1-2"
#            app.editor.message('Popular books ')
            self.sp.book_repo=[]
            self.sp.latest_page=1
            self.sp.get_popular_books()
            
        elif choice == '3':
            self.menu_lvl="1-3"
#            app.editor.message('Search Books')
            self.sp.book_repo=[]
            self.sp.latest_page=1
            self.sp.get_search_input()
            
        elif choice == '4':
            self.menu_lvl="1-4"
#            app.editor.message('Book Categories')
            self.sp.book_repo=[]
            self.sp.latest_page=1
            self.sp.get_book_categories()
            
        elif choice == '5':
            self.menu_lvl="1-5"
#            app.editor.message('Downloads ')
            self.sp.book_repo=[]
            self.sp.latest_page=1
            self.all_urls = {}
            self.sp.get_requested_books()
#        elif choice == '6':
#            self.menu_lvl="1-6"
#            app.editor.message('Login ')
        elif choice == 'b':
            self.menu_lvl="1-b"
    #                                    app.editor.message('Go Back ')
            self.get_user_input( app,self.reader_menu_lst)
        elif choice == 'q':
            self.menu_lvl="1"
            
            try:
                self.sp=None
                self.login =_login()
#                self._event.current_window.buffer._files=[[""]]
                self._event.current_window.buffer.reset()
#                self._event.current_window.buffer._files=downloaded_files()
            except:
                pass
#            print "hello"
#            self.menu_lvl="q"
#            app.editor.message('\nThanks for using Reader. Bye.')
        else:
            app.editor.message('\nInvalid choice.\n ')


    def get_user_input(self, app,lst):
        if self.lvl == 0:
            self.reader_menu_lst = lst
            self.lvl += 1

        app.editor.create_menu(self.window_name,lst)

