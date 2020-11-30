
class pajakKendaraan :
    j_kendaraan = 0
    def __init__(self, merek, cc, plat, kadaluarsa):
        self.merek = merek
        self.cc = cc
        self.plat = plat
        self.kadaluarsa = kadaluarsa
        pajakKendaraan.j_kendaraan += 1 
    def tampil_jumlah(self):
        print("jumlah kendaraan yang telah terdaftar dalam pajak",  pajakKendaraan.j_kendaraan)
    def tampil_atribut(self):
        print("merek :", self.merek, "\ncc / kecepatan motor :", self.cc, "\nplat :", self.plat, "\nkadaluarsa :", self.kadaluarsa)

Motor_1 = pajakKendaraan("Honda New CBR", "150", "AB 1231 Q", "bulan 12, tahun 21")
Motor_2 = pajakKendaraan("Yamaha Mt 25", "250", "AB 9732 J", "bulan 7, tahun 22")
Motor_3 = pajakKendaraan("Yamaha Jupiter MX", "125", "B 234 WX", "bulan 12, tahun 20")
Motor_4 = pajakKendaraan("Honda New Vario", "80", "AB 9720 RT", "bulan 1, tahun 24")

Motor_1.tampil_atribut()
print(pajakKendaraan.j_kendaraan) #menggunakan variable global
print(Motor_4.tampil_jumlah()) #menggunakan object