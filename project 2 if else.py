kelas= int(input('masukan nilai kelas: '))
nilai_fisika = int(input('masukan nilai fisika: '))

if kelas >= 11 and nilai_fisika >= 8:
    print("bisa mendadaftar olimpiade kimia.")
else:
    print("Anda tidak memenuhi syarat untuk daftar olimpiade kimia.")

if kelas == 10  :
    print("Anda dapat daftar olimpiade lain")
elif 7 <= kelas <= 10:
    print("Anda tidak dapat daftar olimpiade.")
else:
    print("Anda dapat menjadi suporter")