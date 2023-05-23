#tuple allow duplicate

#thistuple = ("apple", "banana", "cherry", "apple", "cherry")
#print(thistuple)

#thistuple = ("apple",)
#print(type(thistuple))

#Accessing tuple items

#thistuple = ("apple", "banana", "cherry")
#print(thistuple[1])

#range of indexes

#thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
#print(thistuple[2:5])


#Change tuple values

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# adding items to tuple

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)

#DICTIONARIES

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


# change dictionary items

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018

print(thisdict)

#adding to items to dictionary

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


# conditional statement
# IF STATEMENT

a = 33
b = 200
if b > a:
  print("b is greater than a")

  # Elif statement

  a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


# Else statement

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

  # AND keyword

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


