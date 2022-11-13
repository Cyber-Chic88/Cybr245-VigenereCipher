import random
import time

msg = "Hello World!"
key = []
text_list = []
enc_list = []
dec_list = []
dec_text = []

def seed_gen():
    random.seed(time.time())
    for i in range(12):
        key.append(random.randint(0,1000))
    return(key)

def enc_msg(msg, key):
    for char in msg:
        char = ord(char)
        text_list.append(char)
    #print("The orig msg in ord is : " , text_list) 

    for i in range(0, len(text_list)):
        for j in range(len(key)):
            x = (key[j] ^ text_list[i])
        enc_list.append(x)
    enc_text = [chr(enc_list[i])for i in range(0, len(enc_list))]
    lst_str1 = ''.join([str(i) for i in enc_text])
    #print("The encrypted msg in ord is : ", enc_list)
    return(lst_str1)


def dec_msg(lst, key):
    for i in range(0, len(enc_list)):
        for j in range(len(key)):
            x =  enc_list[i] ^ key[j]
        dec_list.append(x)
    dec_text = [chr(dec_list[i])for i in range(0, len(dec_list))]
    lst_str2 = ''.join([str(i) for i in dec_text])
    #print("The deciphered msg in ord is : ", dec_list)
    return(lst_str2)

def main():
    print("The orig msg is :", msg)
    print("The encryption key is : ", seed_gen())
    print("The encrypted msg is: ", enc_msg(msg, key))
    print("The decrypted msg is: ", dec_msg(enc_list, key))
main()
