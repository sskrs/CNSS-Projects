import random
import string

def encryption(file):
    f = open(file, 'r')
    file_contents = f.read()
    message = file_contents
    # Μετατρέπουμε το plaintext που πήραμε στην είσοδο σε ascii
    m = [ord(c) for c in message]
    # Υπολογίζουμε το μήκος του plaintext σε ascii
    # θα το χρειαστούμε για να δημιουργήσουμε ενα κλειδί με ίδιο μήκος
    m_length = len(m)
    # Δημιουργούμε το κλειδί ιδιου μεγέθους με το μήνυμα
    # και το αποθηκευουμε στο otpkey.txt
    l = 0
    key = []
    while (l < m_length):
        k = random.SystemRandom()
        k = k.choice(string.printable) #συνδυασμός ascii χαρακτήρων: digits, ascii_letters, punctuation, and whitespace.
        k = ord(k)
        key.append(k)
        l = l + 1
    writeFile(key, 'otpkey.txt')
    #print(key)
    ciphertext = [a^b for a,b in zip(m,key)]
    # Aποθηκεύουμε το μήνυμα που μόλις κρυπτογραφήσαμε σε ένα αρχείο με το όνομα ciphertext.txt
    writeFile(ciphertext, 'ciphertext.txt')
    f = open('ciphertext.txt', 'r')
    file_contents = f.read()
    print(f"to encrypted mhnyma einai: {file_contents}")
    f.close()
    return ciphertext

def decryption(file):
    # Get ciphertext text
    f = open(file, 'r')
    file_contents = f.read()
    ciphertext = file_contents
    # Μετατρέπουμε το ciphertext που πήραμε στην είσοδο σε ascii
    c_m = [ord(c) for c in ciphertext]
    f_key = open("otpkey.txt", 'r')
    file_contents_key = f_key.read()
    key = file_contents_key
    k = [ord(c) for c in key]     # μετατροπη key σε ascii
    plaintext = [a^b for a,b in zip(c_m,k)]
    writeFile(plaintext, 'plaintext.txt')
    f = open('plaintext.txt', 'r')
    file_contents = f.read()
    print(f"to arxiko mhnyma htan: {file_contents}")
    f.close()
    return plaintext

def writeFile(file, txt):
    wf, wk = open(txt, 'w'), []
    for i in file:
        wk.append(str(chr(i)))
    wf.write(''.join(wk))

if __name__ == "__main__":
    # Δίνουμε την επιλογή στον χρήστη να επιλέξει αν θέλει κρυπτογράφηση ή αποκρυπτογραφηση
    epilogh = input("Plhktrologste (e) gia encryption, (d) gia decryption, otidhpote allo plhktro gia e3odo: ")
    if epilogh == 'e':
        file = input('Eisagete to file gia encryption: ')
        # το αρχειο που θα εισάγει ο χρήστης θα το χρησιμοποιήσουμε για να κανουμε την κρυπτογραφηση
        encryption(file)
    elif epilogh == 'd':
        # το αρχειο που θα εισάγει ο χρήστης θα το χρησιμοποιήσουμε για να κανουμε την αποκρυπτογραφηση
        file = input('Eisagete to file gia decryption: ')
        decryption(file)


