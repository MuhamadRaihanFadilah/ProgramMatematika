import re
import os


def ApakahPecahanSederhana(desimal):
    if desimal == 0.5:
        desimal = "1/2"
        return desimal
    elif desimal == 0.333:
        desimal = "1/3"
        return desimal
    elif desimal == 0.25:
        desimal = "1/4"
        return desimal
    elif desimal == 0.2:
        desimal = "1/5"
        return desimal
    elif desimal == 0.166:
        desimal = "1/6"
        return desimal
    elif desimal == 0.142:
        desimal = "1/7"
        return desimal
    elif desimal == 0.125:
        desimal = "1/8"
        return desimal
    elif desimal == 0.111:
        desimal = "1/9"
        return desimal
    elif desimal == 0.1:
        desimal = "1/10"
        return desimal
    elif desimal == 0.666:
        desimal = "2/3"
        return desimal
    elif desimal == 0.4:
        desimal = "2/5"
        return desimal
    elif desimal == 0.285:
        desimal = "2/7"
        return desimal
    elif desimal == 0.222:
        desimal = "2/9"
        return desimal
    elif desimal == 0.75:
        desimal = "3/4"
        return desimal
    elif desimal == 1.333:
        desimal = "4/3"
        return desimal
    else:
        return False




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


def integral(var, i):
    suku = var.split('x')
    if ApakahAdaPangkat(var):
        pangkatGabungan = suku[1].split('^')
        pangkat = int(pangkatGabungan[1].replace("(", "").replace(")", ""))
    else:
        pangkat = 1

    if (suku[0] == ""):
        suku[0] = 1
    elif(suku[0] == "-"):
        suku[0] = -1
    koefisien = int(suku[0])
    koefisienSederhana = koefisien

    # --- di turunkan----------------------------

    pangkat = pangkat + 1
    koefisien = koefisien / pangkat

    #--------------------------------------------

    if isinstance(koefisien, float):
        koefisien = round(koefisien, 3)

    if koefisien == int(koefisien):
        koefisien = int(koefisien)

    # ---- penyusunan -----
    if koefisien > 0 and i != 0:
        tanda = "+"
    else:
        tanda = ""


    # else: -8x^3-x  -8x^3-x^3+7x-2x+7
    #     if koefisien < 0:
    #         tanda = ""
    #         koefisien *= -1

    # print("K : ",koefisien)
    # print(int(koefisienSederhana/pangkat))

    if ApakahPecahanSederhana(koefisien):
        koefisien = ApakahPecahanSederhana(koefisien)
    elif koefisien != int(koefisienSederhana/pangkat):
        print(tanda, koefisienSederhana,"/",pangkat,"x^(", pangkat, ")", end="", sep='')
        return

    #hilangkan 1x
    if koefisien == 1:
        koefisien = ""
        tanda = "+"
    elif koefisien == -1:
        koefisien = ""
        tanda = "-"
    # --------Print-------------
    if pangkat == 1:
        print(tanda, koefisien, "x", end="", sep='')
    elif pangkat != 0:
        print(tanda, koefisien, "x^(", pangkat, ")", end="", sep='')
    else:  # pangkat=0
        print(tanda, koefisien, end="", sep='')


# input
# integral 3x^2
# output : 3 * x ^3

# integral :
# pangkat di tambah 1
# koefisien / pangkat

while True:
    # os.system('cls')
    print("====================================================")
    print(" Masukkan polinomial yang akan di integralkan ")
    print("====================================================")
    polinom = input("f'(x) = ")
    polinom = polinom.replace(" ", "")
    polinom = polinom.replace("-", "#-")

    y = re.split(r'[+#]', polinom)

    panjang = len(y)


    print("Integral :")
    print("f(x)  = ", end="")
    for i in range(panjang):
        if y[i] == '':
            continue
        adaVar = ApakahAdaVar(y[i])
        if adaVar:
            integral(y[i], i)
        else:
            if int(y[i]) >= 0:
                tanda = "+"
            else:
                tanda = ""
            print(tanda, y[i], "x",end="", sep='')
    print("+C", sep='')

    jawaban = None
    while jawaban not in ("y", "n"):
        print("\n")
        print("===================================================")
        print("==== Apakah anda ingin menghitung kembali?(y/n)  ==")
        print("===================================================")
        jawaban = input()
        if jawaban == "y":
            os.system('')
        elif jawaban == "n":
            exit()
        else:
            print("Masukkan 'y' atau 'n' ")

