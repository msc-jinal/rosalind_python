def swap(str,ch1,ch2):
    str=str.replace(ch1,'*')
    str=str.replace(ch2,ch1)
    str=str.replace('*',ch2)
    return str


file=open("sequence1.fasta","r")
line=file.read()
print(line)
revline=line[::-1]
print(revline)
revline=swap(revline,"A","T")
revline=swap(revline,"G","C")
print(revline)

