
def downloaded_files():
    
    import os
 
#    _dir="/home/cdh/vishal_iit/UIFramework/examples/Downloads"#
#    _dir="/home/osboxes/Downloads/UIFramework/examples/Downloads/"  
    current_directory = os.getcwd()
    _dir= os.path.join(current_directory, r'Downloads')
    if not os.path.exists(_dir):
       os.makedirs(_dir)
    
        
    ext=[".epub",".py",".pdf",".docx"]
    files=[]
    for fn in os.listdir(_dir):
        for ex in ext:
            if fn.endswith(ex):
                files.append(fn)
                
    file_details=[]
    
    for f in files:
        info=[]
        path=os.path.join(_dir, f)
        info.append(f)
        info.append(str(os.stat(path).st_size)+" bytes")
        info.append(str(os.stat(path).st_mtime)+"")
        file_details.append(info)

    return file_details
#
#    if file_details==[]:
#        return [file_details]
#    else:    
#        return file_details


    