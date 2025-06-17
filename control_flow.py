# 1. Check Even or Odd

# Ask the user for a number. Use an if-else to check if the number is even or odd and print the result.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 2. Sum of First 10 Natural Numbers

# Use a while loop to calculate the sum of the first 10 natural numbers (1 to 10) and print it.

first_num = 11
i = 1
while i < first_num:
    print(i)
    i += 1

# 3. Print All Vowels in a Word

# Ask the user to input a word. Use a for loop and continue to skip consonants and print only vowels from the word.

word = input("Enter a word: ")
vowel = "aeiou"

for i in word:
    if i in vowel:
        print(i)


# 4. Skip Number 5

# Print numbers from 1 to 10, but skip printing 5 using the continue statement.

for i in range(1,11):
    if i == 5:
        continue
    print(i)

# 5. FizzBuzz (Classic)
# Write a program that prints numbers from 1 to 50:

# For multiples of 3, print "Fizz" instead of the number.

# For multiples of 5, print "Buzz".

# For multiples of both 3 and 5, print "FizzBuzz".

for i in range(1,51):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

# 6. Password Strength Checker

# Ask the user to enter a password.
# Use if-elif-else to check:

# If it's less than 6 characters → "Weak"

# If it contains numbers and letters → "Strong"

# If it's only letters → "Medium"
# (Use loops or any() if you know it; else, just practice with for and if.)

password = input("Enter a password: ")

if len(password) < 6:
    print("Weak")
elif password.isalpha() == True:
    print("Medium")
elif password.isalnum() == True:
    print("Strong")
else:
    print("Invalid Password Type")
    

# 7. Count Vowels and Consonants

# Take a string input from the user.
# Loop through each character and use if to count how many vowels and consonants are there.
# # Ignore spaces and symbols.

word = input("Enter a word: ")
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for i in word:
    if i == " ":
        continue
    elif i in vowels:
        vowel_count += 1
    else:
        consonant_count += 1
print(f' vowel : {vowel_count} and consonant : {consonant_count}')
        

# 8. Palindrome Detector (Loop Version)

# Ask the user for a word and check if it’s a palindrome (same forwards and backwards) without using slicing ([::-1]).
# Use a for or while loop and compare characters from start and end.

word = input("Enter a word: ")
temp = ""
for i in range(len(word) -1, -1 , -1):
    temp += word[i]
if temp == word:
    print("A Palindrome")
else:
    print("Not a Palidrome")

# 9. Ask the user for a number n. Print a number pyramid like this:
#             Input: 5

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

num = int(input("Enter a number: "))
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()