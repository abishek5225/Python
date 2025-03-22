import random
import string

letters = string.ascii_letters #a-z A-Z
numbers = string.digits # 0-9 digits
symbols = string.punctuation #special characters

all_chars = letters + numbers + symbols

length = int(input("Enter the length of your password:"))

password = ''.join(random.choice(all_chars) for _ in range(length))

print("🔐 Generated Password:", password)