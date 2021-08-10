nums = [1,2,3,4,5,6]
doubled_numbers = [num*2 for num in nums]
print(doubled_numbers)

string_nums = [str(num) for num in nums]
print(string_nums)

evens = [num for num in nums if num % 2 == 0]
odds = [num for num in nums if num % 2 == 1]
print(evens)
print(odds)

ifelse = [num*2 if num % 2 == 0 else num/2 for num in nums]
print(ifelse)

friends = ['colt', 'joe', 'ashley']

print([friend[0].upper() + friend[1::] for friend in friends])

with_vowels = "This is so much fun!"

no_vowels = ''.join(char for char in with_vowels if char not in "aeiou")
print(no_vowels)
no_vowels_elipse = '...'.join(char for char in with_vowels if char not in "aeiou")
print(no_vowels_elipse)
no_vowels_no_join = [char for char in with_vowels if char not in "aeiou"]
print(no_vowels_no_join)

nested_list = [[1,2,3],[4,5,6],[7,8,9]]
[[print(val) for val in sub] for sub in nested_list]

board = [[num for num in range(1,4)] for val in range(1,4)]
print(board)

xox = [["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)]
print(xox)