x = input("Lingua Ignota")
if type(x) == type("mj"):
    print("Sinner Get Ready")
else:
    print("Caligula")

bool(-17)
bool("Lingua Ignota")
bool(True)
bool(0)

#Boolean operators

x = 5 
y = 10
print(x == 7)
print(x = 7)
print(x != y)
print(x > y)
print(x < y)
print(x >= (y - 3))

#Logical operators

mj1 = "All Bitches Die"
mj2 = "Let The Evil of His Own Lips Cover Him"
print(mj1 == mj2) or mj1 == "All Bitches Die"
print(mj1 <= mj2)
print(mj2 <= mj1)
print("THE SOLITARY BRETHREN OF EPHRATA" < "PENNSYLVANIA FURNACE")
print(not(True))

#Identity operators

    #Tommia ei kiinnostanut

#Membership operators

mj = "THE ORDER OF SPIRITUAL VIRGINS"
print("I" in mj)
print("SPIRITUAL" in mj)
print("T" not in mj)
print(not("T" in mj))

#Boolean returning methods for strings

    #"Ei käydä näitä sen kummemmin läpi"
    #"Mahdollisesti tarvitsette harkkatehtävissä"

#Shortened versions of normal assignment operators

    #Katso kurssimateriaalista luento 5:n kohdalta, vaikuttaa järkevältä opetella

#If-statement

x = 5
if x > 3:
    print(x)
    x = 6
print("This is outside the if-block")

x = 5
print("x:n arvo alussa:", x)
if x > 3:
    print("Nyt ollaan if-lauseen sisällä")
    x = 15
print("x:n arvo lopussa:", x)

x = 2
print("x:n arvo alussa:", x)
if x > 3:
    print("Nyt ollaan if-lauseen sisällä")
    x = 15
print("x:n arvo lopussa:", x)

x = 2
print("x:n arvo alussa:", x)
if x + 1 > 3:
    print("Nyt ollaan if-lauseen sisällä")
    x = 15
print("x:n arvo lopussa:", x)
#Ei mennä if-lauseen sisälle, koska x + 1 = 3, ei > 3

x = 2
print("x:n arvo alussa:", x)
if x + 10 > 3:
    print("Nyt ollaan if-lauseen sisällä")
    x = 15
print("x:n arvo lopussa:", x)
#Mennän ehtolauseen sisälle, koska x + 10 > 3

x = 2
print("x:n arvo alussa:", x)
if x + 10 > 3:
    print("Nyt ollaan if-lauseen sisällä")
    x = 15
elif: x >= 2
    print("Ollaan ensimmäisessä elif-haarassa")
    x = 1
elif x == 2:
    print("Ollaan toisessa elif-haarassa")
    x = 333
else:
    print("Ollaan else-haarassa, eli if-ehto ei toteutunut")
    x = 55
print("x:n arvo lopussa:", x)
#Else-haaraan mennään aina, jos if-lauseen ehto ei toteudu
#Elif-haaroista koodi voi kulkea vain max. yhteen
#Elif-haara = "else-if -haara"




