first_name = input("What is your first name? ")

print("Hello,", first_name)

if first_name == "Daniel":
    print(first_name, "is learning Python")
elif first_name == "Dan":
    print(first_name, "is learning with fellow student in the community! Me too!")
else:
    #ask if user is under or equal the age of 6
    age = int(input("How old are you? "))
    if age <= 6:
        print("Wow you're {} If you are confident in reading already....".format(age))
    print("You should learn Python, {}".format(first_name))

print("Have a great day {}".format(first_name))
