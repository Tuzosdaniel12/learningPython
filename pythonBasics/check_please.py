import math

def split_check(total, num_of_people):
    if num_of_people <= 1:
        raise ValueError("More then one person is require to split the check")
    return math.ceil(total / num_of_people)

try:
    total_due = float(input("What is the total of the bill? "))
    num_of_people = int(input("How many people are spliting the check? "))
    amount_per_person = split_check(total_due, num_of_people)
except ValueError as err:
    print("Oh no! Thats not a valid value. Try again....")
    print("{}".format(err))
else:
    print("Each person owes {}".format(amount_per_person))
