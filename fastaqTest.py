

import Bio.SeqIO as seqio
import gzip


with gzip.open("SRR022825.fastq.gz", "rt") as myfile:
    
    print (myfile)
    records = seqio.parse(myfile,"fastq")
    for s in records:
        print (s.seq)
        #print()


records = seqio.parse("SP1.fq","fastq")


for s in records:
    revSeq =s.reverse_complement() 
    #print (s,revSeq)
    #print()