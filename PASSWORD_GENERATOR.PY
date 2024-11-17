import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "012345679"
symbol = "!@#$%^&*()_-+=?<>;:.{}[]"
all_chars = lower + upper + numbers + symbol 
length = int(input("Enter a length: "))

password = ''.join(random.sample(all_chars, length))
print("Generated Password:", password)
