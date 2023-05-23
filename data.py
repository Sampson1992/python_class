#Python data types
#determing your data type

c = False
print(type(c))

#working with strings
print('my name is Cesar')
#adding variables
law = ('happy birthday to my love')
print(len(law))

#checking string
law = ('happy birthday to my love')
print('sad day' in law)

#upper and lower cases
law = ('Happy Birthday To My Love')
print(law.lower())

#concatenation
a = 'beautiful'
b = 'day'
c = a+ " " +b
print(c)

#list

students = ['Gladys', 'Joseph', 'Clarence', 'lawrence', 'Prince', 'Ebenezer', 'Dennis', 'Temesgen']

print(students)

#accessing list items

students = ['Gladys', 'Joseph', 'Clarence', 'lawrence', 'Prince', 'Ebenezer', 'Dennis', 'Temesgen']
print(students [-2])

# ranges of indexes

students = ['Gladys', 'Joseph', 'Clarence', 'lawrence', 'Prince', 'Ebenezer', 'Dennis', 'Temesgen']
print(students [:5])

# change list items

students = ['Gladys', 'Joseph', 'Clarence', 'lawrence', 'Prince', 'Ebenezer', 'Dennis', 'Temesgen']
students [5] = 'George'
print(students)

# insert into list

students = ['Gladys', 'Joseph', 'Clarence', 'lawrence', 'Prince', 'Ebenezer', 'Dennis', 'Temesgen']
students. insert(2, 'Nelson')
print(students)

# appending to list
students = ['Gladys', 'Joseph', 'Clarence', 'lawrence', 'Prince', 'Ebenezer', 'Dennis', 'Temesgen']
students.append('Festus')
print(students)

#remove items from list

students = ['Gladys', 'Joseph', 'Clarence', 'lawrence', 'Prince', 'Ebenezer', 'Dennis', 'Temesgen']
students.remove('lawrence')
print(students)
