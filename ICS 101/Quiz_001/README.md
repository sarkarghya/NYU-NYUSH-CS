# Q4.1 Counting letters in a word
## 20 Points
Write a function, named count_letters, which takes a string (i.e., a word without spaces or punctuations) as the input and returns a Python dictionary. The function counts the occurrences of the letters in the string. In the returned Python dictionary, the keys are the letters, and the values are the number of occurrences of the letters respectively. The following figure shows an example when the input string is “banana”,
```
>>> result = count_letters("banana")
>>> print(result) 
{'b': 1, 'a': 3, 'n': 2}
```
Write a function, named count_letter_pairs, which counts the occurrences of the letter-pairs in a string. Here, a letter-pair means a set of consecutive letters in the string of a specified length. For example, in “banana”, the letter-pairs of length 2 are “ba”, “na”, and “an”. The function has two input arguments, a string and the length of the letter-pair, and it returns a Python dictionary in which the keys are the letter-pairs of the given length, and the values are the number of occurrences of the letter pairs respectively. The following figure shows an example when the input string is “banana”,
```
>>> result = count_letter_pairs("banana", 2)
>>> print(result) 
{'ba': 1, 'an': 2, 'na': 2}
```
# Q4.2
## 25 Points
You are given a string, several characters, several indices, and an indices group, which are like the following:
```
##String: 
s = "abcdefg"
##Characters: 
chars = ["a", "d", "g", "e"]
##Indices: 
idxes = [0, 2, 1, 6]
##Indices_group: 
groups = [[0, 2, 1, 6], [9, 7]]
```
Write a function pick_out_alphabets(s, idxes), which returns a list whose elements are those alphabets corresponding to indices in idxes. Your code should have the following output.
```
>>> s = "helloworld"
>>> idxes = [0, 1, 2, 8]
>>> pick_out_alphabets(s, idxes)
['h', 'e', 'l', 'l']
>>> idxes = [1, 7, 7, 4, 7]
>>> pick_out_alphabets(s, idxes)
['e', 'r', 'r', 'o', 'r']
```
Write a function replace_alphabet(s, chars, idxes), which replaces the characters in s by the characters in chars. The position of the i-th element in chars is specified by the i-th element in idxes. Your code should have the following output.
```
>>> s = 'tears'
>>> chars = ['w', 'e', 'o', 'l']
>>> idxes = [2, 3, 1, 4]
>>> replace_alphabets(s, chars, idxes)
'towel'
>>> s = 'hellokelly'
>>> chars = ["t", "i", "t"]
>>> idxes = [7, 6, 8]
>>> replace_alphabets(s, chars, idxes)
'hellokitty'
```
An index-list is an element in an indices_group, which is a list of string indices. You can swap the characters of a string within any index-list for any number of times. For example, when there is a ```groups = [[0, 1, 2,], [5, 6]]``` and a string ```s = “abcdefg”```, swapping among “a”, “b”, and “c” and swapping between “e” and “f” are allowed. (Please note: there are no intersections between any two index-lists.)
Write a function alphabetical_smallest(s, groups), which returns the alphabetically smallest string by swapping characters within the given index-lists. Your code should have the following output,
```
>>> s = 'gfedcba'
>>> group = [[0, 1, 2, 3, 4, 5, 6]]
>>> lexic_smallest(s, group)
'abcdefg'
>>> s = 'gfedcba'
>>> group = [[0, 1, 2, 3], [5, 6]]
>>> lexic_smallest(s, group)
>>> 'defgcab'
```
 [Hint: use the functions you written in (1) and (2).]
Note: To compare the alphabetical order of two strings, we compare the characters in both strings one by one. When different characters are found then the one with small alphabetical order is considered to be smaller. For example, for strings ‘ab’ and ‘ac’, ‘ab’ is alphabetically smaller (i.e., ‘ab’<‘ac’); for strings ‘bafe’ and ‘baef’, ‘baef’ is smaller.
