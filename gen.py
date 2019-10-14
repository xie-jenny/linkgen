import itertools
import string


noalpha = input('how many alphabets? ')


print(noalpha)

alphabets = []

for i in range (0,int(noalpha)):
   input_string = input("Enter list elements of the {}th alphabet separated by spaces: ".format(i+1))
   alphabets.append(input_string.split(' '))



file = open("LIST.txt",'w')
for n in itertools.product(*alphabets):
   file.write(''.join(n))
   file.write('\n')


file.close()
print('done.')

