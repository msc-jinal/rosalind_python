# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 20:57:12 2018

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

def main():
    seqdict=extraction("tempRef.fasta")
    totalkey = list(seqdict.keys())      
    totalvalues = seqdict.values()
    
    #print(len(totalkey))
    trimvalue=50
    for pos,seq in enumerate(totalvalues):
        print(totalkey[pos])
        print(seq[:trimvalue])
        
main()