def Sqesearch(data,key):
    pos = []
    for i in range(len(data)):
        if data[i] == key :
            pos.append(i+1)
            print("Ditemukan", key, "pada iterasi ke",i+1)
    if len(pos)>0:
        print("data", key, "sebanyak", len(pos), "ditemukan di posisi", pos)
    else :
        print("Data tidak ditemukan")
    return pos

a = 'rafsanjani rahadi'
Sqesearch(a, 'r')