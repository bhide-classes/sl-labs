import math

def gcd(a, h):
	temp = 0
	while(1):
		temp = a % h
		if (temp == 0):
			return h
		a = h
		h = temp


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

k = 2
d = (1 + (k*phi))/e

msg = int(input('Enter the msg:-'))

print("Message data = ", msg)

c = pow(msg, e)
c = math.fmod(c, n)
print("Encrypted data = ", c)


