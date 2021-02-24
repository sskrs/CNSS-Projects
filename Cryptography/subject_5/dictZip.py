import zipfile

zip = input("Enter zip file (test_zip.zip) : ")
dict = input("Enter dictionary file (english.txt): ")

# Χρησιμοποιούμε την zipfile.ZipFile για να επεξεργαστούμε το zip
zip = zipfile.ZipFile(zip)
# παράμετρο rb γιατι κάνει collision με το pwd παρακατω και δεν θα βγαλει αποτέλεσμα.
# θέλουμε να ανοίξει η λίστα με τους κωδικούς σε binary format.
with open(dict, "rb") as dict:
    # για κάθε password στο file dict δοκίμασε να ανοίξεις το zip.
    for i in dict:
        try:
            # επειδή θέλουμε να ανοίξουμε encrypted zip χρησιμοποιούμε μόνο την παράμετρο pwd
            zip.extractall(pwd=i.strip())
        except:
            pass
        else:
            print("password:", i.decode())
            break