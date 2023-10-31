volume = 1.44
pages = 100
lines = 50
symbols = 25
onesymbol = 4
size = volume*1024*1024
books = size // (pages*lines*symbols*onesymbol)
print("Количество книг, помещающихся на дискету:", int(books))

