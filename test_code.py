x = [1, 2, 3, 4, 5]
y = [3, 7, 12, 18, 25]

# Функция для нахождения коэффициентов квадратичной функции методом наименьших квадратов
def quadratic_least_squares(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_x_squared = sum([xi**2 for xi in x])
    sum_x_cubed = sum([xi**3 for xi in x])
    sum_x_fourth_power = sum([xi**4 for xi in x])
    sum_y = sum(y)
    sum_xy = sum([x[i]*y[i] for i in range(n)])
    sum_x_squared_y = sum([x[i]**2*y[i] for i in range(n)])

    A = [[n, sum_x, sum_x_squared],
         [sum_x, sum_x_squared, sum_x_cubed],
         [sum_x_squared, sum_x_cubed, sum_x_fourth_power]]

    b = [sum_y, sum_xy, sum_x_squared_y]

    # Решение системы уравнений методом Гаусса
    for i in range(n-1):
        if A[i][i] == 0:
            for j in range(i+1, n):
                if A[j][i] != 0:
                    A[i], A[j] = A[j], A[i]
                    b[i], b[j] = b[j], b[i]
                    break
        for j in range(i+1, n):
            ratio = A[j][i]/A[i][i]
            for k in range(i, n):
                A[j][k] = A[j][k] - ratio*A[i][k]
            b[j] = b[j] - ratio*b[i]

    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = b[i]/A[i][i]
        for j in range(i):
            b[j] -= A[j][i]*x[i]

    return x[0], x[1], x[2]

# Находим коэффициенты квадратичной функции
a, b, c = quadratic_least_squares(x, y)

# Печатаем уравнение квадратичной функции
print(f"Уравнение квадратичной функции: y = {a:.2f} + {b:.2f}x + {c:.2f}x^2")

# for i in range(n-1):
#         if A[i][i] == 0:
#             for j in range(i+1, n):
#                 if A[j][i] != 0:
#                     A[i], A[j] = A[j], A[i]
#                     b[i], b[j] = b[j], b[i]
#                     break
#         for j in range(i+1, n):
#             ratio = A[j][i]/A[i][i]
#             for k in range(i, n):
#                 A[j][k] = A[j][k] - ratio*A[i][k]
#             b[j] = b[j] - ratio*b[i]
#
#     x = [0 for i in range(n)]
#     for i in range(n-1,