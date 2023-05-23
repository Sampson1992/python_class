# working with tuples

fruits = ('orange', 'mango', 'banana', 'sweet apple', 'kiwi', 'cherry', 'pineaples', 'water mellon')
print(type (fruits))

#accessing your tuple items

fruits = ('orange', 'mango', 'banana', 'sweet apple', 'kiwi', 'cherry', 'pineaples', 'water mellon')

print(fruits[3:5])

#fruits= ('orange', 'mango', 'banana', 'sweet apple', 'kiwi', 'cherry', 'pineaples', 'water mellon')
#fruits.insert(2, 'strayberry')
#print(fruits)

# add to tuples
fruits = ('orange', 'mango', 'banana', 'sweet apple', 'kiwi', 'cherry', 'pineaples', 'water mellon')
y = list(fruits)
y.append('strarwberry')
fruits = tuple(y)
print(fruits)

#Dictionaries

student = {
    'name': 'Rafique',
    'country': 'Ghana',
    'Sex' : 'male',
    'city': 'kumasi'

}
print(student)

#accessing your dictionary

student =  {
    'name': 'Rafique',
    'country': 'Ghana',
    'Sex' : 'male',
    'city': 'kumasi'

}
print(student['country'])

# update dictionaries

student = {
    'name': 'Rafique',
    'country': 'Ghana',
    'Sex' : 'male',
    'city': 'kumasi'

}
student.update({'country': 'Somalia'})
print(student)

#conditional statement
# if statement

a = 33
b = 200
if b > a:
    print('b is greater than a')

    # elif statement
    a = 33
    b = 33
    if b > a:
        print('b is greater than a')
    elif a == b:
        print('a and b are equal')

    # else statement

    a = 200
    b = 33
    if b > a:
        print('b is greater than a')
    elif a == b:
        print('a and b are equal')
    else:
        print('a is greater than b')

        # else with elif statement

        a = 200
        b = 33
        if b > a:
            print('b is greater than a')
        else:
            print('b is not greater than a')
    # And keyword
    a = 200
    b = 33
    c = 500
    if a >b and c >a:
        print('both conditions are true')

        #or stATMENT
        a = 200
        b = 33
        c = 500
        if a >b or a >c: 
         print('at least one of the conditions is true')