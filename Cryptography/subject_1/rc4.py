# Δημιουργούμε συνάρτηση για να κατασκευάσουμε την μετάθεση S
# σύμφωνα με τον αλγόριθμο 3.2.1 που δίνεται στις σημειώσεις.
def metathesh_s(seed):
    S=[]
    seedlen = len(seed)
    for i in range(256):
       S.append(i)
    j=0
    for i in range(256):
        j=(j + S[i] + seed[i % seedlen])% 256
        S[i], S[j] = S[j], S[i]
    return S


# συνάρτηση που βρίσκει την κλειδοροή του RC4 παίρνοντας ως είσοδο
# το s που παίρνουμε από τη συνάρτηση εύρεσης του seed (metathesh_s)
# και μεσω αυτης εξαγουμε τα bytes του κλειδιου
# και ως έξοδο θα πάρουμε προφανώς το κλειδί.
# η παρουσα συναρτηση βασιζεται στον αλγοριθμο 3.2.2
def keystream(S):
    i, j = 0, 0
    msg = "WEALLMAKEMISTAKESANDWEALLPAYAPRICE"
    plen = len(msg) # Μήκος κλειδιού = Μήκος μηνύματος
    key=[]
    while plen > 0:
        i = i+1 % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        key.append(k)
        plen = plen - 1

    return key


if __name__ == "__main__":
    # δηλώνουμε το κλειδί με το οποιο θα κρυπτογραφήσουμε/αποκρυπτογραφήσουμε
    key = "HOUSE"

    # το μετατρέπουμε σε μορφή unicode με χρήση της συνάρτησης transpose
    key = [ord(i) for i in key]
    #key = transpose(key, 'char', 'unicode')
   #print(key)
    while True:
        # o λόγος που κάνουμε ουσιαστικά το encrypt εδω ειναι για να κρατήσουμε την τιμή του encryptedmsg ώστε
        # να χρησιμοποιηθεί στην αποκρυπτογράφηση.
        # η παρούσα λύση δουλεύει για τη συγκεκριμένη περίπτωση.
        msg = "WEALLMAKEMISTAKESANDWEALLPAYAPRICE"
        # Για να μη μας εμφανίσει το παρακάτω error πρεπει να γίνει μετατροπή
        # του μηνύματος απο char σε unicode
        # TypeError: unsupported operand type(s) for ^: 'int' and 'str'
        msg = [ord(i) for i in msg]
        # Βρίσκω την μετάθεση του seed (όρισμα το seed)
        S = metathesh_s(key)
        # Βρίσκω την κλειδοροή του RC4 με όρισματα s και το μηνυμα που θελω να κρυπτογραφησω
        Key = keystream(S)
        # Πραγματοποιώ πράξη xor μεταξύ στοιχείων της κλειδοροής και του μηνύματος
        encryptedmsg = []
        plen = len(msg)
        for i in range(0, plen):
            encryptedmsg.append(Key[i] ^ msg[i])  # Τελεστής XOR = ^

        # Δίνουμε τη δυνατότητα στον χρήστη να επιλέξει τη θέλει να κάνει.
        epilogh = input("Plhktrologste (e) gia encryption, (d) gia decryption, otidhpote allo plhktro gia e3odo: ")
        if epilogh == 'e':
            # Για θέση της λίστας encryptedmsg μετατρέπουμε το περιεχόμενο της σε δεκαεξαδική μορφή και τα
            # παρουσιάζουμε όλα σε μία σειρα και έτσι έχουμε το encrypted μηνυμα μας σε δεκαεξαδικη μορφή
            print("To kryptografhmeno mhnyma einai: ")
            for i in encryptedmsg:
                print("%02X" % i, end="")
            # το κρυπτογραφημένο μήνυμα σε μορφή λίστας
            # print(f"{encryptedmsg}")


        elif (epilogh == 'd'):
            # εδώ θα πάρουμε το κρυπτογραφημένο μήνυμα το οποίο ειναι σε μορφη λίστας:
            # [15, 209, 180, 127, 243, 108, 217, 2, 44, 26, 97, 4, 208, 12, 237, 46, 66, 208, 209, 125, 12, 242, 253, 48, 7, 132, 194, 12, 2, 82, 153, 98, 31, 97]
            # και θα το κάνουμε decrypt
            #decryptmsg = decryption(key, encryptedmsg)

            S = metathesh_s(key)  # Βρίσκω την μετάθεση S
            # Βρίσκω την κλειδοροή του RC4 με όρισματα s και το κρυπτογραφημένο μηνυμα
            Key = keystream(S)
            decryptmsg = []
            msglen = len(encryptedmsg)
            for i in range(0, msglen):
                decryptmsg.append(Key[i] ^ encryptedmsg[i])

            print("To apokryptografhmeno mhnyma einai: ")
            decryptmsg = [chr(i) for i in decryptmsg]
            transp = ""
            for i in decryptmsg:
                transp += i
            #decryptmsg = transpose(decryptmsg,'unicode','char')
            print(transp)

        break