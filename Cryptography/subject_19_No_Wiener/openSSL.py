from Crypto.PublicKey import RSA
# Αποθηκεύσαμε το public key σε ένα εξωτερικό αρχείο με όνομα pkey.pem
f = open('pkey.pem','r')
key = RSA.import_key(f.read())
# το n ειναι το rsa modulus
print(f"RSA Modulus(N):{key.n}")
print(f"e: {key.e}")
# Μετατρέπουμε το integer σε binary
print(f"Μετατροπή Ν από integer σε binary:  {bin(key.n)}")
# Εκτελούμε την πράξη -2 για να μην υπολογίσει το '0b' που δηλώνει τη δυαδική μορφή του αριθμού.
print(f"RSA bits: {len(bin(key.n))-2}")

