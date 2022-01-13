# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 16:54:13 2021

@author: gusta
"""

import requests
import lxml.html as lh
import pandas as pd

url='https://subscene.com/subtitles/manos-the-hands-of-fate'
#Create a handle, page, to handle the contents of the website
page = requests.get(url)
#Store the contents of the website under doc
doc = lh.fromstring(page.content)
#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')


tr_elements = doc.xpath('//tr')
#Create empty list
col=[]
i=0
#For each row, store each first element (header) and an empty list
for t in tr_elements[0]:
    i+=1
    name=t.text_content().strip()
    print('%d:"%s"'%(i,name))
    col.append((name,[]))
    
    
#Since out first row is the header, data is stored on the second row onwards
for j in range(1,len(tr_elements)):
    #T is our j'th row
    T=tr_elements[j]
    
    if len(T)==5:
        
        #i is the index of our column
        i=0

        #Iterate through each element of the row
        for t in T.iterchildren():
            data=t.text_content().strip()
            #Check if row is empty
            if i>0:
            #Convert any numerical value to integers
                try:
                    data=int(data)
                except:
                    pass
            #Append the data to the empty list of the i'th column
            
            col[i][1].append(data)
            #Increment i for the next column
            i+=1
