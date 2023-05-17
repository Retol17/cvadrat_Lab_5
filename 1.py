import numpy as np

# Задаем значения x и y
x = np.array([-7.0, -5.37, -3.74, -2.11, -0.47, 1.16, 2.79, 4.42, 6.05])
y = np.array([4188.4, -3713.5, -505.8, 19.28, -3.84, -30.22, -244.3, -699.6, -458.1])

# Формируем матрицу X
X = np.zeros((len(x), 6))
for i in range(len(x)):
    X[i] = [1, x[i], x[i]**2, x[i]**3, x[i]**4, x[i]**5]

# Решаем систему уравнений методом Гаусса
A = np.dot(X.T, X)
B = np.dot(X.T, y)
a = np.linalg.solve(A, B)

# Выводим результат в файл
with open('polynomial_equation.txt', 'w') as f:
    f.write('Уравнение многочлена 5-й степени:\n')
    f.write('y = {:.5f} + {:.5f}*x + {:.5f}*x^2 + {:.5f}*x^3 + {:.5f}*x^4 + {:.5f}*x^5\n'.format(a[0], a[1], a[2], a[3], a[4], a[5]))
