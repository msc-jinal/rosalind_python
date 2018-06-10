
import Bio.SeqIO as SeqIO

seqRecords =SeqIO.parse("gcontent.fasta","fasta")


gcmap = {}

for recrod in seqRecords:
    line  = recrod.seq
    id = recrod.id
    strlength=len(line)
    #print(strlength)
    countA=line.count("A")
    countT=line.count("T")
    countG=line.count("G")
    countC=line.count("C")
    #print(countA,countT,countG,countC)
    totalGC=countG+countC
    #print(totalGC)
    GCcontent = (totalGC/strlength)*100
    gcmap[id] = GCcontent  
    
key=(max(gcmap, key=gcmap.get))
print (key)
print (gcmap[key])            