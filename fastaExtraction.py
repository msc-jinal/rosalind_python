# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 14:10:33 2018

@author: User
"""

import regex as r

myFile = open("reference.fasta","r")
totalLines = myFile.readlines()
headseq = open("fastaheadSeq.txt","w")

h1=[]
s1=[]
temp=""

for i in totalLines:
    if i.startswith(">"):
        h1.append(i.strip())
        if temp!="":
            s1.append(temp)
            temp=""
    else:
        temp = temp+ i.strip()
        
s1.append(temp)
for i,val in enumerate(h1):        
    headseq.write(val+' '+s1[i]+'\n')
    

headseq.close()        
       
   
    
        
  

