def insertion_sort(sort_list):
    for i in range(1, len(sort_list)):
        key = sort_list[i]
        j = i - 1
        while j >= 0 and key < sort_list[j]:
            sort_list[j + 1] = sort_list[j]
            j -= 1
            sort_list[j + 1] = key
            print('iterasi', i-1 ,sort_list)

A=[4,3,5,6,2,78,98]
insertion_sort(A)

print("="*50)

def pengurutanDariterbesar(mixList):
    for indeks in range(1, len(mixList)):
        key = mixList[indeks]
        Terurut = indeks - 1 
        while Terurut >= 0 and key > mixList[Terurut]:
            mixList[Terurut + 1] = mixList[Terurut]
            Terurut -= 1 
            mixList[Terurut + 1] = key
            print('iterasi', indeks - 1, mixList)
            print("pergeseran iterasi ke-", indeks - 1,"yangb ergeser adalah", key)

data = [1,2,5,4,8,12,5,4,63,7]
pengurutanDariterbesar(data)

print("="*50)

