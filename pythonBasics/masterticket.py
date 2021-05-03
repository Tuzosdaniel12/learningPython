import sys

TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100

def cal_total_amount(num_of_tickets):
    return (num_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining > 0:
    print("TICKETS REMAINING ARE {}".format(tickets_remaining))
    username = input("What is your name? ").title()
    try:
        num_of_tickets = int(input("{}, how many tickets would you like to buy? ".format(username)))
        if num_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining, Please try again".format(tickets_remaining))
        
    except ValueError as err:
        print("Oh no! Thats not a valid value. Try again....")
        print("{}".format(err))
    else:
        total_amount = cal_total_amount(num_of_tickets)
        print("The total amount for {} tickets is: ${}".format(num_of_tickets, total_amount))
        is_buying = input("Would you like to continue with the purchase of {}tickets for the amount of ${}? please enter Y/n : ". format(num_of_tickets, total_amount))
        if is_buying.lower() == "y":
            print("Thank you for your purchase {} \n".format(username))
            #TODO: Gather CC info to process  the payment
            tickets_remaining -= num_of_tickets
        else:
            print("Thank you anymays, {}! \n".format(username))

print("Sorry tickets are sold out!!")


