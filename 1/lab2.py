x = int(input("Введите число x: "))
y = int(input("Введите число y: "))
if x > 0 and y > 0 :
 b = '1 четверть'
if x < 0 and y > 0 :
 b = '2 четверть'
if x < 0 and y < 0 :
 b = '3 четверть'
if x > 0 and y < 0 :
 b = '4 четверть'
print(f"Находится в {b}")
