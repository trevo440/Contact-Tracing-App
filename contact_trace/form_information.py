import pickle
#------------------------------------------  
def openloginfile():
    y = ''
    login = open('UserFile', 'rb')
    memry = pickle.load(login)
    for x in memry:
        y += (str(x) + ', ')
    return y
#------------------------------------------    
#Login Information (tkinter_main)
# z = openloginfile()
# print(z)
#------------------------------------------  
def openfile():
    y = ''
    patient = open('PatientFile', 'rb')
    memory = pickle.load(patient)
    for x in memory:
        y += (str(x) + ', ')
    return y
#------------------------------------------  
#Personal Information (tkinterapp)
# z = openfile()
# print(z)
#------------------------------------------  
def open_multi():
    info = ''
    contact = open('ContactFile', 'rb')
    mem = pickle.load(contact)
    for x in mem:
        info += str(x) + ', '
    empty = '0, 0, 0, 0, 0, '
    if empty in info:
        info = info.replace(empty, '')    
    return info
#------------------------------------------  
#Contact Information (tkinter_contacts)
#x = open_multi()
#print(x)            