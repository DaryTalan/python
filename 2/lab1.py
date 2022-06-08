s = input("Введите число: ")
d = s.split(".")
a = int(d[0])
b = int(d[1]) 
a = abs(a)
sum = 0
while(a != 0):
 sum = sum + (a % 10) 
 a = a//10  
while(b != 0):
 sum = sum + (b % 10) 
 b = b//10  
print(f"Сумма чисел {sum}")