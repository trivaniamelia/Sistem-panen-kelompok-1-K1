def cetak_laporan(data_panen):
    print("\n====================================")
    print("       LAPORAN HASIL PANEN")
    print("====================================")

    if not data_panen:
        print("Belum ada data panen.")
        return 0

    total_berat = 0
    total_kadar_air = 0

    print("No | Petani/Blok       | Berat (Kg) | Kadar Air (%)")
    print("----------------------------------------------------")

    for i, data in enumerate(data_panen, start=1):
        print(
            f"{i:<2} | "
            f"{data['petani']:<17} | "
            f"{data['berat']:<10.2f} | "
            f"{data['kadar_air']:<13.2f}"
        )

        total_berat += data["berat"]
        total_kadar_air += data["kadar_air"]

    rata_rata_kadar_air = total_kadar_air / len(data_panen)

    print("----------------------------------------------------")
    print(f"Total berat panen     : {total_berat:.2f} Kg")
    print(f"Rata-rata kadar air   : {rata_rata_kadar_air:.2f}%")
    print("====================================")

    return total_berat