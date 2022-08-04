#hillcipher
import numpy as np

def encryption(pt, key, size):
	 # loop to append extra characters
	while(len(pt)%size!=0):
		pt+="x"
	pt = np.array([(ord(a)-97) for a in pt])
	#splits the array into equal parts
	ptm = np.array_split(pt,len(pt)/size)
	ct = ""
	for a in ptm:
		a = a.reshape(size,1)
		encr = np.dot(key,a)%26
		for a in np.nditer(encr):
			ct+=chr(a+97)
	return ct
	
def decryption(ct, key, size):
	adj = np.linalg.inv(key)
	det = round(np.linalg.det(key))
	adj = adj*det  # inverse*det = adjacent matrix
	#np.where() to add all the negative numbers 
	np.where(adj<0,adj+26,adj)
	# loop to find the inverse which is used to multiply with matrix
	x = 1
	while((det*x)%26!=1):
		x+=1

	final = (x*adj)%26 #final is the inverse matrix of the key
	enc = np.array([(ord(a)-97) for a in ct])
	encm = np.array_split(enc,len(enc)/size) #spliting it into equal sizes
	decrypt = ""
	for a in encm:
		a = a.reshape(size,1)
		decr = np.round_(np.dot(final,a))
		decr = decr.astype(int)
		decr = decr%26
		for a in np.nditer(decr):
			decrypt+=chr(a+97)
	return decrypt
	

pt = input("Enter the plain text ")
pt = pt.lower()
size = int(input("Enter the size of the key "))
if(size != 2 and size != 3):
	print("Size must be either 2 or 3")
	exit(0)
print("Enter the key row wise\n")
key = []
for i in range(size*size):
	key.append(int(input(f"Enter Element {i} ")))
key = np.array(key)
key = key.reshape(size,size)
print("\n\nThe key received is ")
print(key)

cipher = encryption(pt, key, size)
print("\nEncrypted text is: ", cipher)

decryptedText = decryption(cipher, key, size)
print("\nDecrypted text is: ", decryptedText)
