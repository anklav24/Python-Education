"""
Sample Input:

4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic
Sample Output:

stepic
champignons
the
"""
dictionary_len = int(input())
dictionary = []
for i in range(dictionary_len):
    dictionary += input().lower().split()

words_count = int(input())
words = []
for i in range(words_count):
    words += input().lower().split()
for word in set(words):
    if word not in dictionary:
        print(word)

