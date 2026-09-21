def input_data_panen():
    data_panen = []
    print("=== INPUT DATA HASIL PANEN AGROINDUSTRI ===")

    while True:
        nama_petani = input("Nama Petani/Blok Lahan (atau ketik 'selesai'): ")
        if nama_petani.lower() == 'selesai':
            break

        try:
            berat = float(input(f"Berat panen ({nama_petani}) (Kg): "))
            kadar_air = float(input(f"Kadar air ({nama_petani}) (%): "))

            data_panen.append({
                "petani": nama_petani,
                "berat": berat,
                "kadar_air": kadar_air
            })
            print("Data berhasil disimpan.\n")
        except ValueError:
            print("Input tidak valid! Masukkan angka untuk berat dan kadar air.\n")

    return data_panen


# Kode untuk menjalankan dan menguji fungsi
if __name__ == "__main__":
    hasil_panen = input_data_panen()
    print("\nData panen yang berhasil diinput:")
    print(hasil_panen)
  
