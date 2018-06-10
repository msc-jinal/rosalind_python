def swap(str,ch1,ch2):
    str=str.replace(ch1,ch2)
    return str

file=open("sequence1.fasta","r")
line=file.read()
print(line)
rna=swap(line,'T','U')
print(rna)

