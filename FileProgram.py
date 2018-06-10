def bubbleSort(list1):
    lenlist = len(list1)
    for i in range(lenlist):
        for j in range(lenlist-1):
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
    
def writeData(val):
    datafile = open("file1_copy.txt","w")
    for i in val:
        datafile.write(str(i)+"\n")
    datafile.flush()
    datafile.close()
    
       
file1 = open("file1.txt","r")
lines = file1.readlines()
print (lines)

lines = [int(i) for i in lines]

    
print ("Before")
print (lines)
bubbleSort(lines)
print ("After")
print(lines)
writeData(lines)

    
lines =  [str(i)+'\n' for i in lines]   
    
print (lines)
df = open("tempfile.txt","w")
df.writelines(lines)
df.flush()
df.close()


   
                     

