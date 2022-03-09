from random import randint

class ships:
    grid_size = 0
    Number_of_ships = 0

    def __init__(self):
        self.guess_list = []
        return

    def position(self):
        coordinates = []

    #@property
    #def guess_list(self):
        
    #    return self._guess_list

class human:
    def input_name(self):
        self.name = input("Enter your name:\n")
    

class human_player(ships, human):
    

    def guess_coordinates(self):
        x = input("Guess x- coordinate:\n")
        y = input("Guess y- coordinate:\n")
        self.guess_list.append([x, y])
        print(self.guess_list)
        print(self.name)






def print_game_info():
    print("Welcome to the Battleship game!\n")

player = human_player()
player.input_name()
player.guess_coordinates()
print(f"{player.name} guessed {player.guess_list}")
    

def place_ships():
    return


def is_data_valid():
    return

def display_hit_or_miss():
    return

def display_score():
    return

print_game_info()

#my_ships.position():

#while repeat and !noship:
 #   while not is_data_valid():
 #       guess_coordinates()
#    display_hit_or_miss()
  #  display_score()
        

