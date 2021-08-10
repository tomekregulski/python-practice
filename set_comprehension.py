print({x**2 for x in range(10)})

# just by adding x: to beginning, we get a dictionary instead

print({x:x**2 for x in range(10)})
print({char.upper() for char in 'hello'})

def are_all_vowels_in_string(string):
	return len({char for char in string if char in 'aeiou'}) == 5

print(are_all_vowels_in_string('hello'))
print(are_all_vowels_in_string('sequeoia'))