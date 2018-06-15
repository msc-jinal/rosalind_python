# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 23:17:07 2018

@author: User
"""
from Bio import SeqIO
for record in SeqIO.parse("example.fastq", "fastq"):
    score=record.letter_annotations["phred_quality"]
    
    
#print(score)
    
file = SeqIO.parse("example.fastq","fastq")
for i in file:
    res=i.letter_annotations["phred_quality"]
    
print(res)
    

file = open("example.fastq","r")
lines = file.readlines()
headlist=[]
seqlist=[]
phredscorelist=[]

for i in lines:
    if i.startswith("@"):
        #print(i.strip())
        headlist.append(i.strip())
    elif i.isupper():
        #print(i)
        seqlist.append(i.strip())
    elif i.startswith("+"):
        continue
    else:
        #print(i.strip())
        phredscorelist.append(i.strip())
        
#print(len(phredscorelist))
#solexa_quality = 10*log(10**(phred_quality/10.0) - 1, 10)