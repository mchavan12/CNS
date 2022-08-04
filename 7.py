import math

p = int(input("P = "))
q = int(input("Q = "))
m = int(input("Message = "))

n = p*q
x = (p-1)*(q-1)

e = 2
while(e<x):
    if(math.gcd(e,x)==1):
        break
    else:
        e = e + 1
print("e = ",e)

d = 1
while((d*e)%x != 1):
    d = d+1
print("d = ",d)

C = pow(m,e,n)
print("Encrypted = ",C)
D = pow(C,d,n)
print("Decrypted = ",D)
