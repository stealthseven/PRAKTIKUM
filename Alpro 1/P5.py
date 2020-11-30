#tugas 1 
#descending
def bubleSort(A):
    tukar = True 
    while tukar :
        tukar = False
        for j in range (len(A)-1):
            if A[j] > A[j+1] :
                A[j], A[j+1] = A[j+1], A[j]
                tukar = True
    return A
A = [3,1,8,4,2]
bubleSort(A)
print("hasil akhir ascending :",A)

print("="*50)

#tugas 1 
#descending
def bubleSort(A):
    tukar = True 
    while tukar :
        tukar = False
        for j in range (len(A)-1):
            if A[j] < A[j+1] :
                A[j], A[j+1] = A[j+1], A[j]
                tukar = True
    return A
A = [3,1,8,4,2]
bubleSort(A)
print("hasil akhir descending :",A)

print("="*50)

#tugas 2
#langkah langkah
def bubleSort(A):
    tukar = True 
    while tukar :
        tukar = False
        for j in range (len(A)-1):
            if A[j] < A[j+1] :
                A[j], A[j+1] = A[j+1], A[j]
                tukar = True
                print("tukar", A[j], "dengan", A[j+1],"hasilnya : ", A)
    return A
A = [3,1,8,4,2]
bubleSort(A)

