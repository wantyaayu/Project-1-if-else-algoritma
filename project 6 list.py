nama_mahasiswa = ["Ayu", "Beni", "Ciko", "Dewi", "Esa"]

print('nama_mahasiswa: ')
for nama in nama_mahasiswa:
    print(nama)

# Menambahkan beberapa nama ke dalam list
nama_mahasiswa.extend(["Fira", "joko", "Hani"])
# Menampilkan list setelah penambahan nama nama baru
print("\nIsi list setelah penambahan elemen baru:")
for nama in nama_mahasiswa:
    print(nama)

# Mengurutkan list secara alfabet
nama_mahasiswa.sort()

# Menampilkan list setelah pengurutan
print("\nIsi list setelah diurutkan:")
for nama in nama_mahasiswa:
    print(nama)