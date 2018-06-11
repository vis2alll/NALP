import sys
#sys.path.append('/home/cdh/vishal_iit/UIFramework')
#sys.path.append('/home/osboxes/Downloads/UIFramework')
sys.path.append("/home/suman/vishal RBD/sugam_pustkalay/vishal_iit/UIFramework")
import console
#import curses

from console.core.keybinding import Registry, MergedRegistry
from console.core.keys import Keys
from console.enums import DEFAULT_WINDOW
from console.core.filters.basic import HasFocus, HasBufferState, Readonly, WindowType, SupportsRichText, IsBlockType, HasPropertyOn
from console.core.filters.base import OrFilter, AndFilter, NotFilter
from console.ui.window import EditorWindow
from console.ui.menu_window import Menu, MenuItem
from console.core.buffer_base import BufferBase

#------------------------------------------------------
from reader_buffer import ReaderBuffer
from login_buffer import LoginBuffer
from sugamya_pustakalya import SugamyaPustakalya as sp
from console.core.event_type import EventType
from _enums import BOOKLIST_WINDOW, LOGIN_WINDOW

class BookWindow(EditorWindow):
    pass
 
pcs_status=False
#class dummy():
#    def __init__(self):
#        self.menu_lvl=""
#
#pcs=dummy()   

def load_custom_binding():
    registry = Registry(EditorWindow)
    handle = registry.add_binding

    window_name ="MENU_LIST"
    from reader import process_choice_selection
    pcs=process_choice_selection(window_name)

    @handle(Keys.AltM)
    def _(e):
        # current_window = e.current_window
        # current_window = e.app.editor.current_window

        e.app.editor.message('message demo')

    @handle(Keys.AltE)
    def _(e):
        e.app.editor.error('error message demo')

    @handle(Keys.AltC)
    def _(e):
        def _on_yes(e):
            e.app.editor.message('you pressed yes')

        def _on_no(e):
            e.app.editor.message('you pressed no')

        e.app.editor.confirm('confirm?', on_yes_handler = _on_yes, on_no_handler = _on_no)

    def search_from_top():
        print "pass as d;lf"
 


    @handle(Keys.ControlH)      # change highlighting bold/italic/underline
    def _(event):
#        global pcs
####################################        
#        event.app.editor.focus(DEFAULT_WINDOW) #BOOKLIST_WINDOW
#
# 
#        event.app.editor.confirm(('search from top?' if
#            not 0 else
#            'search from bottom?'), search_from_top, None)
           
        #-------------main menu---------------#   
        try:
            from login import _login
            pcs.sp=None
            pcs.login =_login()
        except:
            pass
        
        lst=[
                    MenuItem('sugamya pustkalaya','1', lambda app: pcs.choice_selection(event,"1")),
                    MenuItem('bookshare','2', lambda app: pcs.choice_selection(event,"2")),
                    MenuItem('gutenberg','3', lambda app: pcs.choice_selection(event,"3")),
                    MenuItem('local books','4', lambda app: pcs.choice_selection(event,"4")),
                    MenuItem('quits','q', lambda app: pcs.choice_selection(event,"q")),
                        ]

#        event.app.editor.error(str(type( event))) 
        pcs.get_user_input(event.app,lst)
        #------------------------------------------------

##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#
#    booklist_window_has_focus = HasFocus(BOOKLIST_WINDOW)
#    default_window_has_focus = HasFocus(DEFAULT_WINDOW)
#    
#    @handle(Keys.Enter , filter=booklist_window_has_focus)
#    def _(event):
#        event.app.editor.message("overwrite bindings Keys.Right")


##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    

    @handle(Keys.Delete)
    def _(event):
        try:
            event.current_window.buffer.delete()
        except Exception as e:
            event.app.editor.error('unknown error %r' % e)


            
            
    @handle(Keys.Left)
    def _(event):
        
        try:
            if event.current_window.buffer._files==[]:
                event.app.editor.error('No book found')
            else:
                event.current_window.buffer.cursor_left()

        except Exception as e:
            event.app.editor.error('unable to navigate %r' % e)

    @handle(Keys.Right)
    def _(event):
        try:
            if event.current_window.buffer._files==[]:
                event.app.editor.error('No book found')
            else: 
                event.current_window.buffer.cursor_right()

        except Exception as e:
            event.app.editor.error('unable to navigate %r' % e)

