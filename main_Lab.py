
def learning():
    big_data = {}
    with open('1.txt',encoding='utf-8') as file:
        a = [float(i.strip()) for i in file.readlines()]
    c = 1
    for i in range(0, len(a), 19):
        x = []
        y = []
        for j in range(i + 1, i + 10):
            x.append(a[j])
        for h in range(i + 10, i + 19):
            y.append(a[h])

        big_data[c] = {'x': x,
                       'y': y
                       }
        c = c + 1
    file.close()
    return big_data
print('Введите номер номер входных данных(от 1 до 50):')
choice = int(input())
def user_choice(choice):
    big_data = learning()

    if choice < 0 or choice > 50:
        print("Число не входит в промежуток от 0 до 50")
        return 0
    return big_data[choice]

def main():
    slovar = user_choice(choice)
    x = slovar["x"]
    y = slovar["y"]
    print(slovar)
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_10 = sum([xi ** 10 for xi in x])
    sum_x_9 = sum([xi ** 9 for xi in x])
    sum_x_8 = sum([xi ** 8 for xi in x])
    sum_x_7 = sum([xi ** 7 for xi in x])
    sum_x_6 = sum([xi ** 6 for xi in x])
    sum_x_5 = sum([xi ** 5 for xi in x])
    sum_x_4 = sum([xi ** 4 for xi in x])
    sum_x_3 = sum([xi ** 3 for xi in x])
    sum_x_2 = sum([xi ** 2 for xi in x])
    sum_x5_y = sum([x[i] ** 5 * y[i] for i in range(n)])
    sum_x4_y = sum([x[i] ** 4 * y[i] for i in range(n)])
    sum_x3_y = sum([x[i]**3 * y[i] for i in range(n)])
    sum_x2_y = sum([x[i] ** 2 * y[i] for i in range(n)])
    sum_xy = sum([x[i] * y[i] for i in range(n)])

    A = [[sum_x_10, sum_x_9, sum_x_8, sum_x_7, sum_x_6, sum_x_5],
         [sum_x_9, sum_x_8, sum_x_7, sum_x_6, sum_x_5, sum_x_4],
         [sum_x_8, sum_x_7, sum_x_6, sum_x_5,sum_x_4, sum_x_3],
         [sum_x_7, sum_x_6, sum_x_5, sum_x_4, sum_x_3, sum_x_2],
         [sum_x_6, sum_x_5, sum_x_4, sum_x_3, sum_x_2, sum_x],
         [sum_x_5, sum_x_4, sum_x_3, sum_x_2, sum_x, n]]
    B = [sum_x5_y,sum_x4_y,sum_x3_y,sum_x2_y,sum_xy,sum_y]

    # Приведение матрицы коэффициентов к ступенчатому виду
    for i in range(len(A)):
        # Деление первой строки на a11
        div = A[i][i]
        for j in range(len(A[i])):
            A[i][j] /= div
        B[i] /= div

        # Вычитание первой строки, умноженной на aij/a11, из всех последующих строк
        for k in range(i + 1, len(A)):
            mult = A[k][i]
            for j in range(len(A[k])):
                A[k][j] -= mult * A[i][j]
            B[k] -= mult * B[i]

    # Обратный ход метода Гаусса для получения решения системы
    x = [0] * len(A)
    for i in range(len(A) - 1, -1, -1):
        x[i] = B[i]
        for j in range(i + 1, len(A)):
            x[i] -= A[i][j] * x[j]
    print("Решение системы уравнений:")
    for i in range(len(x)):
        print("%d коэф. = %.2f" % (i + 1, x[i]))
    return x

def print_func():
    coeffs = main()
    func = f'Уравнение №{choice}: ({coeffs[0]})x^5 + ({coeffs[1]})x^4 + ({coeffs[2]})x^3 + ({coeffs[3]})x^2 + ({coeffs[4]})x + ({coeffs[5]})'
    with open("2.txt",'a',encoding="utf-8") as file:
        file.write(func)
    print(func)

print_func()
