import random
import fast

def millerabin(n):
    s = n-1
    k=0
    while (s / (2**k)) % 1 == 0: # αλλάζουμε το / με // για μεγάλους αριθμούς
        m = (s / (2**k))
        k = k+1
    k=k-1

    # δημιουργία τυχαία βάσης από το σύνολο {2...n-1}
    a = random.randrange(2 ,n-1)
    flag=0
    i=0
    bo = fast.fast(a, int(m), n)
    while i < k:
        b1 = fast.fast(bo, 2, n)
        if b1 == n - 1 or bo == n-1:
            flag+=1
        elif b1 == 1 or bo == 1:
            flag+=1
        else:
            fast.fast(b1, 2, n)
        i = i + 1
    if flag==0:
        return False
    else:
        return True

if __name__ == '__main__':
    # δουλευει για μικρούς πρώτους ενώ για 1300 bit αργεί πολύ!
    # συνεπώς η def millerabin εχει λάθος implementation για large primes
    # κανονικά κάνουμε βάζουμε σε loop το n = random.randrange(2 ** (1299), 2 ** (1300))
    # και το περνάμε στον παρακάτω έλεγχο μέχρι να μας δώσει true και έτσι θα κάνει
    # generate 1300 bit large prime με το miller rabin
    n = 443
    if millerabin(n)==True:
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")
