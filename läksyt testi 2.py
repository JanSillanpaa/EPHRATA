
#c)
y = 1.1
y = float(y)
y = int(y)
y = float(y)
print(y)
# Kun y muutetaan floatiksi, kokonaisarvo 1.1 säilytetään kokonaisuudessaan, 
# mutta muutettaessa int-funktioon, desimaali ".1" häviää. 
# Täten muutettaessa takaisin flow-funktioksi, desimaaliarvo on nolla, sillä int-funktio luo aina tasaluvun. 