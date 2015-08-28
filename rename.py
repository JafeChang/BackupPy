# -*- coding: utf-8 -*-  
import os  
import re  
import string  
  
path =  os.getcwd()  
  
print 'current path : ' , path  
  
name = 'n21_'  
suffix = '.cif'  
  
  
files = os.listdir(path)  
p = re.compile( r'^\d+(\.cif)$')  
p2 = re.compile( r'\d+' )  

x=0

for f in files:  
    m = p.match( f ) 
    
    if m :         
        print m.string
        print m.group(0)  , '   --->   ' ,  
        m2 = p2.search( m.group(0) )  
        if m2:  
            print m2.group(0) , '  --->   ' ,              
            newFile = name + m2.group(0) + suffix  
            print newFile  
        else :  
            newFile = name + '1' + suffix  
            print newFile  

        open( newFile , 'wb' ).write( open( f , 'rb' ).read())  
