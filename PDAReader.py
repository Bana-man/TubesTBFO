
#Bagian ini dipakai sampai ngebaca sebelum fungsi transisi
PDA = open("PDA.txt")
STATE = ((PDA.readline()).rstrip()).split()
INPUT_SIMBOL = ((PDA.readline()).rstrip()).split()
START_STATE = ((PDA.readline()).rstrip()).split()
START_STACK = ((PDA.readline()).rstrip()).split()
ACCEPTING_STACK = ((PDA.readline()).rstrip()).split()
ACCEPTING_STATE =  ((PDA.readline()).rstrip()).split()
KONDISI = ((PDA.readline()).rstrip()).split()
PDA.close()


#Bagian ini buat ngebaca fungsi transisi
PDA = open("PDA.txt")
TEMP = PDA.readlines()
PDA.close()

count = 0
TRANSITION_FUNCTION = []
panjang_baris = len(TEMP)
for i in range( panjang_baris):
    if i >= 7:        
        TRANSITION_FUNCTION.append(TEMP[i].rstrip().split())


#fungsi bantuan buat dapet currentstate
def currentState(fungsi_transisi):
    return fungsi_transisi[0]

#fungsi bantuan buat dapet  info inputan
def alphabetInput(fungsi_transisi):
    return fungsi_transisi[1]

#fungsi bantuan buat dapet  info isi stack paling atas
def topFromStack(fungsi_transisi):
    return fungsi_transisi[2]

#fungsi bantuan buat dapet  info nextState
def nextState(fungsi_transisi):
    return fungsi_transisi[3]

#fungsi bantuan buat dapet  info yang harus di Add to Stack
def addToState(fungsi_transisi):
    return fungsi_transisi[4]

panjang_baris = len(TRANSITION_FUNCTION)


#for i in range(panjang_baris):
#    print(addToState(TRANSITION_FUNCTION[i]))

#print(TRANSITION_FUNCTION)



    
"""
print(STATE)
print(INPUT_SIMBOL)
print(START_STATE)
print(START_STACK)
print(ACCEPTING_STACK)
print(ACCEPTING_STATE)
print(KONDISI)
print(TRANSITION_FUNCTION)
"""




