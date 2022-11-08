# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def gcd(a, h):
	temp = 0
	while(1):
		temp = a % h
		if (temp == 0):
			return h
		a = h
		h = temp

def modInverse(a, m):
     
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1


p = int(input('Enter value of p:-'))
q = int(input('Enter value of q:-'))
n = p*q
e = int(input('Enter value of e:-'))
phi = (p-1)*(q-1)

while (e < phi):

	if(gcd(e, phi) == 1):
		break
	else:
		e = e+1

d = modInverse(e,phi)

msg = int(input('Enter the msg:-'))

print("Message data = ", msg)

encrypted_msg = (msg**e)%n
print("Encrypted data = ", encrypted_msg)

decrypt_msg = (encrypted_msg**d)%n
print("Decrypted Message = ",decrypt_msg)
