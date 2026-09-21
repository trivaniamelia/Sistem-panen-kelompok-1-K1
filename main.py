from input import input_data_panen
from laporan import cetak_laporan
from diskon import hitung_diskon


def main():
    print("========================================")
    print("   SISTEM PENCATAT HASIL PANEN DIGITAL")
    print("========================================")

    data_panen = input_data_panen()

    if not data_panen:
        print("\nTidak ada data panen yang dimasukkan.")
        return

    total_berat = cetak_laporan(data_panen)

    try:
        harga_per_kg = float(input("\nHarga panen per Kg: "))
        persentase_diskon = float(input("Persentase diskon (%): "))

        if harga_per_kg < 0 or persentase_diskon < 0 or persentase_diskon > 100:
            print("Nilai harga atau diskon tidak valid.")
            return

        total_harga = total_berat * harga_per_kg

        nilai_diskon, total_bayar = hitung_diskon(
            total_harga,
            persentase_diskon
        )

        print("\n========================================")
        print("             STRUK PANEN")
        print("========================================")
        print(f"Total berat      : {total_berat:.2f} Kg")
        print(f"Harga per Kg     : Rp{harga_per_kg:,.2f}")
        print(f"Total harga      : Rp{total_harga:,.2f}")
        print(f"Diskon           : Rp{nilai_diskon:,.2f}")
        print(f"Total bayar      : Rp{total_bayar:,.2f}")
        print("========================================")

    except ValueError:
        print("Input harus berupa angka.")


if __name__ == "__main__":
    main()