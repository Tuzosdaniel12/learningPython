from cards import Card
import random
#game grid
class Game:
    def __init__(self):
        self.size = 4
        self.card_options = ["Add", "Boo", "Cat", "Dog", "Bat", "Ram", "Rat", "Gum"]
        self.columns = ["A", "B", "C", "D"]
        self.cards = []
        self.locations = []
        #loop tru columns
        for column in self.columns:
            #loop from 1 to size of grid plus 1
            for num in range(1, self.size + 1):
                #create locations
                self.locations.append(f"{column}{num}")

    def set_cards(self):
        #used locations
        use_locations = []
        #loop tru card options to set a location of each card
        for word in self.card_options:
            for i in range(2):
                #check if locations are available by removing duplicates using sets
                available_locations = set(self.locations) - set(use_locations)
                #prick random location from available location
                random_location = random.choice(list(available_locations))
                #added to used location list
                use_locations.append(random_location)
                #create a card by sending a word and the random location
                card = Card(word, random_location)
                #append cards to list of cards
                self.cards.append(card)

    def create_row(self, num):
        row = []
        for column in self.columns:
            for card in self.cards:
                if card.location == f"{column}{num}":
                    if card.matched:
                        row.append(str(card))
                    else:
                        row.append("   ")
        return row

    def create_grid(self):
        header = " |  " + "  |  ".join(self.columns) + "  |"
        print(header)
        for row in range(1, self.size + 1):
            print_row = f"{row}| "
            get_row = self.create_row(row)
            print_row += " | ".join(get_row) + " |"
            print(print_row)
    def check_match(self, loc1, loc2):
        cards = []
        for card in self.cards:
            if card.location == loc1 or card.location == loc2:
                cards.append(card)
        if cards[0] == cards[1]:
            cards[0].matched = True
            cards[1].matched = True  
            return True
        else: 
            for card in cards:
                print(f"{card.location}: {card}")
            return False  
    def check_win(self):
        for card in self.cards:
            if not card.matched:
                return False
        return True
    def check_location(self, time):
        while True:
            guess = input(f"What's the location of your {time} card? ")
            if guess.upper() in self.locations:
                return guess.upper()
            else:
                print("Thats's not a valid location. It should look like this: A1")
    def start_game(self):
        game_running = True
        print("Memory Game")
        self.set_cards()
        while game_running:
            game.create_grid()
            guess1 = self.check_location("First")
            guess2 = self.check_location("Second")
            if self.check_match(guess1, guess2):
                if self.check_win():
                    print("Congrats, You Won!!!!")
                    self.create_grid()
                    game_running = False
            else:
                is_playing = input("Those cards are bot a match. Press any key to continue N to exit ")
                if is_playing.upper() == "N":
                    game_running = False
        print("Game Over")

        
if __name__ == "__main__":
    game = Game()
    game.start_game()

