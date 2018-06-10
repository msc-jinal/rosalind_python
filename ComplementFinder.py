def swap(str,ch1,ch2):
    str=str.replace(ch1,'*')
    str=str.replace(ch2,ch1)
    str=str.replace('*',ch2)
    return str
    

file=open("sequence1.fasta","r")
line=file.read()
print(line)
line=swap(line,'A','T')
line=swap(line,'G','C')

print("\n\n\n"+line)

