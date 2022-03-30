#podstawowa składnia funkcji anonimowej
#lambda arg1, arg2: arg1 ** arg2

pitagoras = lambda a, b: ((a*a) + (b*b)) ** 0.5
print(pitagoras(3,4))

#funkcje konwencjonalne vs. lambda

def c_sum(x,y):
    return x + y

l_sum = lambda x,y: x +y

print(c_sum(3,4))
print(l_sum(3,4))

#filter(funkcja, iterator): zwraca tylko te wartości ze zbioru
#danych, dla których funkcja zwróciła True
#map(funkcja, iterator): aplikuje funkcję dla każdej wartości
#reduce(funkcja, iterator): służy do zredukowania całego zbioru danych
#do jednej wartości

temperatury = [
    37.6, 35.8, 37.6, 33.4, 34.1, 37.1, 35.9, 34.1, 37.1, 40.5, 38.5, 37.6,
    35.8, 34.5, 36.4, 38.3, 37.5, 37.7, 34.0, 35.3, 35.7, 38.9, 34.8, 34.1,
    39.6, 35.4, 34.7, 37.6, 38.4, 36.4, 39.8, 39.1, 37.1, 35.6, 36.8, 37.6,
    36.7, 40.0, 38.0, 34.1, 35.5, 38.5, 36.1, 32.6, 32.9, 34.5, 41.0, 38.3,
    33.7, 38.7, 36.9, 36.2, 33.7, 38.3, 35.3, 38.3, 40.1, 39.3, 38.2, 37.6,
    39.1, 37.1, 34.4, 38.7, 35.8, 38.2, 38.2, 33.1, 37.8, 36.5, 37.6, 37.4,
    34.3, 37.7, 36.0, 37.5, 37.6, 36.5, 31.3, 37.7, 40.3, 39.5, 35.7, 38.1,
    34.7, 36.5, 34.3, 38.0, 37.0, 38.5, 39.4, 37.6, 41.7, 40.0, 38.4, 38.9,
    34.2, 40.2, 34.3, 35.3
]

wynik = list(filter(lambda x: x >= 40.0, temperatury))
print(wynik)
wynik_sort = sorted(wynik)
print(wynik_sort)

print(temperatury)
from statistics import mean
sr_temp = mean(temperatury)
print(sr_temp)

odch = list(map(lambda x: round(x - sr_temp, 1), temperatury))
print(odch)

from functools import reduce
nums = [1, 2, 3, 4, 5]
print(reduce(lambda a, b: a + b, nums))

#lambda a,b: a if len(a) > len(b) else b

#obliczanie iloczynu
print(reduce(lambda a,b: a*b, [1,2,3,4]))

#tworzenie zbiorów danych w locie (list comprehension)

szesciany = []
for x in range(10):
    szesciany.append(x**3)

print(szesciany)

szesciany = [x**3 for x in range(10)]
print(szesciany)

# szesciany = [x**3 for x in (1,2,3)]  krotka
# szesciany = [x**3 for x in [1,2,3]]  lista

potega_6 = [x**3 for x in [x**3 for x in range(10)]]
print(potega_6)

#nowa_lista = [funkcja(el) for el in lista if warunek(el)]

kwadraty = [el**2 for el in range(1, 102) if el % 2 != 0]
print(kwadraty)

#tworzenie zbiorów

zbior = {znak for znak in "abracadabra" if znak not in "abc"}
print(zbior)

#tworzenie słowników

tekst = "abracadabra"
wystapienia = {znak: tekst.count(znak) for znak in tekst}
print(wystapienia)

c = {x: x**2 for x in (2,4,6)}
print(c)

#wyrażenia generatorowe (generator expressions)
list_comp = [x ** 0.5 for x in range(1, 11)]
#lista powstaje w momencie wywołania wyrażenia
gene_expr = (x ** 0.5 for x in range(1, 11))
#tworzenie reguły pozwalającej na stworzenie listy ad hoc

for x in list_comp:
    print(x)

for x in gene_expr:
    print(x)

list_comp = [x ** 0.5 for x in range(1, 50000001)]

sum = 0
for x in list_comp:
    sum += x
print(sum)

gene_expr = (x ** 0.5 for x in range(1, 50000001))
# gene_expr nie obliczyło jeszcze tych milionów pierwiastków

sum = 0
for x in gene_expr:
    sum += x
print(sum)

# Ćwiczenie na rozgrzewkę
# Utwórz funkcję lambda, która przyjmuje jeden parametr (a) i zwraca go

cw_1 = lambda a: a
print(cw_1(4))

cw_2 = lambda a: a + 15
print(cw_2(10))

cw_3 = lambda x,y: x*y
print(cw_3(10,4))


subject_marks = [('Język angielski', 88),
                 ('Nauka',           90),
                 ('Matematyka',      97),
                 ('Nauki społeczne', 82)]
cw_4 = sorted(subject_marks, key = lambda x: x[1])
print(cw_4)

