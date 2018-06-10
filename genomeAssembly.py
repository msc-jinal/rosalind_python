# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 16:39:26 2018

@author: User
"""

import regex as r

def extraction(file):
    file = open(file,"r")
    lines = file.readlines()
    seqlist=[]
    headlist=[]
    temp=""
    for i in lines:
        if i.startswith(">"):
            headlist.append(i.strip())
            if temp != "":
                seqlist.append(temp)
                temp=""
        else:
            temp=temp+i.strip()
    seqlist.append(temp)
    return headlist,seqlist
     
def searchAll(template,ch):
    p=[]
    start=0
    pos = template.find(ch,start)
    while pos !=-1:
        p.append(pos)
        start=pos
        pos = template.find(ch,start+1)
    return p

def isOverlap(str1,str2,position):
    temp1 = str1[position:]
    temp2 = str2[:len(temp1)]
    #print(int(len(str2)/2)-2)
    if temp1 == temp2 and len(temp2) > int(len(str2)/2)-2:
        return True
    else:
        return False
    
def appendseq(template,substr,position):
    required = template[0:position]
    required = required+substr
    return required

def findheading(gcMap):
    dessortedkeys = (gcMap,key=gcMap.get)


    
head,seq = extraction("fastagenome.fasta")
total = len(seq)
seqlen = len(seq[0])
tempseq = seq[0]

for i in seq[1:]:
    currentchr=i[0:1]
    pos = searchAll(tempseq,currentchr)
    for chrpos in pos:
        if isOverlap(tempseq,i,chrpos):
            tempseq = appendseq(tempseq,i,chrpos)
            break
                
        
print(tempseq)


        
            
            
            
        