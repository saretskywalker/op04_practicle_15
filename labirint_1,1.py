

labirint = input("Введите символьное представление лабиринта: ")
labirint_list = []

for i in range (0, 26, 5):
    print(labirint[i:i+5])
    labirint_list.append(labirint[i:i+5])
