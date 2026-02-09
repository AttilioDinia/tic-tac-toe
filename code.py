#python code.py

import os
import random
import time

os.system("cls" if os.name == "nt" else "clear")

print("\033[1mTIC-TAC-TOE\033[0m")
print("Tu giocherai con le x")

p1 = "\033[2m1\033[0m"
p2 = "\033[2m2\033[0m"
p3 = "\033[2m3\033[0m"
p4 = "\033[2m4\033[0m"
p5 = "\033[2m5\033[0m"
p6 = "\033[2m6\033[0m"
p7 = "\033[2m7\033[0m"
p8 = "\033[2m8\033[0m"
p9 = "\033[2m9\033[0m"
pos = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

#Controllo vittoria
def tris():
    
    L = [p1, p2, p3, p4, p5, p6, p7, p8, p9]

    if L[0] == L[1] == L[2]:
        return True
    if L[3] == L[4] == L[5]:
        return True
    if L[6] == L[7] == L[8]:
        return True

    if L[0] == L[3] == L[6]:
        return True
    if L[1] == L[4] == L[7]:
        return True
    if L[2] == L[5] == L[8]:
        return True

    if L[0] == L[4] == L[8]:
        return True
    if L[2] == L[4] == L[6]:
        return True

    return False

def pareggio():
    if p1 != "\033[2m1\033[0m" and p2 != "\033[2m2\033[0m" and p3 != "\033[2m3\033[0m" and p4 != "\033[2m4\033[0m" and p5 != "\033[2m5\033[0m" and p6 != "\033[2m6\033[0m" and p7 != "\033[2m7\033[0m" and p8 != "\033[2m8\033[0m" and p9 != "\033[2m9\033[0m":
        return True
    return False

while True:
    
    def tb():
        return f"\n {p1} | {p2} | {p3} \n---+---+---\n {p4} | {p5} | {p6} \n---+---+---\n {p7} | {p8} | {p9} \n"
    
    print(tb())

    scelta = input("Inserici la tua posizione da 1 a 9: ")
    os.system("cls" if os.name == "nt" else "clear")

    if scelta not in pos:
        os.system("cls" if os.name == "nt" else "clear")
        print("\033[1mScegli un numero da 1 a 9\033[0m")
        continue

    #Utente
    if scelta == "1":
        p1 = "\033[1mx\033[0m"
    elif scelta == "2":
        p2 = "\033[1mx\033[0m"
    elif scelta == "3":
        p3 = "\033[1mx\033[0m"
    elif scelta == "4":
        p4 = "\033[1mx\033[0m"
    elif scelta == "5":
        p5 = "\033[1mx\033[0m"
    elif scelta == "6":
        p6 = "\033[1mx\033[0m"
    elif scelta == "7":
        p7 = "\033[1mx\033[0m"
    elif scelta == "8":
        p8 = "\033[1mx\033[0m"
    elif scelta == "9":
        p9 = "\033[1mx\033[0m"

    pos.remove(scelta)
    os.system("cls" if os.name == "nt" else "clear")

    if tris():
        print(tb())
        print("\033[1mHai vinto!\033[0m\n")
        break
    else:
        pass

    os.system("cls" if os.name == "nt" else "clear")

    if pareggio():
        print(tb())
        print("\033[1mPareggio!\033[0m\n")
        break
    else:
        pass

    #Computer
    print(tb())
    print("Il computer sta pensando...")
    time.sleep(2.5)

    def blocca():
        lb = []
        opsioni = ["\033[1mo\033[0m", "\033[1mx\033[0m"]

        # orizzontali
        if p1 == p2 and p1 in opsioni and "3" in pos:
            lb.append("3")
        if p2 == p3 and p2 in opsioni and "1" in pos:
            lb.append("1")
        if p1 == p3 and p1 in opsioni and "2" in pos:
            lb.append("2")

        if p4 == p5 and p4 in opsioni and "6" in pos:
            lb.append("6")
        if p5 == p6 and p5 in opsioni and "4" in pos:
            lb.append("4")
        if p4 == p6 and p4 in opsioni and "5" in pos:
            lb.append("5")

        if p7 == p8 and p7 in opsioni and "9" in pos:
            lb.append("9")
        if p8 == p9 and p8 in opsioni and "7" in pos:
            lb.append("7")
        if p7 == p9 and p7 in opsioni and "8" in pos:
            lb.append("8")

        # verticali
        if p1 == p4 and p1 in opsioni and "7" in pos:
            lb.append("7")
        if p4 == p7 and p4 in opsioni and "1" in pos:
            lb.append("1")
        if p1 == p7 and p1 in opsioni and "4" in pos:
            lb.append("4")

        if p2 == p5 and p2 in opsioni and "8" in pos:
            lb.append("8")
        if p5 == p8 and p5 in opsioni and "2" in pos:
            lb.append("2")
        if p2 == p8 and p2 in opsioni and "5" in pos:
            lb.append("5")

        if p3 == p6 and p3 in opsioni and "9" in pos:
            lb.append("9")
        if p6 == p9 and p6 in opsioni and "3" in pos:
            lb.append("3")
        if p3 == p9 and p3 in opsioni and "6" in pos:
            lb.append("6")

        # diagonali
        if p1 == p5 and p1 in opsioni and "9" in pos:
            lb.append("9")
        if p5 == p9 and p5 in opsioni and "1" in pos:
            lb.append("1")
        if p1 == p9 and p1 in opsioni and "5" in pos:
            lb.append("5")

        if p3 == p5 and p3 in opsioni and "7" in pos:
            lb.append("7")
        if p5 == p7 and p5 in opsioni and "3" in pos:
            lb.append("3")
        if p3 == p7 and p3 in opsioni and "5" in pos:
            lb.append("5")

        lb = list(set(lb))
        return lb

    if blocca():
        sceltarand = random.choice(blocca())
    else:
        sceltarand = random.choice(pos)

    if sceltarand == "1":
        p1 = "\033[1mo\033[0m"
    elif sceltarand == "2":
        p2 = "\033[1mo\033[0m"
    elif sceltarand == "3":
        p3 = "\033[1mo\033[0m"
    elif sceltarand == "4":
        p4 = "\033[1mo\033[0m"
    elif sceltarand == "5":
        p5 = "\033[1mo\033[0m"
    elif sceltarand == "6":
        p6 = "\033[1mo\033[0m"
    elif sceltarand == "7":
        p7 = "\033[1mo\033[0m"
    elif sceltarand == "8":
        p8 = "\033[1mo\033[0m"
    elif sceltarand == "9":
        p9 = "\033[1mo\033[0m"

    pos.remove(sceltarand)

    print(tb())

    os.system("cls" if os.name == "nt" else "clear")

    if tris():
        print(tb())
        print("\033[1mHai perso.\033[0m\n")
        break
    else:
        pass

    os.system("cls" if os.name == "nt" else "clear")