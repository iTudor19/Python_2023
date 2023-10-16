def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in input_string if char in vowels)

def count_occurrences(str1, str2):
    return str2.count(str1)

def is_palindrome(num):
    return str(num) == str(num)[::-1]

import re
def extract_number(text):
    return int(re.search(r'\d+', text).group())

def count_bits(num):
    return bin(num).count('1')

from collections import Counter
def most_common_letter(input_string):
    filtered_string = ''.join(filter(str.isalpha, input_string)).lower()
    count_dict = Counter(filtered_string)
    return max(count_dict, key=count_dict.get)

def count_words(text):
    return len(text.split())
