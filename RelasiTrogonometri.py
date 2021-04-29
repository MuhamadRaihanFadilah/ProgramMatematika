import os
a = 1
Negatif = None
Muter = None
Looping = True
Stop = None
#Fungsi Niali Sudut Istimewa
def NILAIsudut(Tipe,Teta) :
    if Tipe == "sin":
        if Teta == 0:
            Stop = True
            print("=  0")
        elif Teta == 30:
            Stop = True
            print("=  1/2")
        elif Teta == 45:
            Stop = True
            print("=  1/2 * akar 2")
        elif Teta == 60:
            Stop = True
            print("=  1/2 * akar 3")
        elif Teta == 90:
            Stop = True
            print("=  1")
        else:
            Stop = False

    elif Tipe == "cos":
        if Teta == 0:
            Stop = True
            print("=  1")
        elif Teta == 30:
            Stop = True
            print("=  1/2 * akar 3")
        elif Teta == 45:
            Stop = True
            print("=  1/2 * akar 2")
        elif Teta == 60:
            Stop = True
            print("=  1/2")
        elif Teta == 90:
            Stop = True
            print("=  0")
        else:
            Stop = False

    elif Tipe == "tan":
        Stop = True
        if Teta == 0:
            Stop = True
            print("=  0")
        elif Teta == 30:
            Stop = True
            print("=  1/3 * akar 3")
        elif Teta == 45:
            Stop = True
            print("=  1")
        elif Teta == 60:
            Stop = True
            print("=  akar 3")
        elif Teta == 90:
            Stop = True
            print("=  Tak Hingga")
        else:
            Stop = False

    elif Tipe == "cot":
        if Teta == 0:
            Stop = True
            print("=  Tak Hingga")
        elif Teta == 30:
            Stop = True
            print("=  akar 3")
        elif Teta == 45:
            Stop = True
            print("=  1")
        elif Teta == 60:
            Stop = True
            print("=  1/3 * akar 3")
        elif Teta == 90:
            Stop = True
            print(" atau  = 0")
        else:
            Stop = False

    return Stop

#Fungsi Print Jawaban
def Jawaban(Negatif,Tipe,Teta):
    print("+++++++++++++++ Jawaban ++++++++++++++++")
    # Penggabungan
    if (Negatif == True):
        print("  -", Tipe, "(", Teta, ")") #Hitung
    else:
        print("", Tipe, "(", Teta, ")")
    NILAIsudut(Tipe,Teta)
    return 0

#Pemberian Minus
def min(Pilihan,Teta):
    if (Pilihan == "sin"):  # sin # pemberian minus
        if (Teta > 180):
            Negatif = True
        else:
            Negatif = False
    elif (Pilihan == "cos"):  # cos
        if (0 < Teta < 90 or 270 < Teta < 360):
            Negatif = False
        else:
            Negatif = True
    else:  # tan
        if (0 < Teta < 90 or 180 < Teta < 270):
            Negatif = False
        else:
            Negatif = True
    return Negatif

#Untuk Mengulang Program
def Ulang():
    jawaban = None
    while jawaban not in ("iya", "tidak"):
        print("=========================================================")
        print("      Apakah anda ingin menghitung lagi ?  iya / tidak   ")
        print("=========================================================")
        jawaban = input("Masukkan jawaban : ")
        if jawaban == "iya":
            os.system('cls')
            Muter = True
        elif jawaban == "tidak":
            Muter = False
        else:
            print("Masukkan 'iya' atau 'tidak' ")
    return Muter


while(Looping == True):
    print("===================================")
    print("||    Program Perubahan Sudut    ||")
    print("===================================")
    print()
    print("""Masukkan
    - sin
    - cos
    - tan
        """)
    Pilihan = None
    while Pilihan not in ("sin", "cos", "tan"):
        Pilihan = input("Masukkan jawaban : ")  ###
        if Pilihan == "sin":
            Tipe = "sin"
        elif Pilihan == "cos":
            Tipe = "cos"
        elif Pilihan == "tan":
            Tipe = "tan"
        else:
            print("masukkan dengan benar ! (TANPA huruf KAPITAL)")
    print()

    Teta = int(input("Masukkan nilai teta : "))
    Var = None
    if (Teta > 360):
        Dir = int(Teta / 360)
        Var = Teta - 360 * Dir
        print(Tipe, "", Teta, " (derajat) = ", Tipe, " (", Dir, " * 360 + ",Var,") = ", Tipe, "", Var, " (derajat)")
        if (Var <= 90):  # Simple
            Jawaban(Negatif, Tipe, Var)
            Keluar = Ulang()
            if Keluar == False :
                break
            else:
                continue
        else:
            Teta = Var

    Back = NILAIsudut(Tipe,Teta)
    if Back == True:
        Keluar = Ulang()
        if Keluar == False:
            break
        else:
            continue
    else:
        None
    ######################################
    print("""Masukkan
                    1) jika menggunakan 0 & 180 (derajat)
                    2) jika mengunakan 90 & 270 (derajat)
            """)
    Conversi = None
    while Conversi not in (1, 2):  # Perubahan Tipe
        Conversi = int(input("Masukkan jawaban : "))  ###
        if Conversi == 1:
            None
        elif (Conversi == 2):
            if (Pilihan == "sin"):
                Tipe = "cos"
            elif (Pilihan == "cos"):
                Tipe = "sin"
            else:#tan
                Tipe = "cot"
        else:
            print("masukkan dengan angka yg tersedia di atas !")

    if (Conversi == 2):  # Penghitungan Teta
        if (0 < Teta < 180):  # batas batas
            if (Teta < 90):
                Hitung = 90 - Teta
            else:
                Hitung = Teta - 90
        else:
            if (Teta < 270):
                Hitung = 270 - Teta
            else:
                Hitung = Teta - 270
    else:
        if (90 < Teta < 270):
            if (Teta < 180):
                Hitung = 180 - Teta
            else:
                Hitung = Teta - 180
        else:
            if (Teta < 360):
                Hitung = 360 - Teta
            else:
                Hitung = Teta - 360


    Jawaban(min(Pilihan, Teta), Tipe, Hitung)
    Keluar = Ulang()
    if Keluar == False:
        break
    else:
        continue

print("-------------    Program Selesai    ----------------")