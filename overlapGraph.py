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
    if subtempstr == subteststr and len(subtempstr) >= 3:
        return True
    else:
        return False

resdict=extraction("graph.fasta")
totalkeys = resdict.keys()
totalvalues = resdict.values()
#print(totalkeys)
#print(totalvalues)  

outfile =open("overlapgraph_result.txt","w")
matched=[]

def findmatching(tempseqid,seqid):
    tempseq = resdict[tempseqid]
    seq = resdict[seqid]

    if(tempseq != seq):
        cchar = seq[1:2]
        totalpos = searchAll(tempseq,cchar)
        for pos in totalpos:
            if isOverlap(tempseq,seq,pos):
                matched.append(tempseqid+" "+seqid+"\n")
                break
            
for tempseqid in totalkeys:
    tempseq = resdict[tempseqid]
    for seqid in totalkeys:
        seq = resdict[seqid]
        if tempseqid != seqid:
            findmatching(tempseqid,seqid)


outfile.writelines(matched)
outfile.close()    