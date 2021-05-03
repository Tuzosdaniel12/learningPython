import sys 
#constant value in python
MASTER_PASSWORD = "hello"
password = input("Please enter a super secret password: ")
attemp_count = 1
while password != MASTER_PASSWORD:
    if attemp_count > 3:
        sys.exit("To many password attempts")
    password = input("Invalid password, try again: ")
    attemp_count += 1
print("secret town")

for letter in "secret town":
    print(letter.upper())