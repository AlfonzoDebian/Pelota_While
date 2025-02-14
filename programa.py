h = int(input("Poner la altura h: "))

s = h / 5
saltos = 0
valor = h

while valor >= s:
    saltos += 1
    valor*=0.9
pass

print(f"Numero de rebotes que no alcanzo la 5* parte: {saltos}")