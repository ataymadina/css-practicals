import random
from hashlib import sha256

def coprime(a,b):
    while b != 0:
        a, b = b, a % b
    return a
    
def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

#Euclid's extended algorithm for finding the multiplicative inverse of two numbers    
def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise Exception('Modular inverse does not exist')
	return x % m    
        
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Numbers Are Not Prime!!!')
    elif p == q:
        raise ValueError('Both Numbers Are Same,Try Different Numbers!!!')

    n = p * q

    #Phi is the totient of n
    phi = (p-1) * (q-1)

    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    #Use Euclid's Algorithm to verify that e and phi(n) are comprime 
    g = coprime(e, phi)
  
    while g != 1:
        e = random.randrange(1, phi)
        g = coprime(e, phi)

    #Use Extended Euclid's Algorithm to generate the private key
    d = modinv(e, phi)

    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(privatek, plaintext):
    #Unpack the key into it's components
    key, n = privatek

    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
            
    numberRepr = [ord(char) for char in plaintext]
    print("\n\nNumber Representation(Before Encryption).....\n", numberRepr)
    cipher = [pow(ord(char),key,n) for char in plaintext]
    
    #Return the array of bytes
    return cipher


def decrypt(publick, ciphertext):
    #Unpack the key into its components
    key, n = publick
       
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    numberRepr = [pow(char, key, n) for char in ciphertext]
    plain = [chr(pow(char, key, n)) for char in ciphertext]

    print("\n\nNumber Representation(After Decryption).....1\n", numberRepr)
    
    #Return the array of bytes as a string
    return ''.join(plain)
       
def hashFunction(message):
    hashed = sha256(message.encode("UTF-8")).hexdigest()
    return hashed
    
def verify(receivedHashed, message):
    ourHashed = hashFunction(message)
    if receivedHashed == ourHashed:
        print("Verification is Successful", )
        print(receivedHashed, " = ", ourHashed)
    else:
        print("Verification is Failed")
        print(receivedHashed, " != ", ourHashed)
        
def main():
    p = int(input("Enter 1st Prime Number =>"))
    q = int(input("Enter 2nd Prime Number =>")
    public, private = generate_keypair(p, q)
    print("\nPublic Key  => ", public)
    print("Private Key => ", private)
    message =input("\n\nEnter Message To Encrypt(Using Private Key) =>")

    hashed = hashFunction(message)
    encrypted_msg = encrypt(private, hashed)   
    print("\nEncrypted Message =>")
    print(''.join(map(lambda x: str(x), encrypted_msg)))

    decrypted_msg = decrypt(public, encrypted_msg)
    print("\nDecrypted Message(Using Pbulic Key) => ")  
    print(decrypted_msg)
    print("")
    print("\n\n1Verification Of Encryption & Decryption...")
    verify(decrypted_msg, message)
   
main()  