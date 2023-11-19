
from tasukete import *

# pda = open("PDA.txt")
# print(pda.readlines())
# pda.close()


#Bagian ini dipakai sampai ngebaca sebelum fungsi transisi
pda = open("PDA.txt")
state = ((pda.readline()).rstrip()).split()
input_simbol = ((pda.readline()).rstrip()).split()
start_state = ((pda.readline()).rstrip()).split()
start_stack = ((pda.readline()).rstrip()).split()
accepting_stack = ((pda.readline()).rstrip()).split()
accepting_state =  ((pda.readline()).rstrip()).split()
kondisi = ((pda.readline()).rstrip()).split()
pda.close()


#Bagian ini buat ngebaca fungsi transisi
pda = open("PDA.txt")
temp = pda.readlines()
pda.close()

count = 0
transition_function = []
panjang_baris = len(temp)
for i in range( panjang_baris):
    if i >= 7:        
        transition_function.append(temp[i].rstrip().split())







#panjang_baris = len(transition_function)

#for i in range(panjang_baris):
#    print(addToState(TRANSITION_FUNCTION[i]))

#print(TRANSITION_FUNCTION)

# # Quick Examples of Appending to File

# # Append to file using the write() method
# with open('file.txt', 'a') as f:
#     f.write('I am appended text\n')

# # Redirect the output of the print() to a file
# with open('file.txt', 'a') as f:
#     print('I am appended text', file=f)

# # Manually closing file
# file = open('file.txt', 'a')
# file.write('I am appended text\n')
# file.close()

    

# print(state)
# print(input_simbol)
# print(start_state)
# print(start_stack)
# print(accepting_stack)
# print(accepting_state)
# print(kondisi)
# print(transition_function)




