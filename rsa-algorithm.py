import math

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

c = pow(msg, e)
c = math.fmod(c, n)
print("Encrypted data = ", c)
