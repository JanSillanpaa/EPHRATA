#a)
y = '15.5'
y = float(y)
y = int(y)
print(y)
# Merkkijono y on ensin muutettava flow-jonoksi, 
# sillä vain flow-jono lukee lukujonon desimaalit. 
# Tämän jälkeen int-funktiolla saadaan alas päin pyöristetty merkkijono.

#b)
x = (10 > 9)
print(x)
x = str(x)
print(x)
x = (10 > 9)
x = int(x)
print(x)



#c)
y = 1.1
y = float(y)
y = int(y)
y = float(y)
print(y)
# Kun y muutetaan floatiksi, kokonaisarvo 1.1 säilytetään kokonaisuudessaan, 
# mutta muutettaessa int-funktioon, desimaali ".1" häviää. 
# Täten muutettaessa takaisin flow-funktioksi, desimaaliarvo on nolla, sillä int-funktio luo aina tasaluvun. 



#d)

x = "Esteri"
x = list(x)
print(x)

x = ''.join(x)
x = str(x)
print(x)
print(x[0])

# Ekaksi muutin merkkijonon "Ester" listaksi, 
# ja sitten printtasin merkkijonon ensimmäisen merkin.

#e) Tyyppikonversioita tehdessä täytyy muistaa,
# että kaikki konversiot eivät ole yhteensopivia keskenään. 
# Koodaajan täytyy löytää oikea polku konversiosta toiseen.

#2
x1 = int(input("Give value for x1"))
x2 = int(input("Give value for x2"))
x3 = int(input("Give value for x3"))
average = (x1 + x2 + x3) / 3
print(average)
print(abs(average))

#3
import random
num_a = round(random.uniform(0, 99.99), 2)

print(num_a)
num_a = str(num_a)

print(num_a[0:3])
num_b = num_a[3:5]
num_b = num_b + num_a[2]
num_b = num_b + num_a[0:2]
num_b = float(num_b)
print(num_b)

#4

x1 = int(input("How many students have enrolled on the course?"))
x2 = int(input("What's the maximum number of students per lab group?"))

group_size  = (x1 + x2 -1) / x2
print(int(group_size))
