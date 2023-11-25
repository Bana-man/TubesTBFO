# fungsi bantuan buat dapet currentstate
def currentState(fungsi_transisi):
    return fungsi_transisi[0]

# fungsi bantuan buat dapet info inputan
def alphabetInput(fungsi_transisi):
    return fungsi_transisi[1]

# fungsi bantuan buat dapet info isi stack paling atas
def topFromStack(fungsi_transisi):
    return fungsi_transisi[2]

# fungsi bantuan buat dapet info nextState
def nextState(fungsi_transisi):
    return fungsi_transisi[3]

# fungsi bantuan buat dapet info yang harus di Add to Stack
def addToStack(fungsi_transisi):
    return fungsi_transisi[4]

# list ke string
def listToString(list):
    listResult = ""
    for elemen in list:
        listResult += elemen
    
    return listResult

# Parsing isi teks
def parsingStack(list):
    list_hasil = []
    hasil = ""
    count = 0
    i = 0
    for elemen in list:
        if (elemen == 'e' and i == 0):
            list_hasil.append('e')
            break
        hasil += elemen
        if elemen == ">" and count == 0:
            count += 1
            list_hasil.append(hasil)
            hasil = ""    
        if (count == 2):
            break
        i += 1
    list_hasil.append(hasil)

    return list_hasil
    
# Update kondisi Acceptance
# def updateAcceptance(file, kondisi):