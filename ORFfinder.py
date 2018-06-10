codon_list = ["ATG", "TAA", "TAG", "TGA"]

str = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

found_codon_position=[]
n=len(str)
k=0
while k < n-2:
    possible_codon=str[k:k+3]
    if possible_codon in codon_list:
        found_codon_position.append(k)
    k+=1

print(found_codon_position)
    
            
