# 1. Write a function to reverse a string.
def reverse_string(s):
    return s[::-1]
  
print(reverse_string("hello"))  # Output: "olleh"

# 2. Write a function to check if a given string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]
  
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False

# 3. Write a function to find the largest element in a list.
def find_largest_element(lrg):
    if not lrg:
        return None
    largest = lrg[0]
    for element in lrg:
        if element > largest:
            largest = element
    return largest

print(find_largest_element([3, 5, 7, 2, 8]))  # Output: 8

# 4. Write a function to find the factorial of a number.
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# 5. Write a function to count the frequency of elements in a list.
def count_frequency(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

print(count_frequency([1, 2, 2, 3, 3, 3]))  # Output: {1: 1, 2: 2, 3: 3}

# 6. Write a function to remove duplicates from a list while maintaining the order.
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 3, 3]))  # Output: [1, 2, 3]

# 7. Write a function to find the intersection of two lists.
def intersection(list1, list2):
    return list(set(list1) & set(list2))

print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))  # Output: [3, 4]

# 8. Write a function to implement a simple calculator that can add, subtract, multiply, and divide.
def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            return 'Error: Division by zero'
        return a / b
    else:
        return 'Invalid operation'

print(calculator(10, 5, 'add'))        # Output: 15
print(calculator(10, 5, 'subtract'))   # Output: 5
print(calculator(10, 5, 'multiply'))   # Output: 50
print(calculator(10, 5, 'divide'))     # Output: 2.0

# 9. Write a function to check if a given number is odd or even.
def is_odd_or_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_odd_or_even(4))  # Output: "Even"
print(is_odd_or_even(7))  # Output: "Odd"

# 10. Write a function to check if a given string contains any vowels.
def contains_vowel(s):
    vowels = 'aeiouAEIOU'
    return any(char in vowels for char in s)

print(contains_vowel("hello"))  # Output: True
print(contains_vowel("sky"))    # Output: False

# 11. Write a function to find the largest (longest) word in an array of words.
def find_largest_word(words):
    if not words:
        return None
    largest_word = max(words, key=len)
    return largest_word

words = ["apple", "banana", "cherry", "blueberry", "kiwi"]
print(find_largest_word(words))  # Output: "blueberry"

# 12. Write a function to get the current date.
from datetime import datetime

def get_current_date():
    return datetime.now().date()

print(get_current_date())  # Output: 2024-07-10 