#    def has_next_page():
#        if SugamyaPustakalya.pcs.menu_lvl=="11" :#and ReaderBuffer.lvl ==len(ReaderBuffer._files)-1:
#            event.app.editor.error('PCS DFI')
##                    SugamyaPustakalya.latest_page+=1
#                    SugamyaPustakalya.get_latest_books()

        


    @handle(Keys.Up)
    def _(event):
        try:
            if event.current_window.buffer._files==[]:
                event.app.editor.error('No book found')
            else:
                event.current_window.buffer.cursor_up()
        except Exception as e:
            event.app.editor.error('unable to navigate %r' % e)


    @handle(Keys.Down)
    def _(event):

        try:
            if event.current_window.buffer._files==[]:
                event.app.editor.error('No book found')
                
            else:
                event.current_window.buffer.cursor_down()
 
        except Exception as e:
            event.app.editor.error('unable to navigate  %r ' % e)

    def _search_book_id(*args):
        event=args[0]
#        event.app.editor.error(str( args)) 
        book_id=str(args[-1])
        
        if book_id=="" or ' ' in book_id :
            get_book_id(event)
            
        try:
            pcs.sp.get_book_id(book_id)
            pcs.menu_lvl="1-1-id"
     
        except IndexError:
                    event.app.editor.message('Book not Found')
        except Exception as e:
                    event.app.editor.error(' %r ' % e) 

        
    
    def get_book_id(event):
        event.app.editor.input('search input:',
            "PROMPT_WINDOW",
            on_ok_handler = _search_book_id)


    @handle(Keys.ControlF)
    def _(event):
#        global pcs
        if  not pcs.sp==None and pcs.menu_lvl=="1-1":
            get_book_id(event)
            
         
        
    @handle(Keys.ControlR)
    def _(event):
#        global pcs
        if  not pcs.sp==None and pcs.menu_lvl in ["1-1", "1-2", "1-3","1-4-b"]:
            
            try:
                lvl=pcs._event.current_window.buffer.lvl
                book_id=pcs.sp.book_repo[lvl][-1]
                pcs.sp.book_download_request(book_id)
     
            except Exception as e:
                    event.app.editor.error(' %r ' % e) 
                
#        elif  not pcs.sp==None and pcs.menu_lvl=="1-1-id":
#            
#            import os 
#            os.system('clear')
#            try:
#                book_id=pcs.sp.book_repo[0][-1]
#                pcs.sp.book_download_request(book_id)
#     
#            except Exception as e:
#                    event.app.editor.error(' %r ' % e)        


    @handle(Keys.ControlB)
    def _(event):
#        global pcs
#        if  not pcs.sp==None and (pcs.menu_lvl=="1-1" or "1-2" or "1-5"):
        if  not pcs.sp==None and pcs.menu_lvl in ["1-1", "1-2", "1-3", "1-4", "1-4-b", "1-5"]:
            
            try:
                pcs._event.current_window.buffer.reset()
                choice="1"
                pcs.choice_selection(event, choice)
     
            except Exception as e:
                    event.app.editor.error(' %r ' % e) 


    @handle(Keys.ControlN)
    def _(event):
#        global pcs
#        if  not pcs.sp==None and (pcs.menu_lvl=="1-1" or "1-2" or "1-5"):
        if  not pcs.sp==None and pcs.menu_lvl in ["1-1", "1-2", "1-3", "1-4", "1-4-b","1-5"]:
            try:
                lvl=len(pcs.sp.book_repo)

                if pcs.menu_lvl=="1-1":
                    pcs.sp.get_latest_books()

                elif pcs.menu_lvl=="1-2":
                    pcs.sp.get_popular_books()

                elif pcs.menu_lvl=="1-3":
                    pcs.sp.search_book()
                    
                elif pcs.menu_lvl=="1-4":
                    pcs.sp.get_book_categories()

                elif pcs.menu_lvl=="1-4-b":
                    pcs.sp.category_book_search( pcs.sp.category_name)
                
                elif pcs.menu_lvl=="1-5":
                    pcs.sp.get_requested_books()
                    

                    
                    

                try:
                    repo_length=len(pcs.sp.book_repo)
                    if not lvl==repo_length:
                        pcs._event.current_window.buffer.lvl=lvl
                        pcs._event.current_window.buffer.index=0
                        pcs._event.current_window.buffer.emit(EventType.TEXT_CHANGED)
                except:
                    pass
                
            except Exception as e:
                    event.app.editor.error(' %r ' % e) 


    @handle(Keys.ControlD)
    def _(event):
