def hitung_ips(jumlah_matkul):
    total_sks = jumlah_matkul * 3
    total_bobot = 0
    for _ in range(jumlah_matkul):
        nilai = input("Masukkan nilai (A, B, C, atau D): ")
        if nilai.upper() == 'A':
            total_bobot += 4 * 3
        elif nilai.upper() == 'B':
            total_bobot += 3 * 3
        elif nilai.upper() == 'C':
            total_bobot += 2 * 3
        elif nilai.upper() == 'D':
            total_bobot += 1 * 3
        else:
            print("Nilai yang dimasukkan tidak valid.")
            return None
    return total_bobot / total_sks

jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))

ips = hitung_ips(jumlah_matkul)
if ips is not None:
    print("Indeks Prestasi Semester (IPS) Anda adalah:", ips)