names = ('Hari','Jina','Preet','Yug','Sanjay','Champa')

sortedName = sorted(names)

print (sortedName)

print (sorted(names, key=len))

names = ('Hari','Jina','Preet','Yug','Sanjay','Champa')

item1 = 'Hari'
item2 = 'Jina'

len(item1) > len(item2)

print (sorted(names, key=len))

maps = {'Name3':'Harikrushna','Name1':'Jinal','Name2':'Solia'}


item1 = 'Name3'
item2 = 'Name1'

item1 > item2



maps.get(item1) > maps.get(item2)===
        'Hari' > 'Jinal'

print (sorted(maps, key=maps.get))


def mycompare(ch):
    return 1;


