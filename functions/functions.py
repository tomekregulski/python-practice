def sum_all_nums(num1, num2, num3):
	return num1+num2+num3

print(sum_all_nums(4,5,6))

# example *Args

def sum_all_nums_star_args(*args):
	total=0
	for num in args:
		total += num
	return total

print(sum_all_nums_star_args(4,5,6))
print(sum_all_nums_star_args(4,5,6,7,8))
print(sum_all_nums_star_args(4,5,6,1,2,3,4))

nums = (1,2,3,4,5,6)

print(sum_all_nums_star_args(*nums))

def sum_rest_nums(num1,*args):
	print(num1)
	total=0
	for num in args:
		total += num
	return total

print(sum_rest_nums(4,5,6))
print(sum_rest_nums(4,5,6,7,8))
print(sum_rest_nums(4,5,6,1,2,3,4))

# can be used to cherry pick/search for specific piece of info

def cherry_pick(*args):
	if "Tomek" in args:
		return "Welcome back!"
	return "Not sure who you are..."

print(cherry_pick(1, True, 'Tomek', 35, "berry"))

def fav_colors(**kwargs):
	print(kwargs)
	for person, color in kwargs.items():
		print(f"{person}'s favorite color is {color}")

fav_colors(colt='purple', ruby='red', ethel='teal')

def special_greeting(**kwargs):
	if "David" in kwargs and kwargs["David"] == "special":
		return "You get a special greeting David!"
	elif "David" in kwargs:
		return f"{kwargs['David']} David!"

	return "Not sure who this is..."

print(special_greeting(David='Hello'))
print(special_greeting(Bob='hello'))
print(special_greeting(David='special'))
print(special_greeting(Heather='hello', David='special'))

# example of order of parameters
def display_info(a, b, *args, instructor="Colt", **kwargs):
	return [a,b,args,instructor,kwargs]

print(display_info(1,2,3,first_name="Tomek", last_name="Regulski"))

def display_name(first, second):
	print(f"hello {first} {second}")

names = {"first": "Tomek", "second": "Regulski"}

display_name(**names)

def add_and_multiply(a,b,c,**kwargs):
	print(a + b * c)
	print('other things')
	print(kwargs)\


data = dict(a=1, b=2, c=3, d=55,name='Tony')

add_and_multiply(**data, cat='blue')