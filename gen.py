import itertools
import string


noalpha = input('how many alphabets? ')


print(noalpha)

for i in range (0,int(noalpha)):
   input_string = input("Enter a list element separated by space: ")

   a = []
   a = input_string.split(' ')



b = ['1','2','3']
c = ['A','B','C']


alphabets = [a,b,c]


file = open("LIST2.txt",'w')
for n in itertools.product(*alphabets):
   file.write(''.join(n))
   file.write('\n')


file.close()
print('done.')

