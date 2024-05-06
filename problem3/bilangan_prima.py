# Memastikan Bilangan Prima Atau Bukan

def bilangan_prima(angka) :
    if angka > 1 :
        for i in range(2, int(angka*0.5) + 1) :
            if angka % i == 0 :
                print("False")
                return
        print("True")
    else:
        print("Bilangan harus lebih besar dari 1")


print("\n'Memastikan Bilangan Prima'\n")
angka = int(input("Masukkan bilangan : "))
bilangan_prima(angka)
