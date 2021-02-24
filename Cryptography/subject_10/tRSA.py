import fast
N, e = 11413, 19
C = [3203,909,3143,5255,5343,3203,909,9958,5278,5343,9958,5278,4674,909,9958,792,909,4132,3143,9958,3203,5343,792,3143,4443]

# Βρίσκουμε τους παράγοντες του αριθμού Ν
factors = []
for i in range(1, N + 1):
    # κάθε φορά που ένας αριθμός από 1 μεχρι Ν διαιρεί το N τον αποθηκεύουμε στη λίστα factors
    if N % i == 0:
        factors.append(i)
# Τώρα θα κρατησουμε ποιοι από αυτους που είναι πρώτοι έχουν άθροισμα N
# Οι αριθμοί αυτοί θα είναι και οι p,q
prime_factors = []

# Πρώτα ελέγχουμε αν οι παράγοντες που βρήκαμε παραπάνω είναι πρώτοι
# χρησιμοποιήσαμε τον κώδικα από εδώ->
# https://www.programiz.com/python-programming/examples/prime-number-intervals
for k in range(1, N + 1):
    if k > 1:
        for i in range(2, k):
            if (k % i) == 0:
                break
        else:
            for i in range(len(factors)):
                if(k==factors[i]):
                    prime_factors.append(k)

# Σειρά παίρνει ο έλεγχος για ποιοι πρώτοι αριθμοί αν τους πολλαπλασιασουμε βγάζουν γινομενο Ν
for i in range(len(prime_factors)):
    for j in range(1,len(prime_factors)):
    # Έλεγχος αν οι αριθμοί βγάζουν γινόμενο N
        if (prime_factors[i]*prime_factors[j] == N):
            p = prime_factors[i]
            q = prime_factors[j]

# Βρίσκουμε το fn
fn = (p-1)*(q-1)

# τώρα βρισκουμε το κλειδι με το οποίο έγινε η κρυπτογράφηση
# θέλουμε έναν αριθμό x δηλαδη τέτοιον ώστε: e * x mod fn = 1
for x in range(fn):
    if ((e * x) % fn == 1):
         d = x

msg = ''
# το i ειναι το καθε block του c
# για κάθε μπλοκ του c i^d mod N με d private key
for i in C:
    # print(i)--> Το εσωτερικό του C
    # αποκρυπτογραφούμε block by block όπως λέει η εκφώνηση
    # 3203 --> αντιστοιχεί στο πρτο γραμμα του μηνυματος κοκ..
    k = fast.fast(i,d,N)
    # chr() επιστρέφει το integer k στη unicode μορφή του
    # κάθε φορά προσθέτουμε στο μήνυμα το επόμενο αποκρυπτογραφημένο γράμμα του C
    msg += chr(k)
    # print(msg) # για ελεγχο
print(f"To encrypted mhnyma einai: {msg}")