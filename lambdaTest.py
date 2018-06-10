
def fun1(x):
    return x[3]    
    

names = ['Nilam','Jinalben','Bhima','JinkalDarling','Dikesh','Nayana']

n1 = sorted(names)
print (n1)


n2 = sorted(names,key=len)
print (n2)

n3 = sorted(names, key=fun1)    
print (n3)

n4 = sorted(names, key=lambda x: x[3])    
print (n4)