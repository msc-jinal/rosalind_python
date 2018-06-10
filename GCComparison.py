import Bio.SeqIO as SeqIO

def gcCalc(seq):
    seqlen=len(line)
    countC=line.count("C")
    countG=line.count("G")
    totalGC=countG+countC
    GCcontent=(totalGC/seqlen)*100
    return GCcontent


seqRecords=SeqIO.parse("MultiFastaFiles.fasta","fasta")
gcMap={}
for record in seqRecords:
    id = record.id
    line= record.seq
    GCcontent=gcCalc(line)
    gcMap[id]=GCcontent
         
k=gcMap.keys()
v=gcMap.values()
"""
for i in k:
    print(i," ",gcMap[i])"""

       
dessortedkeys = sorted(gcMap,key=gcMap.get,reverse=True)

"""
for i in sortedkeys:
    print(gcMap[i])"""


for i in dessortedkeys:
    print(i," ",gcMap[i])

print("\n\n")
asesortedkeys = sorted(gcMap,key=gcMap.get)
for j in asesortedkeys:
    print(j," ",gcMap[j])
            


