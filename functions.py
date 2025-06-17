
# # 1. Greet User
# # # Write a function greet_user(name) that prints "Hello, <name>!".

name = input("Enter your name: ")

def greet_user(name):
    print(f'Welcome, {name}')

greet_user(name)

# # 2.  Add Two Numbers
# # # Function add(a, b) that returns the sum of two numbers.

def add_num(a,b):
    print(f'sum of a and b is {a + b}')

add_num(3,4)

# # 3. Check Even or Odd
# # # Write a function is_even(num) that returns True if number is even, else False.

num = int(input("Enter a number: "))
def check_evenodd(num):
    if num % 2 == 0:
        print(f'{num} is Even')
    else:
       print(f'{num} is Odd')
check_evenodd(num)

# # 4.  Square a Number
# # # Function square(n) that returns the square of a number.

num = int(input("Enter a number: "))
def square_num(num):
    print(f'{num * num} is the square of {num}')

square_num(num)

# # 5. Print Multiples of 5
# # # Function print_multiples(n) that prints multiples of 5 up to n.

n = int(input("Enter a number: "))
def multiples(n):
    for i in range(1,n+1):
        print(i * 5)

multiples(n)

# # 6. Factorial Function (Loop)
# # # Write factorial(n) that returns factorial using a loop.

n = int(input("Enter a number: "))
def factorial(n):
    for i in range(n,0,-1):
        print(i, end = " ")
factorial(n)

# # 7. Check Palindrome
# # # Function is_palindrome(s) that returns True if the string s is a palindrome (ignore case and spaces).

s = input("Enter a word: ").lower()
def is_palindrome(s):
    if s == s[::-1]:
        print("Its a Palindrome")
    else:
        print("Its not a Palindrome")

is_palindrome(s)

# # 8. Count Vowels in a String
# # # Write count_vowels(text) returning the number of vowels (a, e, i, o, u) in the string.

text = input("Enter a text: ")
vowels = "aeiou"

def count_vowel(text):
    vowels_count = 0
    for i in text:
        if i in vowels:
            vowels_count += 1
    return vowels_count

print(count_vowel(text))



# # 9. Fibonacci with Recursion
# # # Write a recursive function fib(n) that returns the nth Fibonacci number. Include base cases.



# # 10.  Find Max Consecutive Ones
# # # Write a function max_consecutive_ones(arr) that takes a list of 0s and 1s and returns the maximum count of consecutive 1s.

