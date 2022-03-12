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
        self.score = 0

    def rand_coord(self):
        """generates random position
        """
        x = randint(0, Ships.grid_size - 1)
        y = randint(0, Ships.grid_size - 1)

        return (x, y)

    def add_xy_to_list(self, fun, array):
        """
        Add coordinates to a list
        """
        while True:
            (x, y) = fun()
            if (x, y) not in array:
                array.append((x, y))
                break        

    def position_ships(self):
        """
        Generate random positions for ships
        """
        for _ in range(Ships.number_of_ships):
            self.add_xy_to_list(self.rand_coord, self.coordinates)

        print(self.coordinates)

    def hit(self):
        """Checks if opponent hit a ship"
        """
        for (x, y) in self.coordinates:
            hit = self.guesses[-1] == (x, y)
            if hit:
                self.score += 1
                return True
        return hit


class Human:
    """
    Has method to input name
    """
    def __init__(self):
        """
        User inputs name
        """
        while True:
            name = input("Enter your name:\n")
            if name != '':
                break
        self.name = name


class HumanPlayer(Ships, Human):
    """Has method to guess opponent ship coordinates and print grid
    """
    def __init__(self):
        Human.__init__(self)
        Ships.__init__(self)
        self.my_guesses = []

    def input_coord(self):
        """User enters ship coordinates which are then validated
        """
        while True:
            x = input("Guess x-coordinate:\n")
            if x.isdigit():
                x = int(x)
                if 0 <= x < self.grid_size:
                    break
                else:
                    print(f"The coordinates must be between 0 and {self.grid_size - 1}")
            else:
                print("You must enter a number!")

        while True:
            y = input("Guess y-coordinate:\n")
            if y.isdigit():
                y = int(y)
                if 0 <= y < self.grid_size:
                    break
                else:
                    print(f"The coordinates must be between 0 and {self.grid_size - 1}")
            else:
                print("You must enter a number!")

        return (x, y)

    def guess_coordinates(self):
        """User enters opponent ship coordinates to try to hit
        """
        while True:
            (x, y) = self.input_coord()
            if (x, y) not in self.my_guesses:
                self.my_guesses.append((x, y))
                break
            else:
                print(f"You already guessed position {(x, y)}, try again")

    def print_grid(self):
        """
        Print grid. Ships are shown as "@" and shots as "X"
        """
        for i in range(Ships.grid_size):
            for j in range(Ships.grid_size):
                shot = False
                for (x, y) in self.guesses:
                    shot = (i, j) == (x, y)
                    if shot:
                        print('X ', end=' ')
                        break
                if not shot:
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
        self.add_xy_to_list(self.rand_coord, self.my_guesses)
        #print(self.my_guesses)

    def print_grid(self):
        """
        Print grid. Ships are not shown, shots are shown as 'X'
        """
        for i in range(Ships.grid_size):
            for j in range(Ships.grid_size):
                shot = False
                for (x, y) in self.guesses:
                    shot = (i, j) == (x, y)
                    if shot:
                        print('X ', end=' ')
                        break
                if not shot:
                    print('. ', end=' ')                     
            print('')


def print_game_info():
    print("Welcome to the Battleship game!\n")


#print_game_info()

#while repeat and !noship:
 #   while not is_data_valid():
 #       guess_coordinates()
#    display_shot_or_miss()
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
print(f"Computer guessed {player.guesses[-1]}")
if player.hit():
    print("Computer hit")
else:
    print("Computer missed")
print('')

player.guess_coordinates()
computer.guesses = player.my_guesses
print(f"{player.name} guessed {computer.guesses[-1]}")
if computer.hit():
    print("Player hit")
else:
    print("Player missed")
print('')

print(f"score: Computer {player.score} Player {computer.score}")
print('')

player.print_grid()
print('')
computer.print_grid()


computer.guess_coordinates()
player.guesses = computer.my_guesses
print(f"Computer guessed {player.guesses[-1]}")
if player.hit():
    print("Computer hit")
else:
    print("Computer missed")
print('')

player.guess_coordinates()
computer.guesses = player.my_guesses
print(f"{player.name} guessed {computer.guesses[-1]}")
if computer.hit():
    print("Player hit")
else:
    print("Player missed")
print('')

print(f"score: Computer {player.score} Player {computer.score}")
print('')

player.print_grid()
print('')
computer.print_grid()
