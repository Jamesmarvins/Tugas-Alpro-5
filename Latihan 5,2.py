def deret_ganjil(bawah, atas):
    if bawah > atas:
        bawah, atas = atas, bawah
    
    if bawah % 2 == 0:
        bawah += 1

    return [bilangan for bilangan in range(bawah, atas + 1, 2)]

batas_bawah = int(input("Masukkan batas bawah: "))
batas_atas = int(input("Masukkan batas atas: "))

print("Deret bilangan ganjil dari", batas_bawah, "sampai", batas_atas, "adalah:")
print(deret_ganjil(batas_bawah, batas_atas))