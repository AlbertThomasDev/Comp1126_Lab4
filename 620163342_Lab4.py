import sys
sys.setrecursionlimit(1000000)

def excludePunNum(str_lst):
    #print(str_lst)
    new_str = ""
    for i in range(0,len(str_lst)):
        #print(str_lst[i])
        if str_lst[i] not in (",",".","?","!",";",":","-","^") + ("0","1","2","3","4","5","6","7","8","9"):
            #print("does not exsist")
            new_str = new_str + str_lst[i]
    return new_str  


def encoded_string(enc_str):
    if enc_str == "":
        return ""
    if ord(enc_str[0])%2 == 0:
        return chr(ord(enc_str[0]) + 4) + encoded_string(enc_str[1:])
    else:
        return chr(ord(enc_str[0]) + 2) + encoded_string(enc_str[1:])
        

def decoded_string(dec_str):
    if dec_str == "":
        return ""
    if ord(dec_str[0])%2 == 0:
        return chr(ord(dec_str[0]) - 4) + decoded_string(dec_str[1:])
    else:
        return chr(ord(dec_str[0]) - 2) + decoded_string(dec_str[1:])

def stringList(str1):
 return str1.split()


#reverse encodedList function
def encodedList(lst):
    if lst == []:
        return []
    else:
        return encodedList(lst[1:]) + [encoded_string(lst[0])]

def decodedList(lst):
    if lst == []:
        return []
    else:
        return decodedList(lst[1:]) + [decoded_string(lst[0])]

def main(s):
    slst=excludePunNum(s)
    eList = encodedList(stringList(slst))
    dList = decodedList(eList)
    print("Given string =>", s)
    print("Punctuation removed =>", slst)
    print("List Encoded =>", eList)
    print("List Decoded =>", dList)
    print("Encoded Message =>",' '.join(eList))    
