shopping = []

def show_help():
    print("What should we pick up at the store?")
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for this help.
    Enter 'SHOW' to display list.
    """)

    
def add_to_list(item):
    shopping.append(item)
    print("{} was added to shopping list. You have {} items in shopping list".format(item, len(shopping)))


def display_list(shopping, action):
    print("HERE IS YOUR {} LIST: ".format(action))
    for item in shopping:
        print("* {}".format(item))


show_help()


while True:
    new_item = input("> ")
    if new_item.upper() == 'DONE':
        display_list(shopping, 'FINAL')
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        display_list(shopping, 'CURRENT')
        continue
    add_to_list(new_item)
    