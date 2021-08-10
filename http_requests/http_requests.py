import requests
from colorama import init
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

init()

header = figlet_format('Dad Joke 3000')
intro = colored(format(header), color = 'magenta')
print(intro)

user_input = input("What would you like to search for? ")
url = 'https://icanhazdadjoke.com/search'

res = requests.get(
	url, 
	headers={"Accept": "application/json"},
	params={"term": user_input}
).json()

num_jokes = res["total_jokes"]
results = res["results"]

if num_jokes > 1:
	print(f"I found {num_jokes} jokes about {user_input}. Here's one:")
	print(choice(results)["joke"])
elif num_jokes == 1:
	print(f"I found 1 joke about {user_input}:")
	print(results[0]['joke'])
else:
	print(f"Sorry, couldn't find any jokes with your term: {user_input}")