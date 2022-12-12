data = ['https://github.com/91v3n/python_dz/tree/main/DZ5', 'https://gb.ru/lessons/284811/homework', 'https://biggeek.ru/cart']
data = [i[8:] for i in data]
cut = lambda x: x.find('/')
data = [i[:cut(i)] for i in data]
print(data)