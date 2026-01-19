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
print("Начало лабиринта(x y)", start_x, start_y)


finish_x = 0
finish_y = 0
for i in range(5):
    for j in range(5):
        if labirint_list[i][j] == "ф":
            finish_x = j
            finish_y = i
            break
print("Конец лабиринта(x y)", finish_x, finish_y)


rasstoyanie_ot_n_do_f = abs(finish_x - start_x)+abs(finish_y - start_y)
print("Манхетовское расстояние равно:", rasstoyanie_ot_n_do_f)

count_m = 0
for i in range(5):
    for j in range(5):
        if labirint_list[i][j] == "м":
            count_m += 1
print("🟡" * count_m)
