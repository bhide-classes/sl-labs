def decrypt(text,key):
        decrypted=""
        for i in range(len(text)):
                ele=text[i]
                if (text.isupper()):
                    decrypted += chr((ord(ele)- key - 65)% 26+65)
                
                elif(text[i] == " "):
                    decrypted += " "
                    
                else:
                        decrypted += chr((ord(ele)- key - 97)% 26+97)
        print(f"Encrypted Text for key={key} is {decrypted}.")
input_str = input('Enter your string:-')

for i in range(26):
    decrypt(input_str,i)
