'''
Problem:
Sort a list of words by their length and convert them to uppercase using lambda and list comprehension.
Sample Data: words = ["apple", "banana", "pear", "kiwi", "plum", "orange"]
'''

words = ["apple", "banana", "pear", "kiwi", "plum", "orange"]


def sort_by_length_and_uppercase(words):
    if len(words) <1:
        return

    if not all(isinstance(word, str) for word in words):
        raise TypeError("The list contains non-string elements.")

    return [word.upper() for word in sorted(words, key=len, reverse=True)]


print(sort_by_length_and_uppercase(words))
