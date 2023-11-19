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
def addToStack(fungsi_transisi):
    return fungsi_transisi[4]

#list ke string
def listToString(list):
    listResult = ""
    for elemen in list:
        listResult += elemen
    
    return listResult

#def parsting isi teks
def parsingStack(list):
    hasil = ""
    for elemen in list:
        hasil += elemen
        if elemen == ">":
            break
    return hasil




#Update kondisi Acceptance
#def updateAcceptance(file, kondisi):