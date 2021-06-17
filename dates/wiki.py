import datetime

answer_format = "%m/%d"
link_format =  "%b_%d"
link = "https://en.wikipedia.org/wiki/{}"

while True:
    answer = input("What date would you like? Pleae use the MM/DD format. Enter 'quit' to quit. ")
    if answer.upper() == "QUIT":
        break
    
    try:
        date = datetime.datetime.strptime(answer, answer_format)
        #convert the date back to string
        output = link.format(date.strftime(link_format))
        print(output)
    except ValueError:
        print("Thats not a valid Date. Please try again")
