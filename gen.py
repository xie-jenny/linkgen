import itertools
import string


noalpha = input('how many alphabets? ')


print(noalpha)

alphabets = []

for i in range (0,int(noalpha)):
   input_string = input("Enter list elements of the {}th alphabet separated by spaces: ".format(i))
   #collection[i] = []
   alphabets.append(input_string.split(' '))


# test data
b = ['1','2','3']
c = ['A','B','C']




file = open("LIST.txt",'w')
for n in itertools.product(*alphabets):
   file.write(''.join(n))
   file.write('\n')


file.close()
print('done.')

