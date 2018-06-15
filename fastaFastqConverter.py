# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 23:39:14 2018

@author: User
"""
def extractheadseq(file):
    file = open(file,"r")
    lines = file.readlines()
    filedict={}
    seqkey=""
    tempstr=""
    for seq in lines:
        if seq.startswith(">"):
            #print(header)
            if tempstr != "":
                filedict[seqkey]=tempstr
                tempstr=""
            seqkey=seq.strip()
        else:
            tempstr=tempstr+seq.strip()
    filedict[seqkey]=tempstr
    return filedict
        
def main():
    mydict = extractheadseq("tempRef.fasta") 
    totalkey = mydict.keys() 
    #print(key)  
    output = open("testoutput.fastq","w")    
    for val in totalkey:
        #print(val)
        score ='a'*len(mydict[val])
        output.write("@"+val+"\n"+mydict[val]+"\n"+"+\n"+score+"\n")
        
    output.close()

        
    
main()