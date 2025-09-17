#18.
t = int(input("Temperatura: "))
if t > 0 and t < 100:
    print("tecno")
elif t <= 0:
    print("cvrsto")
else:
    print("gasovito")

#23.
import math
x = float(input("Unesi x: "))
y = float(input("Unesi y: "))
r1, r2 = 4, 6 
iznad_prave = x - y - 4 > 0

d = math.sqrt(x**2 + y**2)
unutar_prstena = r1 <= d <= r2

if iznad_prave and unutar_prstena:
    print("Pripada")
else:
    print("Ne pripada")

#39.
broj = input("Unesite broj: ")
n = len(broj)
suma = sum(int(c)**n for c in broj)

print("Da" if suma == int(broj) else "Ne")

#96.
def split_string(string, number):
    result = []
    for i in range(0, len(string), number):
        podstring = string[i:i+number]
        if len(podstring) < number:
            podstring += '*' * (number - len(podstring))
        result.append(podstring)
    return result

string = input("Unesite string: ")
number = int(input("Dužina podstringa: "))
rezultat = split_string(string, number)
print(f"Podstringovi: {rezultat}")