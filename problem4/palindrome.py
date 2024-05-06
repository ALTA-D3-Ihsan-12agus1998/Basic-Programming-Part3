def cek_palindrome(kata):
    return kata == kata[::-1]

print("\n'Memastikan Kata Palindrome'\n")
input_kata = input("Masukkan kata: ")
if cek_palindrome(input_kata):
    print("True")
else:
    print("False")
