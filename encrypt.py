import random

def encrypt(character):

    main_count = 0

    key = []

    count = 0

    keyint = random.randint(65, 127)

    bin1 = str(bin(keyint)[2:])

    for i in bin1:
        key.append(int(i))
        count += 1


    binary = str(bin(ord(character))[2:])
    plaintext = []
    ciphertext = []
    c = 0
    c2 = 0

    for i in binary:
        plaintext.append(int(i))
        c += 1
        
    for i in key:

        if ((i or plaintext[c2]) == 1) and ((i and plaintext[c2]) != 1):
            b1 = 1
            
            ciphertext.append(str(b1))

        else:
            b1 = 0
            
            ciphertext.append(str(b1))

        c2 += 1
        
    result = ''.join(ciphertext)
    return result
     
string = input("Enter string: ")

for h in string:
    print(chr(int(encrypt(h))), end = '')
