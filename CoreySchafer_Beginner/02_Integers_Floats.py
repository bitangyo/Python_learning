
#integer = whole number, float = decimal
num = 3
num2 = 3.14

print(type(num))
print(type(num2))

# Arithmetic Operators:
# Addition:         3 + 2
# Subtraction:      3 - 2
# Multiplication:   3 * 2
# Division:         3 / 2
# Floor Division:   3 // 2
# Exponent:         3 ** 2
# Modulus:          3 % 2

print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 // 2)
print(3 ** 2)
print(3 % 2)

print(2 % 2)
print(3 % 2)
print(4 % 2)
print(5 % 2)

print(3 * 2 + 1)
print(3 * (2 + 1))

num = 1

#num = num + 1
#num += 1 #same as = num + 1
num *= 10 #same as = num * 10 #this is a way to save some characters

print(num)

print(abs(-3)) # absolute number equals 3 in this case
print(round(3.75)) # rounds to whole number
print(round(3.75, 1)) # rounds to first digit after the decimal

# Coimparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 <2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

#These comparisons will return booleans which are true/false values, boolean details coming up in future video

num_1 = 3
num_2 = 2

print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_1 < num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)

num_1 = '100'
num_2 = '200'

print(num_1 + num_2)
print(int(num_1) + int(num_2)) # cast variable as int