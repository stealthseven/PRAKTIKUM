# TUGAS !!!
from IPython.display import clear_output 
#variable Global untuk menyimpan data buku
buku = []
kl = 1 

#fungsi untuk menampilkan semua data
def show_data():
    if len(buku) <= 0 :
        print("belum ada data")
    else:
        #for indeks in range(len(buku))
        for indeks in buku :
            print(indeks) #% (indeks, buku)
            
show_data()

#fungsi Untuk menambah data
def insert_data():
    buku_baru = input("judul buku :")
    buku.append(buku_baru)


#fungsi untuk edit data
def edit_data():
    show_data()
    indeks = int(input("input ID buku:"))
    if(indeks > len(buku)):
        print("ID salah")
    else:
        judul_baru = input("judul baru:")
        buku[indeks] = judul_baru


#fungsi untuk menghapus data 
def delete_data():
    show_data()
    indeks = int(input("Inputkan ID buku :"))
    if(indeks > len(buku)):
        print("ID Salah")
    else:
        buku.remove(buku[indeks])
        
#fungsi menampilkan menu
def show_menu():
    Tr = 1 
    print("\n")
    print("--------------------MENU-------------------")
    print("[1] show data")
    print("[2] insert data")
    print("[3] edit data")
    print("[4] delete data")
    print("[5] exit")
    
    menu = int(input("PILIH MENU > "))
    print("\n")
    clear_output(wait=True)
    if (menu == 1):
        show_data()
    elif(menu == 2):
        insert_data()
    elif(menu == 3):
        edit_data()
    elif(menu == 4):
        delete_data
    elif(menu == 5):
        Tr = 0 
    else:
        print("salah pilih")
    return Tr


if __name__ == "__main__":
    Tr=1
    while(Tr==1):
        Tr=show_menu()
        clear_output(wait=True)

