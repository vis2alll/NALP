import sys
sys.path.append('/home/cdh/vishal_iit/UIFramework')

import console

from console.core.keybinding import Registry, MergedRegistry
from console.core.keys import Keys
from console.enums import DEFAULT_WINDOW
from console.core.filters.basic import HasFocus, HasBufferState, Readonly, WindowType, SupportsRichText, IsBlockType, HasPropertyOn
from console.core.filters.base import OrFilter, AndFilter, NotFilter
from console.ui.window import EditorWindow
from console.ui.menu_window import Menu, MenuItem
from console.core.buffer_base import BufferBase

#-----
from reader_buffer import ReaderBuffer



class BookWindow(EditorWindow):
    pass
 
BOOKLIST_WINDOW = "BOOKLIST_WINDOW"


def load_custom_binding():
    registry = Registry(BookWindow)

    handle = registry.add_binding

#    @handle(Keys.AltM)
#    def _(e):
#        # current_window = e.current_window
#        # current_window = e.app.editor.current_window
#
#        e.app.editor.message('message demo')
#
#    @handle(Keys.AltE)
#    def _(e):
#        e.app.editor.error('error message demo')
#
#    @handle(Keys.AltC)
#    def _(e):
#        def _on_yes(e):
#            e.app.editor.message('you pressed yes')
#
#        def _on_no(e):
#            e.app.editor.message('you pressed no')
#
#        e.app.editor.confirm('confirm?', on_yes_handler = _on_yes, on_no_handler = _on_no)
#
#
#    @handle(Keys.ControlH)      # change highlighting bold/italic/underline
#    def _(event):
#        window_name = 'HIGHLIGHT'
#
#        def _toggle_highlight(app, name):
#            window = app.editor.find_window(DEFAULT_WINDOW)
#
#            # if selection is not on enable/disable selected property
#            window.buffer.toggle_property(name)
#            state = window.buffer.get_property(name)
#            if name == BufferBase.PROPERTY_BOLD:
#                prop = 'bold'
#            elif name == BufferBase.PROPERTY_ITALIC:
#                prop = 'italic'
#            elif name == BufferBase.PROPERTY_UNDERLINE:
#                prop = 'underline'
#
#            app.editor.message('%s %s' % (prop, 'enabled' if state else 'disabled'))
#
#        event.app.editor.create_menu(window_name, [
#            MenuItem('bold', 'b', lambda app: _toggle_highlight(app, BufferBase.PROPERTY_BOLD)),
#            MenuItem('italic', 'i', lambda app: _toggle_highlight(app, BufferBase.PROPERTY_ITALIC)),
#            MenuItem('underline', 'u', lambda app: _toggle_highlight(app, BufferBase.PROPERTY_UNDERLINE)),
#                    ])

##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#
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

    @handle(Keys.Enter)
    def _(event):
        try:
            
            event.current_window.buffer.enter()
        except Exception as e:
            event.app.editor.error('unknown error %r' % e)
            
            
    @handle(Keys.Left)
    def _(event):
        
        try:
            event.current_window.buffer.cursor_left()

        except:
            event.app.editor.error('unable to navigate')

    @handle(Keys.Right)
    def _(event):
        try:
            event.current_window.buffer.cursor_right()

        except:
            event.app.editor.error('unable to navigate')


    @handle(Keys.Up)
    def _(event):
        try:
            event.current_window.buffer.cursor_up()
        except Exception as e:
            event.app.editor.error('unable to navigate %r' % e)

    @handle(Keys.Down)
    def _(event):
        try:
            event.current_window.buffer.cursor_down()
 
        except Exception as e:
            event.app.editor.error('unable to navigate %r' % e)


    
#    @handle(Keys.AltS)   #  to access sugamyapustkalaya
#    def _(event):
#        window_name ="MENU_LIST"
#        
#
#        
#      
#        from reader import process_choice_selection
##        def choice_selection(app,choice):
#        pcs=process_choice_selection(event,window_name)
#            
#        #-------------main menu---------------#   
#        lst=[
#                    MenuItem('sugamya pustkalaya','1', lambda app: pcs.choice_selection(app,"1")),
#                    MenuItem('bookshare','2', lambda app: pcs.choice_selection(app,"2")),
#                    MenuItem('gutenberg','3', lambda app: pcs.choice_selection(app,"3")),
#                    MenuItem('local books','4', lambda app: pcs.choice_selection(app,"4")),
#                    MenuItem('quits','q', lambda app: pcs.choice_selection(app,"q")),
#                        ]
#        
#        pcs.get_user_input(lst)
#        #------------------------------------------------
 
    
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

 
#---------------------------------------------------
 
        edit_buffer = PromptBuffer()#ReaderBuffer()
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
                        windows = [editwindow,booklistwindow ],#
                        initial_focused_window = BOOKLIST_WINDOW )


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

