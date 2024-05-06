# input

# student_score = 80

print("\n'Penilaian'\n")
nama_mahasiswa = input("Masukkan Nama Mahasiswa : ")
input_nilai = input("Masukkan Nilai : ")


# Process: Your Solution Code Here
nilai = int(input_nilai)
grade = ""

if nilai >= 80 :
    grade = "A"
elif nilai >= 65 :
    grade = "B+"
elif nilai >= 50 :
    grade = "B"
elif nilai >= 35 :
    grade = "C"
else:
    grade = "D"


# Output "Nilai A"
print("\nMahasiswa ", nama_mahasiswa)
print("Dengan Nilai ", nilai ," Mendapat Grade ", grade)