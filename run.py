from random import randint


class Ships:
    """
    Store positions of ships and opponent guesses
    """
    grid_size = 5
    number_of_ships = 4

    def __init__(self):
        self.coordinates = []
        self.guesses = []

    def position_ships(self):
        """
        Generate random positions for ships
        """
        for _ in range(Ships.number_of_ships):
            self.coordinates.append((randint(0, Ships.grid_size - 1), randint(0, Ships.grid_size - 1)))
        print(self.coordinates)

    
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
    """Has method to guess opponent ship coordinates and print grid
    """
    def __init__(self):
        Human.__init__(self)
        Ships.__init__(self)
        self.my_guesses = []

    def guess_coordinates(self):
        """User enters opponent ship coordinates to try to hit
        """
        x = input("Guess x-coordinate:\n")
        y = input("Guess y-coordinate:\n")
        self.my_guesses.append((int(x), int(y)))
        #print(self.my_guesses)

    def print_grid(self):
        """
        Print grid. Ships are shown as "@" and hits as "X"
        """
        for i in range(Ships.grid_size):
            for j in range(Ships.grid_size):
                hit = False
                for (x, y) in self.guesses:
                    hit = (i, j) == (x, y)
                    if hit:
                        print('X ', end=' ')
                        break
                if not hit:
                    found_ship = False
                    for (x, y) in self.coordinates:
                        found_ship = (i, j) == (x, y)
                        if found_ship:
                            print('@ ', end=' ')
                            break
                    if not found_ship:
                        print('. ', end=' ')                     
            print('')


class ComputerPlayer(Ships):
    """Has method to guess opponent ship coordinates and print grid
    """
    def __init__(self):
        Ships.__init__(self)
        self.my_guesses = []

    def guess_coordinates(self):
        """Computer generates random opponent ship coordinates to try to hit
        """
        self.my_guesses.append((randint(0, Ships.grid_size - 1), randint(0, Ships.grid_size - 1)))
        #print(self.my_guesses)

    def print_grid(self):
        """
        Print grid. Ships are not shown, hits are shown as 'X'
        """
        for i in range(Ships.grid_size):
            for j in range(Ships.grid_size):
                hit = False
                for (x, y) in self.guesses:
                    hit = (i, j) == (x, y)
                    if hit:
                        print('X ', end=' ')
                        break
                if not hit:
                    print('. ', end=' ')                     
            print('')


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
player.position_ships()
player.print_grid()

computer = ComputerPlayer()
computer.position_ships()
computer.print_grid()
print('')

computer.guess_coordinates()
player.guesses = computer.my_guesses
print(f"Computer guessed {player.guesses}")
print('')

player.guess_coordinates()
computer.guesses = player.my_guesses
print(f"{player.name} guessed {computer.guesses}")
print('')

player.print_grid()
print('')
computer.print_grid()
