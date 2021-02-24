# Συναρτηση ολισθησης του μηνυματος με τον αριθμο(δεικτη) που θελουμε να ολισθησουμε.
def rot(msg, n):
    return msg[n:] + msg[:n]  # returns number_before_mod list of bits

# Συναρτηση xor
def xor(part1, part2):
    # αρχικοποιουμε τη λιστα c με μηδενικα παντου και με μηκος οσο αυτο του πρωτου ορισματος
    # της συναρτησης
    c = [0] * len(part1)
    for x in range(len(part1)):
        # Εαν η διαφορα τους ειναι μηδεν
        # τοτε εχουμε 1 bit - 1  0 - 0 που λογω xor μας κανει 1.
        if (part1[x] - part2[x] == 0):
            c[x] = 1
    return c

def decrypt(ciphertext):
    c2 = rot(ciphertext, 2)
    c4 = rot(ciphertext, 4)
    c10 = rot(ciphertext, 10)
    c12 = rot(ciphertext, 12)
    c14 = rot(ciphertext, 14)
    decr = xor(ciphertext, xor(c12, xor(c2, xor(c10, xor(c14, xor(c10, c4))))))
    return decr

# Εναρξη του κυριου προγραμματος
if __name__ == "__main__":
    # Ζηταμε να μας δωσει ο χρηστης εισοδο με την συγκεκριμενη μορφη για να δουλεψει ο αλγοριθμος
    print('msg 16-bit paradeigma 1 0 0 1 1 1 0 1 1 0 1 1 1 0 0 0\n')
    # Αποθηκευουμε το μηνυμα που πηραμε προηγουμενως σε μια λιστα 16 θεσεων, οσα δηλαδη και τα bit του μηνυματος.
    m = list(map(int, input("Eisagete bit tou mhnymatos : \n").strip().split()))[:16]
    print(f"Arxiko mhnyma---------------->{m}")

    c = xor(m, xor(rot(m, 6), rot(m, 10)))
    print(f"kryptografhmeno mhnyma------->{c}")

    epilogh = input("Gia na deite to apoktyptografhmeno mhnyma pathste (u) diaforetika pathste (n): ")
    if epilogh == 'u':
        # καλουμε τη συναρτηση αποκρυπτογραφησης με ορισμα το ciphertext = xor(m, xor(rot(m, 6), rot(m, 10)))
        # που υπολογισαμε προηγουμενως
        decr= decrypt(c)
        print(f"Apokryptografhmeno mhnyma:--->{decr}")