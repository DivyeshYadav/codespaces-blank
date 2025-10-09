# Random Password Generator
import random
import string

def generate_password(length=12):
	characters = string.ascii_letters + string.digits + string.punctuation
	password = ''.join(random.choice(characters) for _ in range(length))
	return password

if __name__ == "__main__":
	try:
		length = int(input("Enter password length (default 12): ") or 12)
	except ValueError:
		length = 12
	print("Generated password:", generate_password(length))
	