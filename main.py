# Задание 1

print('Задание 1')

x = int(input("Введите икс: "))
y = int(input("Введите игрик: "))

if x == y:
    print("X равен Y")
elif x > y:
    print("X больше Y")
elif x < y:
    print("X меньше Y")


# Задание 2

print('Задание 2')

profit = int(input('Введите прибыль:'))

if profit < 0:
  print('Ошибка: доход не может быть отрицательным')

elif profit < 10000:
  tax = profit * 13 / 100
  print(f'Ваш налог — 13%. Сумма налога — {tax}')

elif profit < 50000:
  tax = profit * 20 / 100
  print(f'Ваш налог — 20%. Сумма налога — {tax}')

else:
  tax = profit * 30 / 100
  print(f'Ваш налог — 30%. Сумма налога — {tax}')


# Задание 3

print('Задание 3')

first = int(input("Введите вес 1 монетки: "))
second = int(input("Введите вес 2 монетки: "))
third = int(input("Введите вес 3 монетки: "))

if first == second:
    print("Третья легче")
elif first < second:
    print("Первая легче")
else:
    print("Вторая легче")