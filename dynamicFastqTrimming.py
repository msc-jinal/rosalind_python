# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 21:59:49 2018

@author: User
"""
import sys

def trimming(file,trimval,output):
    file = open(file,"r")
    outputfile = open(output,"w")
    lines = file.readlines()
    
    for pos in range(0,len(lines),4):
        seqid = lines[pos]
        seq = lines[pos+1]
        diff = lines[pos+2]
        score = lines[pos+3]
        seq = seq[:trimval]
        score = score[:trimval]
        outputfile.write(seqid+seq+"\n"+diff+score+"\n")
 
def main():
    filename = sys.argv[1]
    trimval = int(sys.argv[2])
    fname = filename.split(".")
    output = fname[0]+".trim."+fname[1]
    trimming(filename,trimval,output)
    
main()