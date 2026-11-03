import time

global step
step = 0

list_angka = [93,62,17,10,29,82,61]

print('List awal',list_angka)
time.sleep(1)
print('Memulai proses pengurutan ...')
time.sleep(1)
print('___________________________________________')

for iterasi in range(len(list_angka)-1,0,-1):
    for i in range(iterasi):
        if list_angka[i]>list_angka[i+1]:
            step = step + 1
            print('Langkah ke:', step)
            time.sleep(1)
            print('Urutannya:',list_angka)
            time.sleep(1)
            print('Perbandingan dimulai dari:',list_angka[i],'dan',list_angka[i+1])
            time.sleep(1)
            print('Karena angka', list_angka[i],'lebih besar dari', list_angka[i+1],'maka perlu di-SWAP.')
            print('Yaitu dari ',list_angka[i],'<-->',list_angka[i+1],'menjadi',list_angka[i+1],'<-->',list_angka[i],'.')
            list_angka[i],list_angka[i+1] = list_angka[i+1], list_angka[i] #proses swap variablenya disini
            print('List sementara:', list_angka)
            print('___________________________________________')
            time.sleep(5)
        else:
            step = step + 1
            print('Langkah ke:', step)
            time.sleep(1)
            print('Urutannya:',list_angka)
            time.sleep(1)
            print('Perbandingan dimulai dari:',list_angka[i],'dan',list_angka[i+1])
            time.sleep(1)
            print('Karena angka', list_angka[i],'lebih kecil dari', list_angka[i+1],'maka TIDAK perlu di-SWAP.')
            print('List sementara:', list_angka)
            print('___________________________________________')
            time.sleep(5)
        
    print('__________[KEMBALI KE AWAL]________________')

print('Data sudah ter-urutkan ...')
print('List akhir',list_angka)