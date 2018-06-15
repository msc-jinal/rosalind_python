# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 21:13:29 2018

@author: User
"""
import collections
import sys

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
    filename = sys.argv[1]
    trimvalue = int(sys.argv[2])
    fname = filename.split(".")
    #outputfile = fname[0]+".trim."+fname[1]
    output=open(fname[0]+".trim."+fname[1],"w")
    
    seqdict=extraction(filename)
    totalkey = list(seqdict.keys())
    totalvalues = seqdict.values()
    
    for pos,seq in  enumerate(totalvalues):
        #print(seq[:trimvalue])
        output.writelines(">"+totalkey[pos]+"\n"+seq[:trimvalue]+"\n")

main()