#        global pcs
#        if  not pcs.sp==None and (pcs.menu_lvl=="1-1" or "1-2" or "1-5"):
        if  not pcs.sp==None and pcs.menu_lvl in ["1-5"]:

            try:
                lvl=pcs._event.current_window.buffer.lvl
                book_id=pcs.sp.book_repo[lvl][0]
                pcs.sp.download_book(book_id)
     
            except Exception as e:
                    event.app.editor.error(' %r ' % e) 




    @handle(Keys.Enter)
    def _(event):
#        global pcs
#        if  not pcs.sp==None and (pcs.menu_lvl=="1-1" or "1-2" or "1-5"):
        if  not pcs.sp==None and pcs.menu_lvl in ["1-4"]:
            pcs.sp.latest_page=1
            
            try:
                pcs.sp.book_repo_temp=pcs.sp.book_repo
                lvl=pcs._event.current_window.buffer.lvl
                pcs.sp.category_name=pcs.sp.book_repo[lvl][-1]
                pcs.sp.book_repo=[] 
                pcs.sp.category_book_search(pcs.sp.category_name)


            except Exception as e:
                    event.app.editor.error(' %r ' % e) 
                    
        else:
            try:
                event.current_window.buffer.enter()
            except Exception as e:
                event.app.editor.error('unknown error %r' % e)






    return registry




def main(stdscr, args):
    
    top, left = stdscr.getbegyx() # top left coordinate of the screen
    rows, cols = stdscr.getmaxyx() # size of screen

    console.init(stdscr)

    from console.logger import logger

    _logger = logger('main')


    try:
        from os import path
        import traceback
        from console.application import Application
        from console.ui.editor import Editor
        from console.ui.window import Window,EditorWindow,PromptWindow
        from console.enums import DEFAULT_WINDOW
        from console.config import PROMPT_HEIGHT
        from console.core.prompt_buffer import PromptBuffer
#        from binding import load_custom_binding
        
        
        _logger.debug('terminal size %dx%d' % (rows, cols))

#--------------------------------------------------

        book_buffer = ReaderBuffer()
        book_buffer.is_readonly = False
        
        
        booklistwindow = EditorWindow(name = BOOKLIST_WINDOW,
                top = top,
                left = left,
                rows = rows - PROMPT_HEIGHT,
                columns = cols,
                buf = book_buffer,
                wrap = True)         

#--------------------------------------------------

        login_buffer = LoginBuffer()
        login_buffer.is_readonly = False
        
        
        loginwindow = EditorWindow(name = LOGIN_WINDOW,
                top = top,
                left = left,
                rows = rows - PROMPT_HEIGHT,
                columns = cols,
                buf = book_buffer,
                wrap = True) 

#---------------------------------------------------
 
        edit_buffer = PromptBuffer()
        edit_buffer.is_readonly = False


        editwindow = EditorWindow(name = DEFAULT_WINDOW,
                top = top,
                left = left,
                rows = rows - PROMPT_HEIGHT,
                columns = cols,
                buf = edit_buffer,
                wrap = False)


        
        editor = Editor(
                        rows - PROMPT_HEIGHT, 	# editable area height
                        cols,			# editable area width
                        rows - PROMPT_HEIGHT,	# prompt row
                        PROMPT_HEIGHT,		# height of prompt window(1)
                        cols,
                        windows = [editwindow,booklistwindow,loginwindow ],#
                        initial_focused_window = BOOKLIST_WINDOW)#BOOKLIST_WINDOW )


        registry = MergedRegistry([
            console.default_bindings(),
            load_custom_binding()
            ])

        app = Application(editor, registry = registry)
        app.run()
        
        
    except:
        _logger.error('application exited with exception: %r' % traceback.format_exc())
        raise
    finally:
        pass


console.run(main, sys.argv)

