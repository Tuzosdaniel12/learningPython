def yell(text):
    text = text.upper()
    number_of_char = len(text)
    print(text + "!" * (number_of_char // 2))

yell("You are doing great")
yell("Don't forget to ask for help")
yell("don't repeat yourself. keep things dry")

