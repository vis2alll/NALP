from __future__ import unicode_literals

from console.logger import logger
from console.core.event_type import EventType
from console.core.buffer_base import BufferBase

#---------
from de import downloaded_files
from console.logger import logger


class ReaderBuffer(BufferBase):
    _logger = logger('reader-buffer') 

    def __init__(self, name = '', text = '' ):
        BufferBase.__init__(self, name)
        
        self._text = text
        self._files = downloaded_files()
        self.lvl=0
        self.index=0
 

    @property
    def text(self):
        return self._files[self.lvl][self.index]

    @text.setter
    def text(self, value):
        self._text = value
        self.emit(EventType.TEXT_CHANGED)

    def cursor_right(self):
        self.index+=1
        if self.index > len(self._files[self.lvl])-1:
            self.index=0
            
        self.emit(EventType.TEXT_CHANGED)
        
    def cursor_left(self):
        self.index-=1
        if self.index < 0:
            self.index=len(self._files[self.lvl])-1
            
        self.emit(EventType.TEXT_CHANGED)
    
    def cursor_up(self):
        self.index=0
        self.lvl-=1
        if self.lvl < 0:
            self.lvl=len(self._files)-1
            
        self.emit(EventType.TEXT_CHANGED)


    def cursor_down(self):
        self.index=0
        self.lvl+=1
        if self.lvl > len(self._files)-1:
            self.lvl=0
            
        self.emit(EventType.TEXT_CHANGED)




    def top(self):
        pass

    def bottom(self):
        pass

    def enter(self):
        _logger = logger('reader_buffer')
        _logger.error(': opening selected file...')
        
    def delete(self):
        _logger = logger('reader_buffer')
        _logger.error(': deleting file...')
        

