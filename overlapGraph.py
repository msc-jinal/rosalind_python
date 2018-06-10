# -*- coding: utf-8 -*-
"""
step 1: Extarct header and sequence from fasta file
step 2: Find matching suffix and prefix

@author: User
"""

import collections

def extraction(file):
    file = open(file,"r")
    lines = file.readlines()
    seqdict=collections.OrderedDict()
    temp=""
    dictkey=""
    for i in lines:
        if i.startswith(">"):
            if temp != "":
                #print(dictkey)
                seqdict[dictkey]=temp
                temp=""
            i = i.replace(">","")   
            dictkey = i.strip() 
        else:
            temp=temp+i.strip()
    #print(dictkey)       
    seqdict[dictkey]=temp
           
    return seqdict

def searchAll(tempstr,ch):
    poslist=[]
    start=1
    pos = tempstr.find(ch,start)
    while pos != -1:
        poslist.append(pos)
        start=pos
        pos = tempstr.find(ch,start+1)
    #print(poslist)
    return poslist

def isOverlap(tempstr,teststr,position):
    subtempstr=tempstr[position:]
    subteststr=teststr[:len(subtempstr)]
    #print(subtempstr)
    #print(subteststr)
    if subtempstr == subteststr:
        return True
    else:
        return False

resdict=extraction("graph.fasta")
totalkeys = resdict.keys()
totalvalues = resdict.values()
#print(totalkeys)
#print(totalvalues)  

outfile =open("overlapgraph_result.txt","w")

def findmatching(totalkeys,tempseqid,tempseq):
    for key in list(totalkeys)[1:]:
        seqval = resdict[key]
        if(seqval != tempseq):
            cchar = seqval[1:2]
            totalpos = searchAll(tempseq,cchar)
            for pos in totalpos:
                if isOverlap(tempseq,seqval,pos):
                    outfile.write(tempseqid+" "+key+"\n")
                    break
            
for i in range(len(totalkeys)):
    #print(i)
    tempseqid = list(totalkeys)[i]
    tempseq = resdict[tempseqid]
    #print("id ",tempseqid)
    #print("seq ",tempseq)
    findmatching(totalkeys,tempseqid,tempseq)

outfile.close()    