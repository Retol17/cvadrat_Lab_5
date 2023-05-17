# Входные данные (пример)
x = [1, 2, 3, 4, 5]
y = [3, 7, 12, 18, 25]

# Функция для нахождения коэффициентов многочлена 5й степени методом наименьших квадратов
def polynomial_least_squares(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_x_squared = sum([xi**2 for xi in x])
    sum_x_cubed = sum([xi**3 for xi in x])
    sum_x_fourth_power = sum([xi**4 for xi in x])
    sum_x_fifth_power = sum([xi**5 for xi in x])
    sum_y = sum(y)
    sum_xy = sum([x[i]*y[i] for i in range(n)])
    sum_x_squared_y = sum([x[i]**2*y[i] for i in range(n)])
    sum_x_cubed_y = sum([x[i]**3*y[i] for i in range(n)])
    sum_x_fourth_power_y = sum([x[i]**4*y[i] for i in range(n)])
    sum_x_fifth_power_y = sum([x[i]**5*y[i] for i in range(n)])

    A = [[n, sum_x, sum_x_squared, sum_x_cubed, sum_x_fourth_power, sum_x_fifth_power],
         [sum_x, sum_x_squared, sum_x_cubed, sum_x_fourth_power, sum_x_fifth_power, sum_x**6],
         [sum_x_squared, sum_x_cubed, sum_x_fourth_power, sum_x_fifth_power, sum_x**6, sum_x**7],
         [sum_x_cubed, sum_x_fourth_power, sum_x_fifth_power, sum_x**6, sum_x**7, sum_x**8],
         [sum_x_fourth_power, sum_x_fifth_power, sum_x**6, sum_x**7, sum_x**8, sum_x**9],
         [sum_x_fifth_power, sum_x**6, sum_x**7, sum_x**8, sum_x**9, sum_x**10]]

    b = [sum_y, sum_xy, sum_x_squared_y, sum_x_cubed_y, sum_x_fourth_power_y, sum_x_fifth_power_y]

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
    for i in range(n-1, -1, -