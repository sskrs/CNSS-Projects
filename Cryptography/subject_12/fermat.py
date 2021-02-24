# αλγόριθμος Fermat βασισμένος στο 3.5.1
import random
import fast

# n = random
def fermat(n):
    # κάνουμε τον έλεγχο 512 φορές
    for i in range(512):
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
    # βάζουμε τον αριθμό 617 γιατι στο δεκαδικό σύστημα ενας αριθμός με 617 ψηφία ισούται στο
    # δυαδικό με έναν αριθμό 2048 bit.
    n = random.randrange(1, 10 **(617))
    # eternal loop μέχρι να μας επιστραφεί αριθμός με 2048 bit που να είναι πρώτος
    while fermat(n)==False:
        n = random.randrange(1, 10 ** (617))

        if fermat(n) == True:
            print(f"{n} einai prime")
        # else:
            # print(f"{n} is not prime")
