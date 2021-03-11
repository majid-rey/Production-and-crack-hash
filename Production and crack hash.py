import hashlib
import csv
import time
import datetime
from numpy.random import randint
def hash_password():
    it = input("Please enter a password : ")
    hashedWord1 = hashlib.sha256(it.encode()).hexdigest()
    hashedword2 = hashlib.md5(it.encode()).hexdigest()
    hashedword3 = hashlib.sha384(it.encode()).hexdigest()
    hashedword4 = hashlib.sha512(it.encode()).hexdigest()
    hashedword5 = hashlib.sha1(it.encode()).hexdigest()
    
    s = "\n hash sha512 : %s \n\n hash sha256 : %s \n\n hash sha384 : %s \n\n hash sha1   : %s \n\n hash md5    : %s" %(hashedword4,hashedWord1,hashedword3,hashedword5,hashedword2)
    print(s)
    time.sleep(7.8)
    switch()

def Password_production():
    i = int(input("Enter the password value : (Entering number 0 its own program specifies the value) : "))
    
    if int(i) > 0 :
        
        if i < 64:
            pass_value = int(i)
        else:
            pass_value = 64
        s = randint(0, 10,pass_value) 
        str_pass = str()
        for sa in s:
            str_pass += str(sa)
    else:
        y = int(input("Enter the password strength : (0 : weak , 1 : Normal , 2 : Powerful , 3 : Excellent ) : "))
        if y > 2:
            pass_value = 16
            s = hashlib.md5(str(randint(-909, 100,pass_value)).encode()).hexdigest()
            str_pass = s[8:25]
        elif y == 2:
            pass_value = 12
            s = hashlib.md5(str(randint(-500, 100,pass_value)).encode()).hexdigest()
            str_pass = s[14:27]
        elif y == 1:
            pass_value = 8
            s = randint(0, 10,pass_value)
            str_pass = str()
            for sa in s:
                str_pass += str(sa)
        elif y < 1:
            pass_value = 4
            s = randint(0, 10,pass_value)
            str_pass = str()
            for sa in s:
                str_pass += str(sa)
        
    print("\n\n << ",str_pass," >> ")
    time.sleep(6.5)
    switch()


def Crack_Hash():
    print ( "\n\nPlease select a hash type :\n\n 1 : sha512 \n 2 : sha384 \n 3 : sha256 \n 4 : sha1 \n 5 : md5 ")
    stype = int(input("\nPlease enter : "))
    snum = int(input("\nPlease enter the value of the password : "))
    hash_word = input("Please enter hash : \n")
    uu = datetime.datetime.now()
    dic_hash = dict()
    onb = "9"
    for i in range(0,snum):
        onb += "9"
    num = int(onb)
    s = "%0" + str(snum) + "d"
    if stype == 1 :
        for hashret in range(0 , num):
            st = s %(hashret,)
            hashedWord = hashlib.sha512(st.encode()).hexdigest()
            dic_hash[hashedWord] = st
    elif stype == 2 :
        for hashret in range(0 , num):
            st = s %(hashret,)
            hashedWord = hashlib.sha384(st.encode()).hexdigest()
            dic_hash[hashedWord] = st
    elif stype == 3 :
        for hashret in range(0 , num):
            st = s %(hashret,)
            hashedWord = hashlib.sha256(st.encode()).hexdigest()
            dic_hash[hashedWord] = st
    elif stype == 4 :
        for hashret in range(0 , num):
            st = s %(hashret,)
            hashedWord = hashlib.sha1(st.encode()).hexdigest()
            dic_hash[hashedWord] = st
    elif stype == 5 :
        for hashret in range(0 , num):
            st = s %(hashret,)
            hashedWord = hashlib.md5(st.encode()).hexdigest()
            dic_hash[hashedWord] = st
    hack = dic_hash[hash_word]
    print ("\n\nHashed password : << ", hack , " >> \n")
    uu=datetime.datetime.now()-uu
    print (int(uu.total_seconds()))
    time.sleep(6.5)
    switch()
    

def switch():
    s = "\n\n 1 : Password Hash \n 2 : Password Production \n 3 : Crack Hash \n 4 : Exit  \n"
    print (s)
    s = int(input("Please select one of the options : ( 1 or 2 or 3 or 4 ) : "))
    if s == 1:
        hash_password()
    elif s == 2:
        Password_production()
    elif s == 3:
       Crack_Hash() 
    elif s == 4:
        return


switch()
time.sleep(5.5)
