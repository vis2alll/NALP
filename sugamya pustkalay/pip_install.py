# -*- coding: utf-8 -*-
"""
Created on Tue Dec 05 11:57:22 2017

@author: DELL
"""

#=========================        req module install & import          =========================#

req_modules=[]
plt_modules=["prettytable"]

req_modules.extend(plt_modules)
is_proxy=False



def install_and_import(package):
    global is_proxy
    
    import importlib
    global manually,proxy
    _import=True
    
    
    
    try:
        if not is_proxy:
            if package=='pyserial':
                importlib.import_module("serial")
            else:
                importlib.import_module(package)
    #        print 'import ',package
        else:
            importlib.import_module("garbage_awk1o29810ljj234cj3lmzsnksad")
            
    except ImportError: 
        print 'import ERROR:  ',package
 
        manually.append(package)
        print "       installing "+str(package)+"..."
    
      
        import pip
        try:
            pip.main(['install', package])
#            pip.main(['uninstall', 'leancloud'])
            if package=='pyserial':
                importlib.import_module("serial")
            else:
                importlib.import_module(package)

            
        except ImportError:
    
            response=["y","n"]
                
            if proxy==None:
                is_proxy=str(raw_input("Are you running Internet behind a proxy (y/n)? : "))
                
                while 1:
                    if not is_proxy in response:
                        print "Your response "+str((is_proxy))+" was not one of the expected responses: (y , n) "
                        is_proxy=str(raw_input("Are you running Internet behind a proxy (y/n)? : "))
                    else:
                        break
                        
                    
                if  is_proxy=="y" :
                    proxy=str(raw_input("Enter proxy_IP & proxy_Port  ex: 10.10.78.21:3128 : "))
                    pip.main(['install','--retries=2','--proxy='+str(proxy), '--upgrade',package])
                 
            #=====================================#    
import sys,os,importlib

manually=[]
proxy=None

print "      ----installing Packages...   "

for package in req_modules:
#    try:
    if package=="Image":
        try:
            from PIL import Image,ImageTk
        except ImportError:
            install_and_import(package) 
            
    else:    
        install_and_import(package)
#    except Exception as e:
#         exc_type, exc_obj, exc_tb = sys.exc_info()
#         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#         print(exc_type, fname, exc_tb.tb_lineno)




        try:
            if package=="pyserial":
                package=="serial"
                
            globals()[package] = importlib.import_module(package)
            print 'import ',package
        except ImportError:
            pass
#            manually.append(package)





if not manually==[]: 
    
    if 'pyserial' in manually:
        try:
            import serial
            manually.remove("pyserial")
        except ImportError:   
            pass
        
    if 'PIL' in manually:
        try:
            from PIL import Image,ImageTk
            
            manually.remove("PIL")
            manually.remove("Image")
        except ImportError:   
            pass

    if not manually==[]:    
        print "_______________________________"
        print "Packages not installed yet:"+str(manually)
        print  "Try to install them manually. "
    else:
        print "All Packages imported successfully. "
else:
    print "All Packages imported successfully. "
#================================   installation finished   =========================================#

