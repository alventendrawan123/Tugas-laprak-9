def cari_min_max():
    angka = []
    while True:
        data = input("Masukkan angkanya (ketik 'done' jika selesai): ")
    
        if data.lower() == 'done':
            break
        
        try:
            nommor = float(data)
            angka.append(nommor)
        except ValueError:
            print("inputan tidak valid")

    if angka:
        print("nilai maksimal:", max(angka))
        print("nilai minimal:", min(angka))

    else:
        print("Harap masukkan angka terlebih dahulu.")

if __name__ == "__main__":
    cari_min_max()