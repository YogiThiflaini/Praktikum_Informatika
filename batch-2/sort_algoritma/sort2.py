import time

global step
step = 0

list_angka = [93,62,17,10,29,82,61]

print('List awal',list_angka)
time.sleep(1)
print('Memulai proses pengurutan ...')
time.sleep(1)
print('___________________________________________')

for i in range(len(list_angka)):
    min_index = i
    
    for j in range(i+1, len(list_angka)):
        if list_angka[j] < list_angka[min_index]:
        
            step = step + 1
            print('Langkah ke:', step)
            time.sleep(1)
            print('Urutannya:',list_angka)
            time.sleep(1)
            print('Perbandingan dimulai dari:',list_angka[min_index],'dan',list_angka[j])
            time.sleep(1)

            print('Karena angka', list_angka[j],'lebih kecil dari', list_angka[min_index],'maka angka', list_angka[j],'dianggap paling kecil.')
            min_index = j #proses swap index variable terkecilnya disini
            
            print('List sementara:', list_angka)
            print('___________________________________________')
            time.sleep(5)

        else:
            step = step + 1
            print('Langkah ke:', step)
            time.sleep(1)
            print('Urutannya:',list_angka)
            time.sleep(1)
            print('Perbandingan dimulai dari:',list_angka[min_index],'dan',list_angka[j])
            time.sleep(1)
            print('Karena angka', list_angka[min_index],'lebih kecil dari', list_angka[j],'maka lanjut ke langkah berikutnya.')
            
            print('List sementara:', list_angka)
            print('___________________________________________')
            time.sleep(5)

    if list_angka[min_index] == list_angka[i]:
        step = step + 1
        print('Langkah ke:', step)
        print('Karena angka', list_angka[min_index],'paling kecil dan posisi awal sama, maka lanjut ke langkah berikutnya.')
        list_angka[i], list_angka[min_index] = list_angka[min_index], list_angka[i]
    
        print('List sementara:', list_angka)
        print('___________________________________________')
        time.sleep(5)
    
    else:
        step = step + 1
        print('Langkah ke:', step)
        print('Karena angka', list_angka[min_index],'paling kecil. Maka perlu SWAP dengan', list_angka[i],'.')
        list_angka[i], list_angka[min_index] = list_angka[min_index], list_angka[i]
    
        print('List sementara:', list_angka)
        print('___________________________________________')
        time.sleep(5)
        

print('Data sudah ter-urutkan ...')
print('List akhir',list_angka)