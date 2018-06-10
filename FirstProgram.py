import numpy as np

def bubbleSort(list1):
    lenlist = len(list1)
    for i in range(lenlist):
        for j in range(lenlist-1):
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
    
list1 = [11,5,25,67,99]
print ("Before")
print (list1)
bubbleSort(list1)
print ("After")
print (list1)



    
    
    


            
   
    


    
    
        