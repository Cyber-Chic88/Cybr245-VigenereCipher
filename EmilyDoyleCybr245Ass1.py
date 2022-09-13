def Key(filename, key):
    filename=open('', 'r')
    key = list(key)
    if len(filename) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
     
def Encrypt(filename, key):
    filename= open('','r')
    output_file= open('_copy.html', 'w')
    Enc_msg = []
    for i in range(len(filename)):
        x = (ord(filename[i]) +
             ord(key[i])) % 26
        x += ord('A')
        Enc_msg.append(chr(x))
    return("" . join(Enc_msg))
     

def Deciph(output_file, key):
    output_file= open('_copy.html', 'r')
    orig_text = []
    for i in range(len(output_file)):
        x = (ord(output_file[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))
     
# Driver code
if __name__ == "__main__":
    string = "ILOVECRYPTOGRAPHY"
    keyword = "CIPHER"
    key = Key(filename, keyword)
    Enc_msg = Encrypt(filename,key)
    print("Encrypted Message :", Enc_msg)
    print("Original/Decrypted Text :",
           Deciph(Enc_msg, key))
