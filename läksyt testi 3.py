#1

#a)

y = '15.5'
y = float(y)
y = int(y)
print(y)
# Merkkijono y on ensin muutettava flow-jonoksi, 
# sillä vain flow-jono lukee lukujonon desimaalit. 
# Tämän jälkeen int-funktiolla saadaan alas päin pyöristetty merkkijono.

#b)


#c)
y = 1.1
y = float(y)
y = int(y)
y = float(y)
print(y)

#e
# Kun y muutetaan floatiksi, kokonaisarvo 1.1 säilytetään kokonaisuudessaan, 
# mutta muutettaessa int-funktioon, desimaali ".1" häviää. 
# Täten muutettaessa takaisin flow-funktioksi, desimaaliarvo on nolla, sillä int-funktio luo aina tasaluvun. 