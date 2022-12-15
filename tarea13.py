from functools import reduce

lista = list(range(5))

res1 = list(filter(lambda x: x % 2, lista)) 
res2= reduce((lambda x,y: x + y), res1)

print(res1)
print("El resultado de la suma es:",res2)
