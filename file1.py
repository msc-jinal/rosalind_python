import os

"""file open function will open file in read mode
read() will read all the lines from file and give string 
readline() will read first line from your file and give string
readlines() will read whole file and give list of the file lines
file.name = give name of the file
file.mode = give mode of file
file.read(count) = will read specified number of characters from file
file.tell() = give current position within file
file.seek() = set line at defined position
os module is used to perform delete aand rename operation in file
os.rename("current file","rename file") = rename the existing file
os.remove() = remove or delete file
os.mkdir("test") = will create new directory
os.getcwd() = give current working directory
os.rmdir("test") = remove specified directory
os.chdir("path") = change directory


"""

f1 = open("reference.fasta","r")
print(type(f1.read()))
print(type(f1.readline()))
fullfile = (f1.readlines())
print(type(fullfile))
f1 = open("reference.fasta","r")
#print(f1.read())
#print(f1.name)
#print(f1.mode)
str= (f1.read(120))
pos = f1.tell()
#print(pos)
pos = f1.seek(10)

#s.rename("ref.fasta","reference.fasta")"""
os.mkdir("test")
#os.getcwd()
#os.rmdir("test")








