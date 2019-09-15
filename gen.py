import string

#casing = input('enter number of letters: ')

#print(casing)

alphabet1 = ['s','S'] 
alphabet2 = ['d','e','f','D','E','F']
alphabet3 = ['r','R']
alphabet4 = ['v','w','x','y','z','V','W','X','Y','Z']
alphabet5 = ['j','k','l','J','K','L']
alphabet6 = ['j','k','l','J','K','L']
alphabet7 = ['r','R']


string=''
file = open("LIST.txt","w")
for x in alphabet1:
    for y in alphabet2:
        for z in alphabet3:
             for a in alphabet4:
                  for b in alphabet5:
                       for c in alphabet6:
                           for d in alphabet7:
                                string+=x
                                string+=y
                                string+=z
                                string+=a
                                string+=b
                                string+=c
                                string+=d
                                string+='\n'

file.write(string+'\n')
string=''
file.close()
print ('DONE!')





