import re
import os


def ApakahAdaPangkat(var):
    variable = var.split('^')
    if (len(variable) > 1):
        return True
    else:
        return False


def ApakahAdaVar(var):
    variable = var.split('x')
    if (len(variable) > 1):
        return True
    else:
        return False


def turunan(var):
    suku = var.split('x')
    pangkatGabungan = suku[1].split('^')
    pangkat = int(pangkatGabungan[1].replace("(", "").replace(")", ""))
    if (suku[0] == ""):
        suku[0] = 1
    koefisien = int(suku[0])

    # --- di turunkan---
    koefisien = koefisien * pangkat
    pangkat = pangkat - 1

    # ---- penyusunan -----
    if koefisien > 0:
        tanda = "+"
    else:
        tanda = ""

    # --------Print-------------
    if pangkat == 1:
        print(tanda, koefisien, "x", end="", sep='')
    elif pangkat != 0:
        print(tanda, koefisien, "x^(", pangkat, ")", end="", sep='')
    else:  # pangkat=0
        print(tanda, koefisien, end="", sep='')


while True:
    os.system('cls')
    print("====================================================")
    print(" Masukkan polinomial yang akan di turunkan ")
    print("====================================================")
    polinom = input("f(x) = ")
    polinom = polinom.replace(" ", "")
    polinom = polinom.replace("-", "#-")

    y = re.split(r'[+#]', polinom)

    panjang = len(y)

    print("Turunan :")
    print("f'(x) = ", end="")
    for i in range(panjang):
        adaPangkat = ApakahAdaPangkat(y[i])
        if adaPangkat:
            turunan(y[i])
        else:
            adaVar = ApakahAdaVar(y[i])
            if adaVar:
                split = y[i].split('x')
                if split[0] == "":
                    split[0] = 1
                hasil = int(split[0])
                tanda = ""
                if hasil > 0:
                    tanda = "+"
                print(tanda, hasil, end="", sep='')

    jawaban = None
    while jawaban not in ("y", "n"):
        print("\n")
        print("==========================================")
        print("==== Apakah anda ingin mengulang?(y/n)  ==")
        print("==========================================")
        jawaban = input()
        if jawaban == "y":
            os.system('cls')
        elif jawaban == "n":
            exit()
        else:
            print("Masukkan 'y' atau 'n' ")
