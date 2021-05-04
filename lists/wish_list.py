books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
]

# books[1] = "Python for Data Analysis - Wes McKinney"
# print(books[-1]) last book of array


#insert value to arrray based on position
books.insert(0, "Learning Python: Powerful Object_Oriented Programming")

books[0] += " - Mark Lutz"

#deleted a value by using del
#remove or pop a value from array by using .pop()

def display_wishlist(title, wishes):
    items = wishes.copy()
    print("{}:".format(title))
    suggested_gift = items.pop(0)
    print("======>Suggested gift: {}<======".format(suggested_gift))
    for item in items:
        print("* " + item)
    print()    

display_wishlist("Books", books)
display_wishlist("Video Games", video_games)

#this style of looping is used when trying to modified original array, if don't do a copy of original it will cause unexpected results
for book in books.copy():
    books.remove(book)

#.split() splits string in an array

#time.sleep(time_per_iteration_argument) time how often you want the code pause
