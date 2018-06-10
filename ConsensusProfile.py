import numpy as np

file=open("sequence2.fasta","r")
lines=file.readlines()

#print(lines)
#print("\n\n")

arra=[]
for i in lines:
    if i.startswith(">"):
        continue
    else:
        arra.append(i.strip())
        
matrix=np.array(arra)
#print(matrix)
countA=0
countC=0
countG=0
countT=0
profile=[]
profile.append([])
profile.append([])
profile.append([])
profile.append([])
le=9

for i in range(len(arra[0])):
    for j in matrix:
        if j[i].count("A"):
            countA+=1
        if j[i].count("C"):
            countC+=1
        if j[i].count("G"):
            countG+=1
        if j[i].count("T"):
            countT+=1
    profile[0].append(countA)
    profile[1].append(countC)
    profile[2].append(countG)
    profile[3].append(countT)
    countA=0
    countC=0
    countG=0
    countT=0
maximum=0  
maxlist=[]

      
cons=""
for i in range(len(profile[0])):
    m = max(profile[0][i],profile[1][i],profile[2][i],profile[3][i])
    if profile[0][i] == m:
        cons = cons +"A"
    elif profile[1][i] == m:
        cons = cons +"C"
    elif profile[2][i] == m:
        cons = cons +"G"
    elif profile[3][i] == m:
        cons = cons +"T"
print (cons)


print ("A:",str(profile[0]).replace("[","").replace("]","").replace(",",""))
print ("C:",str(profile[1]).replace("[","").replace("]","").replace(",",""))
print ("G:",str(profile[2]).replace("[","").replace("]","").replace(",",""))
print ("T:",str(profile[3]).replace("[","").replace("]","").replace(",",""))

    
    
    