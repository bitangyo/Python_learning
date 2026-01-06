
courses = ['History', 'Math', 'Physics', 'CompSci'] # the squared brackets distinguished this 
#as a list from a variable, the list contains a number of values in this case strings

print(courses) #prints all the contents of the courses list
print(len(courses)) #prints the number of values contained in the list
print(courses[0]) #gives the value in the 0th position in the list
print(courses[3]) #gives the last value of a list with a length of four
print(courses[-1]) #gives the last value of a list regardless of length

print(courses[0:2]) # beginning included end point not (positions 0 to 1)
print(courses[:2]) # beginning included end point not (positions 0 to 1)
print(courses[2:]) # beginning included end point not (positions 2 till the end)

courses.append('Art') # adds value to the end of the list
print(courses)

courses.insert(0, 'Art') # adds value to a specified location in the list
print(courses)

courses_2 = ['Art', 'Education']

#courses.insert(0, courses_2) # inserts the whole list into the list including the brackets
#print(courses[0])
courses.extend(courses_2) # adds the individual values correctly to the list
print(courses)

## Removing values from a list
courses.remove('Math') #removes the value from the list
courses.remove('Art') #it removes the first instance if there are multiple of the same value

courses.pop() #removes the last value in the list
popped = courses.pop() #removes the last value and saves it as an individual variable

print(popped)
print(courses)

## Reversing and sorting a list
courses.reverse()
print(courses)
nums = [1,5,2,4,3]
courses.sort() #sorts string lists in alphabetical order
nums.sort() #sorts numerical lists in ascending order
print(courses)
print(nums)

courses.sort(reverse=True) #sorts string lists in reverse alphabetical order
nums.sort(reverse=True) #sorts numerical lists in descending order
print(courses)
print(nums)

#the above methods modify the lists themselves, the below function returns the list in the sorted manner, while the list remains unchanged

print(sorted(courses))
sorted_courses = sorted(courses) #can of course be set as a new variable

#functions for numerical lists
print(min(nums))
print(max(nums))
print(sum(nums))

#Get the position/index of a value in a list
print(courses.index('CompSci'))
#print(courses.index('beepboop')) #gives error that value is not in the list
print('beepboop' in courses) # Returns True/False depending on the value being in the list
print('Art' in courses)

for item in courses:
    print(item)

for course in courses:
    print(course)

for index, course in enumerate(courses, start=1):
    print(index, course)

course_str = ' - '.join(courses) #truns list into a single string, separateing values with specified separator
print(course_str)
new_list = course_str.split(' - ') #turns sting into list splitting to values by specified separator
print(new_list)

##tuples - like a list but cannot be modified (mutable vs immutable) list mutable, tuple immutable

# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)


#Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

#tuple_1[0] = 'Art' #give error as tuple is immutable, for this reson mehtods that modify the object cannot be used with a tuple

print(tuple_1)
print(tuple_2)

# Sets - unordered with no duplicates
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'} #duplicates are simpli listed once in the output
art_courses = {'History', 'Math', 'Art', 'Design', 'Math'}

print(cs_courses)
print('Math' in cs_courses) #Sets do this operation much more efficiently than lists or tuples
print(cs_courses.intersection(art_courses)) #returns the values present in both sets
print(cs_courses.difference(art_courses)) #returns the values present in cs_courses, but not in art
print(art_courses.difference(cs_courses)) #returns the values present in cs_courses, but not in art
print(art_courses.union(cs_courses))#returns the values present in either set
#these are again much more efficient with sets compared to lists or tuples

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()