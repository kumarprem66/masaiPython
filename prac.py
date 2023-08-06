import numpy as np


file_name = "data.txt"

with open(file_name,'w') as file:
    file.write("Hello World")



with open(file_name,'r') as file:
    data = file.read()


li = data.split(" ")
print(li)

out = "output.txt"
with open(out,'w') as file:
    file.write("Number of words : "+str(len(li)))












