# generate p,q πρώτους
# αλγόριθμος Fermat βασισμένος στο 3.5.1
import random
import fast

def fermat(n):
    for i in range(10):
        # δημιουργία τυχαίου αριθμού βάσης
        a = random.randint(1, n - 1)
        gcd = fast.fast(a,n-1,n) # a * 1 mod n
        # εαν το gcd(a,n) ειναι 1 το ο n ειναι πρωτος
        if gcd == 1:
            return True
        else:
            #επιστρέφει false εαν ο αριθμός ειναι σύνθετος
            return False
        return True


if __name__ == '__main__':
    # εδώ δημιουργούμε αριθμό που θέλουμε να ελεγξουμε αν ειναι πρώτος
    # βάζουμε τον αριθμό 155 γιατι στο δεκαδικό σύστημα ενας αριθμός με 155 ψηφία ισούται στο
    # δυαδικό με έναν αριθμό 512 bit.
    p = random.randrange(1, 10 **(155))
    #print(f"p: {p}\n")

    # eternal loop μέχρι να μας επιστραφεί αριθμός με 512 bit που να είναι πρώτος
    while fermat(p)==False:
        p = random.randrange(1, 10 ** (155))

        if fermat(p) == True:
            print(f"p:  {p}\n")
        # else:
            # print(f"{n} is not prime")

    q = random.randrange(1, 10 ** (155))
    #print(f"q:  {q}\n")

    # eternal loop μέχρι να μας επιστραφεί αριθμός με 512 bit που να είναι πρώτος
    while fermat(q) == False:
        q = random.randrange(1, 10 ** (155))

        if fermat(q) == True:
            print(f"q:  {q}\n")
        # else:
        # print(f"{n} is not prime")
    N=p*q

    print(f"N:  {N}\n")
    #print(N)
    e = (2**16)+1
    print(f"e:  {e}\n")

    #υπολογισμός d
    fn = (p-1)*(q-1)
    print(f"fn: {fn}")
    for d in range(fn):
        if (((e % fn) * (d % fn)) % fn == 1):
            print(f"d:  {d}\n")

    for dp in range(p):
        if (((e % p) * (dp % p)) % p == 1):
            print(f"dp:  {dp}\n")

    for dq in range(q):
        if (((e % q) * (dq % q)) % q == 1):
            print(f"dq:  {dq}\n")

    for qinv in range(p):
        if (((q % p) * (qinv % p)) % p == 1):
            print(f"qinv:  {qinv}\n")

