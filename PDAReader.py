
from tasukete import *

# pda = open("PDA.txt")
# print(pda.readlines())
# pda.close()


#Bagian ini dipakai sampai ngebaca sebelum fungsi transisi
pda = open("PDA.txt")
state = ((pda.readline()).rstrip()).split()
input_simbol = ((pda.readline()).rstrip()).split()
stack_simbol = ((pda.readline()).rstrip()).split()
start_state = ((pda.readline()).rstrip()).split()
start_stack = ((pda.readline()).rstrip()).split()
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



isiHTML = ['html', 'head', 'img', 'src', '/', 'title', '/title', '/head','body','/body', '/html']
#print(transition_function)

state = start_state
stack = start_stack
accepting = accepting_state

# print(currentState)
# print(currentStack)
# print(accepting)

# print(stack)

# print(parsingStack("e"))

# flag = False

#print(parsingStack("tes"))

# print(listToString(state))
# print(stack)
# print(accepting)


for masukkan in isiHTML:
    flag = False
    for transisi in transition_function:
        #print(transisi)
        if (listToString(state) == currentState(transisi) and stack[-1] == topFromStack(transisi) and masukkan == alphabetInput(transisi)):
            state = nextState(transisi)
            elemen = parsingStack(addToStack(transisi))
            if (elemen == 'e'): 
                stack.pop()
            elif (elemen != stack[-1]):
                stack.append(elemen)
            flag = True
    print(stack)
    if (flag == False):
        exit("Syntax Error")

for i in accepting_state:
    if (state == i):
        exit("Berhasil")
           
exit("Syntax Error")

            


            

            



        
    








#pantransisiang_baris = len(transition_function)

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




