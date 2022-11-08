def encrypt():
        encrypted=""
        text=input("Enter The Text : ")
        key=int(input("Enter The key : "))
        for i in range(len(text)):
                ele=text[i]
                if (text.isupper()):
                    encrypted += chr((ord(ele)+ key - 65)% 26+65)
                
                elif(text[i] == " "):
                    encrypted += " "
                    
                else:
                    encrypted += chr((ord(ele)+ key - 97)% 26+97)
                
        print("Encrypted Text : ",encrypted)
