from de import downloaded_files

class ReaderBuffer():

    def __init__(self,  text = ''):
        
        self._text = text
        self._files = downloaded_files()
        self.lvl=0
        self.index=0
        
        
print ReaderBuffer()._files