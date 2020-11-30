class mahasiswa:
    jumlah=0
    def __init__(mhs,nama,prodi,NIM):
        mhs.prodi=prodi
        mhs.nama=nama
        mhs.nim=NIM
        mahasiswa.jumlah +=1
    def tampil_jumlah(mhs):
        print("jumlah mahasiswa %d : ", mahasiswa.jumlah)
    def tampil_mahasiswa(mhs):
        print("nama : ", mhs.nama, ",NIM : ", mhs.nim, "prodi : ", mhs.prodi)
#- Menambah instance
# membuat objek pertama pada kelas mahasiswa
mhs1=mahasiswa("iwan","SI",150016001)
# membuat objek kedua pada kelas mahasiswa
mhs2=mahasiswa("riyadi","math",160016002)
# membuat objek ketiga pada kelas mahasiswa
mhs3=mahasiswa("yanto","fisika",140016003)
# membuat objek keempat pada kelas mahasiswa
mhs4=mahasiswa("tri","biologi",130016004)
#- Mengakses attribute
mhs1.tampil_mahasiswa()
mhs2.tampil_mahasiswa()
mhs3.tampil_mahasiswa()
mhs4.tampil_mahasiswa()
#- Menampilan jumlah instance
mahasiswa.jumlah
