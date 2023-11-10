buah = ['apel', 'pisang', 'jeruk', 'nanas', 'anggur']
 
# isi list buah
print("Isi list buah:")
for b in buah:
    print(b)
 
# Menambahkan buah baru ke dalam list
buah.append('mangga')
print("\nSetelah menambahkan mangga, isi list buah menjadi:")
for b in buah:
    print(b)
 
# Menghapus buah pisang dari list
buah.remove('pisang')
print("\nSetelah menghapus pisang, isi list buah menjadi:")
for b in buah:
    print(b)

