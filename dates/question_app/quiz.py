import datetime
import random

from question import Add, Multiply


class Quiz:
    questions = []
    answers = []

    def __init__(self):
        question_types = (Add, Multiply)
        #gen 10 random questions with nums 1 to 10
        for _ in range (10):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            question = random.choice(question_types)(num1, num2)
            #  add these questions into self.questions
            self.questions.append(question)

    def take_quiz(self):
        # log the start time 
        self.start_time = datetime.datetime.now()

        # ask all of the questions
        for question in self.questions:
            # log if they got the question right
            self.answers.append(self.ask(question))
        else:
            #  log the end time
            self.end_time = datetime.datetime.now()

        # show a summary
        return self.summary()

    def ask(self, question):
        correct = False
        # log the start time
        question_start = datetime.datetime.now()

        # capture the answer
        answer = input(f"{question.text} = ")

        # check the answer
        if answer == str(question.answer):
            correct = True

        # log the end time
        question_end = datetime.datetime.now()

        return correct, question_end - question_start

    def total_correct(self):
        #return the # questions correct
        total = 0
        for answer in self.answers:
            if answer[0]:
                total += 1
        return total

    def summary(self):
        # print how many you got right and the total # num of questions. 5/10
        print(f"You got {self.total_correct()} out of {len(self.questions)} right")
        # print the total time for the quiz: 30 seconds!
        print(f"It took you {(self.end_time-self.start_time).seconds} seconds total.")

Quiz().take_quiz()