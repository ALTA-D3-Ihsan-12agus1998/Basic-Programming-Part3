# bilangan = int(input())

def faktor_bilangan1(bilangan) :
    print("Hasil faktor dari bilangan", bilangan, "adalah : ")
    for i in range(bilangan, 0, -1) :
        if bilangan % i == 0 :
            print(i)

print("\n'Faktor Bilangan Besar ke Kecil'\n")
bilangan = int(input("Masukkan Angka : "))
faktor_bilangan1(bilangan)