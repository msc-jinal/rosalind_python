def swap(str,ch1,ch2):
    str=str.replace(ch1,"*")
    str=str.replace(ch2,ch1)
    str=str.replace("*",ch2)
    return str

def change(str,ch1,ch2):
    str=str.replace(ch1,"*")
    str=str.replace(ch2,ch1)
    str=str.replace("*",ch2)
    return str


def translate(sequence):
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
    str=codontable[sequence]
    return str

DNA="TCATAATACGTTTTGTATTCGCCAGCGCTTCGGTGT"
DNA=swap(DNA,'A','T')
DNA=swap(DNA,'G','C')
print(DNA)
RNA=change(DNA,"T","U")
print(RNA)

i=0
while i<len(DNA):
    #print (DNA[i:i+3])
    piece=DNA[i:i+3]
    i=i+3
    s=translate(piece)
    print(s,end='')
print("\n\n")
#SIMQNISGREAT

def translation(sequence):
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
            codon= sequence[i:i+3]
            protein += codontable[codon]
        return protein
            
pro = translation(DNA)
print(pro)
RNASeq="AUGUUGGAGAACGUCAAAAAAAUGCGCGCGGAGCGCCGGUGGGACUUAAUCAAGGUUCAUCGUUUCCUAAGAUGGGAACUCAUUGGUGCUCCGAGGACCAAUGUCAUCCACACACGGUUUAUACAAAGGCUAAAUAACGACAUCACAAAGCUUCGUAGGAUUUACCAACCGCCGACGUGGGUCAGUUGUAGACAGGCGGGCGCCCAAUUCAUCACUGGCACGAGUCGUACAGAUCUCCCAUUGAGUAGGGUUACGAGGCCUCCGAAACGCACCACCGCAUCAAAGCGCGGUAUUCAACUUCACUCUUCGAGUAAAAACAGCCUGCUCGGUCCUCCCCCGGAAGAGUGCGACAACGCAGUCAUGCCAAAAUGGAAUGUCGGGUCUAACCUGCGUGACCAUGCCCGACUGGUUCCUAUCGCGGGCUCUGCUCGUCUCAACCAGGCCCUCAAAGUUAGGGACUUUCGCGUCGAGGCCCUAGCAGCCAUAAUAGCAGGUUGCCGUUCUAGGUGUGUUCUGAGACAUCCCUCCGUGUCGGUCCUGCUUACGCAUGGCAGACUCGUUAUUACUUUUGUUUCGGAAUGUCCCAGCAGAACUUCUGGUCGGCCUUCUUCUGGGAAGAGCGUUACUCUCGCUGCUCACGACUCUUCAUCUAGCUUCAGGUCAGAGGCCAUAGCUAAUCCGGUUCGAAAUUUAUUAGGGUCUCGGGGCUUUAACGUCCGGGAUCGGCACUGGGAAAUCAGCCGAGCCACAAGCUGGCCGAUGUUCGGCCGGAGUAUCCUAUUCUCAAUUCCGGUACCCAACAGGGACAUAUGCCGCGCAUGUUUGAGAUUAACGCCGCUAUGGGCAAAGAGUGGAGGACCGAGCUCGGCAGCCUAUUCCGACAAUGACUGGGUACGAUCUGUUACCGUGGUACGCAAAAACCACCUGGCGAGAGGUACAAACGCGAAAGGGCAUAACGAAGGACGACGCCAGAGAGACGAGACUAGUCAUCGUGCUAAGCCAGAAUGGGGACUUUCGCAACGCUCGGCGGCAUACGCCAAGACGCUAUGGGAAAUUGCAUCUCGUAAGCAGGCGAAGGCAGGGUGUGGCCCUUUAAAUCUCGGAUAUAUUGUGAGCAGUGCAACGUGCUUGGCAGCAUUUAUAACUAUAGCAUGGGAUCUAGACUGUCCAUACUUUUGGAAACGGAGUUUCGCCCUCCUUUCCGCUACGGUAUGCACGCCUCUCGCCUUCCAGACGUACGGUCCUUUAUGCGUACGUCUACAUCUUGGGAGCCUACACGAAUUCAGCGCAGUCGCUAAUGUCCCUAUGGCGACUCCGGGGGCGUUUGUCCGUUCCCCGCAUCUGGAUCACCUACUCGGGUCCCUAGGGCCGGAGUUGCCGUCCGUAGAACCUUUCAGAACAAGCGUUGAAGUCGACAGAAAAAAAAAAAUGGAGCGAUACACCCUCAAGUACAGACAUCGAUUUCUUAUCCCGGAUAAUAUCGUAUCUCUAUUGCUAGCUGCAGAAGUCUUGCCGGAGUUCUAUAAGUAUACGUCCUGCCCUGGCUUCUGUCACAAUAAAUCGGCAGACCUUAGAGCAAUCUGUGGUUACACAUCUAAUGUUUACACAAGCCGUGAUUGGAUUGUGUCGGCUCCGUUCGUUCACUCAUCCUUUUCGAAAGCACCUGUAACAUCAAAUGCCUUGCCUGUAUUCAUGUCCGGUACAUGGAUAUGUAAUGGCGGGUCGCGCGUAUACUCCAAAGUUGUUCUAUCAUCAGACAAUAAGGACCGUGGUUUUGCUUCUGCCUCAUGUGGCACUCACGCUCCCUACCGAUAUAGUCCCAUCCAGACCGCGUUCGUGAUAGCCAUAACGAUUCAGGCAAACGCCAGGAGUAUGCACGGGGCAAAAAUUUCCUGUGUACCACAGUGGUAUGCGACUAACCCCCCGCAUCGCUACGCUCGCGGCGAAGGUCCAGAAGCGGUCCGUCUGCUAACGCUUCCAGUGAGCAUCGUGCCGAUAAAGACCCCUGCGACGCUGGUGUCGGGUACACUUCGCGGAGGUGACAUAAUGACCCAGGCACAUCGUGGCGGACCUGAUGAUAGCUCCCUACAACAAUCCAAUUCUUUGCACCUGCUGAGAUGGCCGGGAGUGAGUUGUUUCUGCAACCUCGUGCCUCUAUUAUGUGUCUGGUCACUGUACACCUACGACCAGGUAAGGCAUCGUCGGACUAUAAAGAUGCGGCCGUCAUACCAGCAUUUGCCCCUAGGUAUUUUAACUUUGGGUACGGACCGACCCAAAUCGAGUAAAUUGAUUUCCACCCAGGCUGGCAACCACGUUAUAGCGUGCGCCCGAUCAAAGGCGGAAUGGUUGGAAAACCGACAUAAGCGAUCGCCCGAUACGCCUUGCCAGAGACAAGUACAAACACUCUGUGGUAUCGUAUUGCUUUGCCAUGCGGGCGCCCUUUUGCUCAUUCGGGGGACCACUUUGCACACUAAUCCUACCGUUCUGUUCUGCGUAGCACACAUCGGCAAGCGAUUGAAAGGCUUAUACGGGGUGCUGCUAGACACCGGCGUACAGCGCAGGGGGAUGGCCACCGCGUACACUAUGAUAAAAAUUCGCGUCUCGGCCUUAUUUCUCGGGAAGCGUCAUAUUGACCCGUUACGACACAGGAGUUCUUUAAGUACUACAUGGUGGGAACGUUUACAGAGUUACGCGUCUGACAUGACUUAUAAGAGGAGCGCGACCGACUCCCUGGGAAGCAGAGACUCCCAAAGCCCGCGUGCCACACCCUUCUCGGAUCCGGAGAUCAUGCUUACGACACAUGCCUGUAAGCAGCCAAGGAUGCCCCGGUUUACUGUCAUUGGCUUGGGUGAAGCUAGAGUGGUCGCUGGGGGAGAUUCUCGGCUCCCUGCCCAGACCUCACCGCGUCCGUUUUCUCCAUCAGACUCUCAUGGCAAUAAAUCCCGGGGAAUACAUUAUUAUAACCCUAACACGCUAAUCGAUCCGGAUAAUCGUCGAGCACAAGAAUGUAUGCGGCUUGUUCGUUUGACACGUACAAGAGAAUGCCGUCCGUGUCUCAUAUUGUACAGUAGGACGCCCCAAACAAUACUAUACAAGUACGCGGGCAGUGCCGCUAGUGAAAUAAGUAAAGGUAUUGUAGUGCUACGAGGAAUAAAGUACACAGUUGGGGAGUUGGUUACAUUGGUUACCGUACACAAGUCGCCUGCUUUAACCAGAGAUGCCUUGAUGGUCCCAACGACGUCAUCUCUAGCAAUUGGCCUACCAAGAACCACCAAUGCUGUCUUGCUCGCUACACGGUCGCUGGAUCCACCUGAAGAUGUCGUGAGGAUUAUCUCCAAAAAACUUCCUUACGGUACGGACUUCUAUCGGCAAUCGACUUCGACUUGUGGUUUGCCUAGCCCAACUGUACGUAGGCCCACCGCGUCGUCGCAGUGCAAUUCGAUCUAUAGUCCCAUAAGUAAGACUACUUCCUUAUCGUACUUUCGUUAUUAUAGACGUAGCGCCAGGCUAAAUCAAACUCUGCGUGCACGCUCAAAGCCGUUAUUAUCCGCUCCCUACAGACAGUGGCAGCCCCCGCGAGUGUCUUCGGAUGGAUGGGGAGAUCAUCUUGGAUGUGUUCUUGAACCAGCUCCGGAGUGGCUCAAACUAAGGUGUCCGUGUACAAGUACUUAUGGCUGGUUGAAUGUCGAAUCUGGUGUGGAUUCCCUGAACUGGAUUGGUUCCCGUGUUCGUGGUUUGCCCACGUACAUAGGCAAACUUGCGGCGCAAUCGAAAACGGAUGACCUGUGUCGCCCAACCGUGUUGGGCGACCUAGAAUUCGAUACAUGCUUUUCUAAUACGUCAGACAGGUCUGUGCUGAGGGCGUUAUACGAAUCAGGGUGUUCAAUGUAUCAAUGUGGCAUAGAUGCAGCCCCGCAGAAGGGUUGGCCUAUCGGGUUCAAUGCUCGGGCUUCCUCCGUAGGAAUGGAACCACGGAGCUUGGUGGCCUCAAGUAUAUCCACGACAUGUCAUGUUGAUUCGCGGCGGAGCCCCAAGUCCCGUUCGACAGUUCACGAUAACUCCUGCAAAGAUUACGUCCAUUCAAUAAUGAGCUGGGAAUGUAACAGACUUAACGGGUAUAAAGAUUUGGAUAAUUUCGGACAGAGGAAAGACGUCUGCACGCUAAUUGCUCAAUUUCUAGACUAUUUUAAAAGGUUAACAAUAUUCCCGGUAGGAGCCCCACUUGUUCCGCUUUGCUUUACCCGCCCCGUAGGCGUUAAUCUGUUAGGUUUCACUUAUCCACGCUGGCAGCUUUACCUGGUGCCGAAUCUAGUUCUUUGUUACACCCGAAGGUGCUUUAGGAAGGCAGGAGGGACCGGUCCCCGCAACCUGACCGAAUUGUCCUUAUUAUUGUACCACGCGGACGUAAAUCAUCUCGCGAAUAAGCUUUUAAGGAGCAUGAUCUACAGUCUCUACGACAGACCGUGUGUUUGUAAGAUGACGGAUACCUGCAGGGGAAACCAGGCGUCAAUCCGAACUAGCGGUGGAGAAUAUUUGAAGCUGUUACGUGGUAACUUAGUGCUGCUCAAAGGCCCACGACAGCAAAAAGGCGACAAGUAUGUUAAUGUCUAUAAGGUUUAUCAGGUAGGAGGCCCAUCGGCAAGCCGCAAUUCAACCGCCUUGCCUGGGCGCUCUCUUGGUUGGGAGAAGCGGAUUAGCACCGCCCCGGCCAGGGGUGGCAGGGUAUCCAACUGUACCAGCGGGCUCAACGGGUCCACCCGCACGCGUACGAGCUUCAGCUCACUACGUAAUAGGAAUCAAGGCGGUGCCAGUUGGAUGUGCGACGUAUUCAGCUAUCUUGGCACGUUACCGGUCCUACGCUUUGCCCCGAAUCGUAUAGGUGUAGGGGAUCGGAAACUUCAGGGCCCGCCACGAUUUGCUGAAUCGCUCGGUCCAAGGAAUCAAAUGCCCAAGCGUCGUAGGAUAUGCGGGGAGAGUUCUGUAUCGUCAUGUGAGUUGCGAUCAUCCGGGGACGCUCCGCGUGCAAUAAUACAAGUUAUGCCUCCAGUGGAGAAACGACCUAAUUGUUUCGAAGCAUCCACAGUUAUUGCCGUCCAGACGCACACAAACACUGUUCAACUACCGACCACAUUAUCUAUUCGCAGGGUAGCCGGACCUUCAAACAACGUCGAUUGGGAAUGUCGGUCGGGUCGUCGAGGGACCCUACCGCAAAAGCUAUUAACCUCCGACCCGAGUCGGCUAUCGCCUCGCAUACCCGAGGCUACUGAAAGUGGUACGCUUGGUGGCAUUGGCUCGCUUGGUGCCGUUAAUAGUAGAGGCAUAAGGUUUGUAAAACUGGGGCCGGAGGAGGAUGAUUUGGAUAAUAGCGCGACGCCGGACGGCGCUCCAAGAUGCGGUUGCAGGCUAUUCAUUGGGAACCACCUCUGGGCCUGCAAACAUUCCGCAACCAGUCGCGUUAUGGCACUGAAGGCUCUGGUGUCGACUGAGCCUAUAUCCUUCUUGCGGGAGCUUAGUAACACGACACCGGAACUGGCGAGGUACUGCGAGAAAGAUCAAAACGACUCACCCGUGCCCAUAUGGGAAACUCAACCCAUGCAAGUCACGGCUCGCUGCAGCUUGAACAGUUGGUGCGUGGGCAAUCACUGCGCAGAUACGGAUUGCGGGGAGAGCUGGCGUGAAGGUUUGUUGCCGCCGUUCAGGGCGAGUGCGUGUCCGCGGCUUAGACAUUACAAAUCUUGCAUAUUAGCAUAUUACUCGCUGCAUUUAUGCUUUAGAUUGCACAGUCCAGCGACACGGCGCGUGCGGCGUUGGUCUCGGGGUACGCGAGGUAAACUCAAGCAUCGCCAUGAACAGAGCGGGAUAUUGUCUGAUAAUUCUCGUCUCAUUUGGGCUCAGCUUCCCUCUAUGCAGAACCUGGUCCGAGCGUCAUUUUUGUCAAAACUUCUAGGCCGGUCUAGACGCGACAGGCGACCACUCCAAGACGUCAUCCAGUUUGGGCUGAUGACGGGAUCUGCGAUGCGAUGGUCCUCUCGACUUCUUGACCCUGCGGAAUGGGUGCAGACUGCUAAUUACGGUUGUGCACGUUUAAGGUCCGAUAAAGCAAAUAGGUCUUGGCAAUUCACGAUCAAGACUGCCGGCGAGUAUGGAGUAGGGCCGCUAGGGAGAGCGCCGCCAGUGCAGAUAGUGGCACUGAGGGGGGAUCCUCCUAUGUUAGACCCUACCUCUUCCGAACUGGGCGCACAGUCCGCGAUUGGCAAUGGUCGCGAUAAAAUAGGCGUGGGUCAUCGAAAAAUCCACUCUACGUGCUACCCUUGUCCUGAUGGCUGGCACUCAUGUUCUCUAUUUCGCAUCAUGGUAAGAGCCGGUCGCGAAAGGGCCUUGUGUCGAAUGCUCCGCAGGAUUUGGCACCCCGUCGCAAACCUUAGGGCAGUUUUACGCCGAUGUUCUCUCUAUACGACACUUCACGGGCCCCGGCAUCCCAUACUGCUACUCUUGAGUCCUCUACCCAAUCACGUGCAGGCCGUCAAACCCGCGAACCCGUCUUGUUUGACUCACCUAGAUUCACUCGCCAUACUCAAAAGCCCUUACACGGAUCCGGGUUUUCGUUUGUCCCAGCUCAUCGGGUCCCCUGGGGCGGCUGAUUCGGUGGGCUACGCAGAAGUGACUUACGGAUCAGACCGAUUUACACGAGCCGAUGAUCCUCACACUUCCGUCUGCUUCAUACGAUUGUGUCCUUACGAGGCUGAGCAAAACAAGCUAAGCAUAACCAGGGAUGAGCAGGAACCGGAUAUCACUACAGUCAAUCACCUCCUCAUGUCGGGUAUCCGAACAUGCCCUAGUGCCGCUUCAGAGCCCCCAACUCGUGAGCUUCUUAUGCCAGUGGUGUGCGAGCUAGGUGUACUGGAGUAUUCCUUCGUCCGUUUUCAAGAUGCGUUCUUUUUGAAAUUAGGGUGCCGCGAUGACUUUAUAUCUCUGCCCAAGGGCCUUCGAAGCCCUGGGGCAUACCGCAGAGCUCCAGCCCAUGCUGACACUUUGUUCAGACCGUCGUUGCGGGUCAUGUUUGUCUUCGAAAUCUUGCCCGGUAAGGCUAUUUGGACCAACGAACGGCAUCGUGGUAGGAGGAAGGAGGCAUUCUGUCGGUUCACAAAUCCGGCGGCCCCAAAGGUGAGUCAGAGCCACGCCAGUUUCUCAGGACUAGCCAGACGACGCACGCACCACCUGUGUUGUGGUUCCAUCACCGUCGAAAGCGGCGUAGCAAUGCGUUCUGUUACUGGACAACAAAGUAACACAUCGGUGCCAGUGGAAGCUUACGUCGAAACGGCUGGACACCGAACUAAAUCGUCGAGCGUCAGGACAACCUCCAGGAACACUUCAGGGCAUAUUGGGGGCCCUGAUCGGAGACUCUUCUUUCAACACGAACUCGUAUCCCGCUUAGUAUACAUGCUUUUUGCAAACAUGCUAGGCCAAAAAGAUACGAAUUCACGUGGUGGAUUAUUACAGUCUAACUAUAGGGGCCGUGAUACGCACUCAUCGCGGUCUUUACUCCGCUCCCUUGUUUCCGUCAACUCAACGAUAAGGAGAGAAGCAAUCGCGUCCAAGCCCAGCUUAAACGUCAUUCAACAAGUGGGUGUCGCCUGGUAUAGGCUUACGUCCUUCCACGCUAUACGACGAUUUAUCAGCAACUCGGGGGAAACGCGCGAACUUGCACAGGAUGAUUCAUUCAGAUUAUUCCUUUUUUCAGCUGCUGGGUUGGCGCGCCAGCUGAAAUUCAUGACUCUACCAUUAACCAUGUUAUCUCCCUCCCAGCACUUUACAAAGCUACACUAUAAAAAGUGUACUACUAUGAGUGUGCCCGCCUACGGAUGCCAGCGAAGCAUGCGGCAACACCUCGAGUUCCCCUUUAACUGGCGUAUCGGCCUUCAAUCUUGUAGUCUGGGUUCCUCUUUACGAAACCCUUAUAAAGAGCUUCGGGUGAAGUGCACAUCGGGAACUGCUGACGGGAGGCGUCUCACGAGUCAUGGUGCCGCCUCUAACUAUGAUGGACACAGUUACACAACGACAAGGAUAGUACGGCAGGUGAGCCCGAUAUUCGAUAUGCUGCUGUUCACACUUUUUAUAGCUCUCCUUCAUGGGGUAUUAGGCAAUCUCUUAGAAAAUUUUUCGCGAAAGUGCUUUAUGACCCGUGUCGUCCUCAGCUUAGGGCCUAUAGAGGAAACAGACACCGAUGAUCAAUCUUACCGUGCUGCCGCGUCACCGGACACCAGGACACUCUAUAAAAUCGUUUCCUCGAGAAACGGCGCCCUUAUUCUCGUCGGCCCUUUCAAUGCCGGCGGUGGACAACAUGUCACUCUAAUUUAUCAUCAGAAGCGCGUAUUGGCAGGGUCGGGCGCCUUGAGAAGCCUGAGGUUAGCGUCGUACGUGUCUCGCCUCUCGUACACGCAAUCGGGUCCCGAUCGCCCGCUGCCCGAGGACCGUUGUCUGCGCUGGGCUCCGAAUGCACGGCCUAAAACCGUGCGCGUCGGCCAGCGUCCCCUGGCUCCAGGCUUAAUAGGCGCAAUGCCGGCUGGUUUACCAACGGAAUUUCUGUACCCAAUUGACGAUCUAUUGGGGUACCUGCUCCCUAAUUUGGUUACCUUGUUCUUAUUUCAUACAUGCGAAACGGCUGCUCUCACCACUCAUCAUUAUAACUUUCAUUCGGGACGAUUAGACUUUUCAGCACGAUUGUUUGAAGAAACUGGGGCAAGUCUUUCUAAGGAGUCAAGUUUGCAAUCAAUGAAAAAACGUGAAGCACAAUGUCCUCUGUCAUCCGGUCAGCGGCAGAUGCUCCCGGAGCCCUACAGGCGCACCCGACCUACUAGCCACGCAAAUUAUGGGCACAAAAGCACUUGCAGGAGAGGUAGUAUAGUCCUGGCUGCCGAGCAACACCGAAUCCGUCAGCCCACGUUUAAGGGAGCCGUUAAUUACCCUAGCUGUUGCACGUGUGCAGAACGCAAAGUGCCCGGCCAAUUAAGAACCCGCUGCCCCCAGCCUAUAACUGGUGGAGUCUCCCGGGAAGAGCGUGAAUCUUUAAACCGCGCCGUUCCCUCACCCAAAUGUGUCGCCGGGGGAACGUCUACGUUGCCGCAGCAACAGAGCCAUAAAGAUAGUCGCACGCGUUUUCCCACCAGGUAUUGUCGGCCUUGGACCCAUUUGAUGAUGUGCAUAAUGGCUAUAGACCUGCGCUUCUGGUAUGCCCCCAGAACGCCAGUAGACAACAUGCAGAAUCACGUGCAGACUCUAGUGCUGCCUAUCUCUUUGACCGAGAAAGAGUAUCUCCAGCAUCUUAGCGGUAAGCGAGACGGCUUUCGGGGGCUUGUAGGAGAGUCUCGGAAGGAACCUCGUAUGGCUGAACUACCCGUGUAUUGCAUAUACGGUGUCUCCCUCGAUAGUCCAACUGCUGCACAUAACUUUAGAGGUGGUGUAAGGGAAACCAUAUACAACGAUGUUAAUACUAUUCAUGGGGCUGUCUGCGAGAGUGAAUGGGCAGUAUCAAGCUAUGAGAAAACUCCAAGAGUCUCGGUAUCUCCUAUCCUGUCGCUCCCGGGAAUGAGGAAUCUGGGCGUUCGGACUGAUAGCACCUUGCAAUUCUUUCCAUUAACACCCAAAGUAAUCGCACUUGUAGCGCUAUAUUUGUGUGACCCAUUGACUCCUAUCUGUAAUACAGAUCUUGAAAAUACAAGUGAUUGUUGCAUGCUACGAGGCGAUGGGUAA"
def rnacodon(sequence):
    codontable={
    'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
    'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
    'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
    'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
    'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
    'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
    'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
    'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
    'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W',
    }
    protein=""
    if len(sequence)%3 == 0:
        for i in range(0,len(sequence),3):
            codon= sequence[i:i+3]
            protein += codontable[codon]
        return protein
proRNA = rnacodon(RNASeq)
print(proRNA)           