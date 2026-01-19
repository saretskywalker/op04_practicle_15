#1н0001м0101з1001110л1ф0м1

labirint = input("Введите символьное представление лабиринта: ")
labirint_list = []

for i in range (0, 26, 5):
    print(labirint[i:i+5])
    labirint_list.append(labirint[i:i+5])

start_x = 0
start_y = 0

for i in range(5):
    for j in range(5):
        if labirint_list[i][j] == "н":
            start_x = j
            start_y = i
            break
print("Начало лабиринта", start_x, start_y)
