# Example 1
x = "Hello World"
print(x)

# Example 2

y = 'haiiiiiiii'
print(y)

# Example 3
z='Python'
print('Hello'+ z)
print("Hello"+ z)

# Example 4 - print string with Quotation Mark

print('"Hello Python"')

# Example 4 - To find out the length of the String
a = "Hello World"
print(len(a))
print ("The length of the string is %d" %len(a))

# Example 5 - To find out the index of a letter in  the String

a = "Hallo World"
print(a.index("W"))


# Example 6 - To find out the count of  letter in  the String
a = "Hello World"
print(a.count("l"))

# Example 7 - To display the  letter in  the String of specific Index
a = "Hello World"
print(a[3:7])


# Example 8 -This prints the characters of string from 3 to 7 skipping one character. This is extended slice syntax. The general form is [start:stop:step].

a = "Hello world!"
print(a[3:7])
print(a[3:7:1])

# Example 9 -There is no function like strrev in C to reverse a string. But with the above mentioned type of slice syntax you can easily reverse a string like this
a = "Hello world!"
print(a[::-1])

# Example 10 -Upper and Lower Case Functions
a = "Hello world!"
print(a.upper())
print(a.lower())
# Example 10 - Star and End with functions
a = "Hello world!"
print(a.startswith("Hello"))
print(a.endswith("Hello"))
print(a.endswith("world!"))

# Example 11 - Split functions

a = "Hello world!"
b = a.split(" ")
print(b)







