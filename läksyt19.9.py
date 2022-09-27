word = input('Give a string to be encrypted')

def encrypt_it(word):
    alph = "abcdefghijklmnopqrstyzäåö"
    keyw = "uvxyzåäöabcdefghijklmnopqrst"
    result = " "

    for i in word:
        place_in_key = alph.find(i)
        result = result + keyw [place_in_key]
    
    return result

print(encrypt_it(word))




def decrypt_it(word):
    alph = "uvxyzåäöabcdefghijklmnopqrst"
    keyw = "abcdefghijklmnopqrstuvxyzåäö"
    result = ""

    for i in word:
        place_in_key = alph.find(i)
        result = result + keyw[place_in_key]

    return result
    

print(decrypt_it(input("Give a string to be encrypted: ")))







