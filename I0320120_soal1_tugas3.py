#nama teman angkatan
list = ['Tsania', 'Zafira', 'Aji', 'Alvin', 'Maurich', 'Ano', 'Sasa', 'Willy', 'Sekar', 'Alya']
print(list)

#nama pada isi list indeks 4, 6, 7
print(list[4])
print(list[6])
print(list[7])

#mengganti nama pada list indeks 3,5,9
list[3] = 'Zanet'
list[5] = 'Sony'
list[9] = 'Dani'
print(list)

#menambah nama teman
list.append('Candrika')
list.append('Issacian')

#perulangan nama
for x in list:
    print(x)

#panjang list
print(len(list))


