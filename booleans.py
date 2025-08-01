bool(0)
bool(13)

bool("")
bool("hello")

bool([])
bool([1,4,6])
default_greeting = "there"

name = input("enter your name: (optional) ")
user_name = name or default_greeting
print(f"Hello, {user_name}!")