def Binsearch(data, key):
    awal = 1
    akhir = len(data) + 1
    ketemu = False
    while (awal <= akhir) and not ketemu:
        tengah = int((awal + akhir)/2)
        if key == data[tengah]:
            ketemu = True
            print('data', key, 'ditemukan di posisi', tengah,'dari data setelah di urutkan')
        elif (key < data[tengah]):
            akhir = tengah - 1
        else:
            awal = tengah + 1
    if ketemu == False:
        print('data tidak ditemukan')

a = 'rafsanjani rahadi'
b = 'a'
Binsearch(a,b)

