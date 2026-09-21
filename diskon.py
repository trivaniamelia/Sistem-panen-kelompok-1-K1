def hitung_diskon(total_harga, persentase_diskon):
    nilai_diskon = total_harga * persentase_diskon / 100
    total_bayar = total_harga - nilai_diskon

    return nilai_diskon, total_bayar