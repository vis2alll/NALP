#"26353" "9m85twwz"

from console.ui.menu_window import Menu, MenuItem
from sugamya_pustakalya import SugamyaPustakalya
from bookshare import Bookshare
from console.core.event_type import EventType
from _enums import BOOKLIST_WINDOW, LOGIN_WINDOW,DEFAULT_WINDOW

class _login():
    def __init__(self):
        self.userid=""
        self.password=""
        self.login_lvl=None
        self.event=None
        self.pcs=None
        self.login_status=0
        self.login_tag=""



        

    def _on_password_ok(self,*args):
        password = str(args[-1])
        if " " in password:
            self.get_password()
            
        else:
            self.password="9m85twwz"
#            self.password=password
#            self.event.app.editor.error(str(self.pcs.sp.check_credentials(self.userid,self.password)))

            response=self.pcs.sp.check_credentials(self.userid,self.password)
            
            if response==1:
                self.login_status=1
                self.login_lvl=self.login_tag
                
#                self.event.app.editor.focus(BOOKLIST_WINDOW)
#                self.event.current_window.buffer._files = [["hellooow3"]]
#                self.event.current_window.buffer.emit(EventType.TEXT_CHANGED) 
                
                
                choice="1" #sugamPustakalya 
                self.pcs.choice_selection( self.event, choice)
                
            else:
                self.pcs.sp=None
                self.pcs.get_user_input( self.event.app,self.pcs.reader_menu_lst)
                self.event.app.editor.error(str(response))

               
 
    def get_password(self):
        self.event.app.editor.input('password:',
                    "PROMPT_WINDOW",
                    on_ok_handler = self._on_password_ok)
    
    def _on_userid_ok(self,*args):
        
        
        
        userid = str(args[-1])
        if " " in userid:
            self.login_process(self.pcs,self.event)
        else:
            self.userid="26353"
#            self.userid=userid
            self.get_password()

        

        
    def login_process(self,pcs,event,login_tag):
        self.login_status=0
        self.login_tag=login_tag
        self.pcs=pcs
        self.event=event
        event.app.editor.input('userid:',
                "PROMPT_WINDOW",
                on_ok_handler = self._on_userid_ok)     

 

            