from random import randint


class Ships:
    """
    Store positions of ships and guesses
    """
    grid_size = 5
    Number_of_ships = 4

    def __init__(self):
        self.guess_list = []
        self.coordinates = []

    def position(self):
        """
        Generate random positions for ships
        """
        for _ in range(Ships.Number_of_ships):
            self.coordinates.append((randint(0, Ships.grid_size - 1), randint(0, Ships.grid_size - 1)))
        print(self.coordinates)

    def print_grid(self):
        """
        Print grid
        """
        for i in range(Ships.grid_size):
            for j in range(Ships.grid_size):
                for x_y in self.coordinates:
                    found = (i, j) == x_y
                    if found:
                        print('@ ', end=' ')
                        break
                if not found:
                    print('. ', end=' ')
            print('')

    #@property
    #def guess_list(self):
        
    #    return self._guess_list


class Human:
    """ 
    Has method to input name
    """
    def __init__(self):
        """
        User inputs name
        """
        self.name = input("Enter your name:\n")


class HumanPlayer(Ships, Human):
    """Has method to guess coordinates
    """
    def __init__(self):
        Human.__init__(self)
        Ships.__init__(self)

    def guess_coordinates(self):
        """User enters x and y coordinates to try to hit computer ship
        """
        x = input("Guess x-coordinate:\n")
        y = input("Guess y-coordinate:\n")
        self.guess_list.append((int(x), int(y)))
        print(self.guess_list)

def print_game_info():
    print("Welcome to the Battleship game!\n")

def is_data_valid():
    return

def display_hit_or_miss():
    return

def display_score():
    return

#print_game_info()

#while repeat and !noship:
 #   while not is_data_valid():
 #       guess_coordinates()
#    display_hit_or_miss()
  #  display_score()

player = HumanPlayer()
player.guess_coordinates()
print(f"{player.name} guessed {player.guess_list}")
player.position()
player.print_grid()

        

