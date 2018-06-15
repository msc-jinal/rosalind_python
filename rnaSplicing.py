# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 17:37:45 2018

@author: User
"""
def extraction(file):
    myfile = open(file,"r")
    lines = myfile.readlines()
    headlist=[]
    seqlist=[]
    tempstr=""
    for i in lines:
        if i.startswith(">"):
            headlist.append(i.strip())
            if tempstr != "":
                seqlist.append(tempstr)
                tempstr=""
        else:
            tempstr=tempstr+i.strip()
    seqlist.append(tempstr)
    
    return headlist,seqlist

def removeintrons(mainseq,seqlist):
    for seq in seqlist[1:]:
        #print(seq)
        mainseq=mainseq.replace(seq,"")
        #print(len(mainseq))
    return mainseq
    
def proteinfinder(sequence):
    codontable={
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    protein=""
    if len(sequence)%3 == 0:
        for i in range(0,len(sequence),3):
            codon=sequence[i:i+3]
            protein += codontable[codon]
            
    protein = protein[:-1]
            
    return protein
         
def main():    
    headlist,seqlist = extraction("rnaspilicing.fasta")
    totalseq = len(seqlist)
    mainseq = seqlist[0]
    mainseq = removeintrons(mainseq,seqlist)
    proteinseq = proteinfinder(mainseq)
    print(proteinseq)

main()    

