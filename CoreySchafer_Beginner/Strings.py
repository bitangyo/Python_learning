
# Print Welcome Message
print('Hello World')

message = 'Hello World'
#message = 'Bobby's World'
message1 = 'Booby\'s World'
message2 = "Babby's World"

multiline_message = """Bobby's World was a great 
cartoon in the past"""

print(message)

# how many characters are in a variable?
print(len(message))

# get specific positioned character from a string (position is numbered from 0 as the first character)
print(message[10])
print(message[0:5])
print(message[6:]) #leaving out the position of end char just gets all until the end
print(message[:5]) #same goes for leaving out the start char

#data types have methods, method is a function belonging to an object (we will get into it later)
print(message.lower()) #lowercases the string variable
print(message.upper()) #uppercases the string variable
print(message.count('Hello')) #counts the number of occurences of specified string element
print(message.count('l'))
print(message.find('World')) #gives the starting position of the specified string element within the message variable
print(message.find('Universe')) #it gives -1 for not found
print(message.find('l')) #gives position of the first occurence

message.replace('World', 'Universe')
print(message) # does not get replaced if not specified how the replacement should be called
new_message = message.replace('World', 'Universe')
print(new_message)

#Concatenate
greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name + '. Welcome!'
message = '{}, {}. Welcome!'.format(greeting, name)
message = f'{greeting}, {name.upper()}. Welcome!' # you can add methods and do other coding with the variable in an f string

print(message)

#info fuctions
#print(dir(name)) #shows attributes and methods that can be used with the specified variable
#print(help(str)) #gives deeper info of how a variable type works, what can it be used with
print(help(str.lower)) #can be specified to a certiain attribute/method