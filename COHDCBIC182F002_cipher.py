
def encrypt():
    print('Do you want to encrypt or decrypt a message?') 
    print('1.Encrypt \n2.Decrypt')
    mode=0
    mode=int(input()) #storing the encryption or decryption in variable mode    
    print('Enter your message:')
    message = input()
    key = 0
    print('Enter the key number (1-26)') #they number that will shift the letters
    key = int(input())
    
    if mode == 2: #if decryption is selected change the value of the key as minus value
       key = -key
        
    translated = '' #adding empty space

    for symbol in message:
        if symbol.isalpha(): #if the message is only has capital or simple alphabet lettrs 
            num = ord(symbol) #get the ASCII value of the letter
            num = num + key   #add the key value to the previous ascii value

            if symbol.isupper(): #if the letter is capital
                if num > ord('Z'): #if the value of the num is greater than the ascii value of Z
                    num = num - 26
                elif num < ord('A'): #if the value of the num is lower than the ascii value of A
                     num = num + 26
            elif symbol.islower():
                if num > ord('z'): #if the value of the num is greater than the ascii value of z
                    num = num - 26
                elif num < ord('a'): #if the value of the num is lower than the ascii value of a
                    num = num + 26
            translated = translated + chr(num)
        else:
            translated = translated + symbol
        print(translated)

encrypt()
