import random
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def findPrimitive(modulo):
    roots = []
    required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)

    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            roots.append(g)          
    return roots


if __name__ == '__main__':

	P = int(input("Enter the prime number:-"))
	primitives = findPrimitive(P)
	G = random.choice(primitives)
	
	print('The Value of P is :%d'%(P))
	print("Primitive roots are",primitives)
	print('The Value of G is :%d'%(G))
	a = 4
	print('The Private Key a for Alice is :%d'%(a))

	x = int(pow(G,a,P))

	b = 3
	print('The Private Key b for Bob is :%d'%(b))

	y = int(pow(G,b,P))
	
	ka = int(pow(y,a,P))
	
	kb = int(pow(x,b,P))
	
	print('Secret key for the Alice is : %d'%(ka))
	print('Secret Key for the Bob is : %d'%(kb))


