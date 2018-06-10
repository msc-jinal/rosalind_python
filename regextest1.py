"""
Created on Sat Jun  9 12:18:30 2018
regex of re
re.match() = search only at beginning
re.search() = search in the entire string
re.compile(pattern) = create pattern
writelines() = write all the lines one after another
writeline() = write all lines with one blank line in between
@author: User
"""
import regex as r

f1 = open("reference.fasta","r")
header = open("fastaHeadings.txt","w")
sequence = open("fastaSequences.txt","w")


headingPattern = r.compile(">\w+\|\d+\|\w+\|\w+\.\d\|\w+\d+\s\w\.\w+\s\d\.\d\w\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+")

lines = f1.readlines()
for i in lines:
    if (headingPattern.findall(i)):
        header.writelines(i)    
    else:
        sequence.write(i)
        
header.close()
sequence.close()
f1.close()   




    


        
    
    
    


    








