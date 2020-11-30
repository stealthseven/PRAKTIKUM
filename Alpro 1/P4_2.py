def selection_sort(list):
    print("list awal :", list)

    for i in range (len(list)-1):
        index_min = i 
        for j in range(i+1, len(list)):
            if list[index_min] < list[j]:
                index_min = j
            #penukaran
            tempat = list[i]
            list[i] = list[index_min]
            list[index_min] = tempat

            print("inkes yang ditukarkan", index_min, "dengan indeks ke", i)
            print('iterasi ke :', i, 'menukar angka :', tempat,"|", list)

    

selection_sort([4,3,5,6,2,78,98])
