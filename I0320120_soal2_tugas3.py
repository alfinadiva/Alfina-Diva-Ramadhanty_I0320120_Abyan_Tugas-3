#dictionary
dict = {'Nama' : 'Alfina Diva Ramadhanty',
        'Hobi' : ['Naik Gunung','Travelling'],
        'Sosial Media' : ['Instagram','Line','Twitter','Facebook'],
        'Lagu Kesukaan' : ['To the bone','Way back home','Happier'],
        'Makanan Favorit' : ['Iga Bakar','Seafood','Mie goreng']}

#mengubah hobi dan sosial media
dict['Hobi'][1] = ('Baca Novel')
dict['Sosial Media'][2] = ('Telegram')

#menghapus 2 makanan favorit
del dict['Makanan Favorit'][1:3]

#menambah hobi
dict['Hobi'].append('mendengarkan musik')

print(dict)


