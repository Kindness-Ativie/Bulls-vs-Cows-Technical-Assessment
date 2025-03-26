
# two words of unknown length
word1: str = input('Enter s1: ')
word2: str = input('Enter s2: ')

# find word of minimum length, other word will be comparison word
minimum_word = word1
compare_word = word2

if len(word2) < len(word1):
    minimum_word = word2
    compare_word = word1

# count bulls by using minimum word starting at index of 0
bulls_count = 0
idx = 0
while idx <= len(minimum_word) - 1:
    if minimum_word[idx] == compare_word[idx]:
        bulls_count += 1
    idx += 1

# count cows by removing duplicates in the compare word (largest word)
cows_count = 0
for letter in set(compare_word):
    if letter in minimum_word:
        cows_count += 1

# print outcome of bulls and cows
print(f'Bulls: {bulls_count}\nCows: {cows_count}')