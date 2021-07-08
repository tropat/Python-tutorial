#!/usr/bin/python3
zmienna1 = "kot"
zmienna2 = "Pati"
tekst = zmienna2 + " i " + zmienna1
print(tekst)
print(tekst.lower())
print(tekst.upper())
print(tekst.upper().isupper())
print(len(tekst))
print(tekst[0])
print(tekst.index("kot")) #zwraca numer indeksu, gdzie zaczyna sie dana fraza
print(tekst.replace("kot","pies"))
#-----------------------------------------------
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)
#-----------------------------------------------
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)