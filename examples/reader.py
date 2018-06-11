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


class process_choice_selection():

    def __init__(self, _event, window_name):
        self._event = _event
        self.window_name = window_name
        self.reader_menu_lst = None
        self.lvl = 0
        return

    def choice_selection(self, app, choice):
        choice = str(choice)
        if choice == '1':
#            app.editor.message('sugamya pustkalaya ')
            
            lst = [
             MenuItem('Latest books', '1', lambda app: self.sp_choice_selection(app, '1')),
             MenuItem('Popular books', '2', lambda app: self.sp_choice_selection(app, '2')),
             MenuItem('Search Books', '3', lambda app: self.sp_choice_selection(app, '3')),
             MenuItem('Book Categories', '4', lambda app: self.sp_choice_selection(app, '4')),
             MenuItem('Downloads', '5', lambda app: self.sp_choice_selection(app, '5')),
             MenuItem('Login', '6', lambda app: self.sp_choice_selection(app, '6')),
             MenuItem('Go Back', 'b', lambda app: self.sp_choice_selection(app, 'b')),
             MenuItem('quits', 'q', lambda app: self.sp_choice_selection(app, 'q'))
                 ]

            
            self.window_name="SUGAMYAPUSTKALAYA"
            self.get_user_input(lst)
            
        else:
            if choice == '2':
                app.editor.message('bookshare ')
                bs = Bookshare()
                bs.process_user_choice()
            else:
                if choice == '3':
                    app.editor.message('gutenberg ')
                else:
                    if choice == '4':
                        app.editor.message('local books ')
                    else:
                        if choice == 'q':
                            app.editor.message('%s ' % '\nThanks for using Reader. Bye.')
                        else:
                            app.editor.message('\nInvalid choice.\n ')


    def sp_choice_selection(self, app, choice):
        if choice == '1':
            sp = SugamyaPustakalya(self)
            sp.get_latest_books()
            
        else:
            if choice == '2':
                app.editor.message('Popular books ')
            else:
                if choice == '3':
                    app.editor.message('Search Books')
                else:
                    if choice == '4':
                        app.editor.message('Book Categories')
                    else:
                        if choice == '5':
                            app.editor.message('Downloads ')
                        else:
                            if choice == '6':
                                app.editor.message('Login ')
                            else:
                                if choice == 'b':
#                                    app.editor.message('Go Back ')
                                    self.get_user_input( self.reader_menu_lst)
                                else:
                                    if choice == 'q':
                                        app.editor.message('\nThanks for using Reader. Bye.')
                                    else:
                                        app.editor.message('\nInvalid choice.\n ')


    def get_user_input(self, lst):
        if self.lvl == 0:
            self.reader_menu_lst = lst
            self.lvl += 1

        self._event.app.editor.create_menu(self.window_name,lst)


#######################################################################################################
#        self._event.app.editor.find_window("BOOKLIST_WINDOW").buffer="kakakak"
#        self._event.app.editor.find_window("BOOKLIST_WINDOW").emit(EventType.TEXT_CHANGED)
#        search_window = str(self._event.app.editor.find_window("BOOKLIST_WINDOW").buffer)
##        c_win=str(self._event.app.editor._windows)
#        self._event.app.editor.message("search_window")
 
#        return        
