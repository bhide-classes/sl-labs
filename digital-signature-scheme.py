def modInverse(a, m):
     
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1
    
p = int(input("Enter prime number p:-"))
q = int(input("Enter prime number q:-"))
e = int(input("Enter prime e:-"))

msg = int(input("Enter the msg:-"))

n = p*q
phin = (p-1)*(q-1)

d = modInverse(e,phin)

print("private key:-",d)
print("public key:-",n)

signature = (msg^d)%n
msg1 = (signature^e)%n

if(msg==msg1):
    print(f"""
    msg = {msg} and msg1 = {msg1}
    Since msg == msg1
    Digital Signature Verified
    """)
else:
    print("Digital Signature not Verified")
