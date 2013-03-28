import random
import sys
from playerclass import Player


class ComputerPlayer(Player):

    def __init__(self, l, w, a, b, c, d, name):
        '''
        '''

        Player.__init__(self, l, w, a, b, c, d, name)
        # This retrieves each of the attribute values from the board class
        self.l = l
        self.w = w
        self.num_battleships = a
        self.num_cruisers = b
        self.num_frigates = c
        self.num_minesweepers = d
        self.name = name

        # A list of the boat's coordinates
        self.coordinates = []

        # A list of the coordinates for each random hit
        self.hitlist = []

        # A list of the opponents coordinates for the ships
        self.opp_list = []

    def place_ships(self):
        '''(self) -> NoneType
        Given the number of ships, place them randomly on the game board.
        '''
        # list of numbers of each ship
        list_num_ships = [self.num_battleships, self.num_cruisers, \
                          self.num_frigates, self.num_minesweepers]

        # list of coordinates (tuples) occupied on player's board
        self.coordinates = []
        # default setting for boolean value
        # to check if new coordinates are occupied
        on_board = False

        while list_num_ships != [0, 0, 0, 0]:

            if list_num_ships[0] != 0:   # place battleships first
                # produces a random integer, 0 results in horizontal placement,
                # 1 in vertical
                temp = random.randint(0, 1)
                if temp == 0:   # horizontal placement
                    temp_x = random.randint(0, (self.l - 6))
                    temp_y = random.randint(0, (self.w - 1))
                    # list that contains coordinates
                    #(tuples) of potential coordinates
                    temp_list = [(temp_x, temp_y), (temp_x + 1, temp_y), \
                                 (temp_x + 2, temp_y), (temp_x + 3, temp_y), \
                                 (temp_x + 4, temp_y)]
                else:           # veritcal placement
                    temp_x = random.randint(0, (self.l - 1))
                    temp_y = random.randint(0, (self.w - 6))
                    temp_list = [(temp_x, temp_y), (temp_x, temp_y + 1),\
                                 (temp_x, temp_y + 2), (temp_x, temp_y + 3),\
                                 (temp_x, temp_y + 4)]
                for i in temp_list:
                    if i in self.coordinates:
                        # boolean value to check if any
                        # of the coordinates are occupied
                        on_board = True
                if not on_board:
                    for i in temp_list:
                        self.coordinates.append(i)  # add coordinates to board
                    # remove one from number of battleships to put on board
                    list_num_ships[0] = list_num_ships[0] - 1
                on_board = False  # reset occupancy flag

            elif list_num_ships[1] != 0:      # place cruisers second
                # Produces a random integer, 0 results in horizontal placement,
                # 1 in vertical
                temp = random.randint(0, 1)
                if temp == 0:   # horizontal placement
                    temp_x = random.randint(0, (self.l - 5))
                    temp_y = random.randint(0, (self.w - 1))
                    # list that contains coordinates
                    # (tuples) of potential coordinates
                    temp_list = [(temp_x, temp_y), (temp_x + 1, temp_y), \
                                 (temp_x + 2, temp_y), (temp_x + 3, temp_y)]
                else:           # veritcal placement
                    temp_x = random.randint(0, (self.l - 1))
                    temp_y = random.randint(0, (self.w - 5))
                    temp_list = [(temp_x, temp_y), (temp_x, temp_y + 1),\
                                 (temp_x, temp_y + 2), (temp_x, temp_y + 3)]
                for i in temp_list:
                    if i in self.coordinates:
                        # boolean value to check if any of
                        # the coordinates are occupied
                        on_board = True
                if not on_board:
                    for i in temp_list:
                        self.coordinates.append(i)  # add coordinates to board
                    # remove one from number of cruisers to put on board
                    list_num_ships[1] = list_num_ships[1] - 1
                on_board = False  # reset occupancy flag

            elif list_num_ships[2] != 0:      # place frigates third
                # produces a random integer, 0 results in horizontal placement,
                # 1 in vertical
                temp = random.randint(0, 1)
                if temp == 0:   # horizontal placement
                    temp_x = random.randint(0, (self.l - 4))
                    temp_y = random.randint(0, (self.w - 1))
                    # list that contains coordinates (tuples)
                    # of potential coordinates
                    temp_list = [(temp_x, temp_y), (temp_x + 1, temp_y), \
                                 (temp_x + 2, temp_y)]
                else:           # veritcal placement
                    temp_x = random.randint(0, (self.l - 1))
                    temp_y = random.randint(0, (self.w - 4))
                    temp_list = [(temp_x, temp_y), (temp_x, temp_y + 1), \
                                 (temp_x, temp_y + 2)]
                for i in temp_list:
                    if i in self.coordinates:
                        # boolean value to check if any of
                        # the coordinates are occupied
                        on_board = True
                if not on_board:
                    for i in temp_list:
                        self.coordinates.append(i)  # add coordinates to board
                    # remove one from number of frigates to put on board
                    list_num_ships[2] = list_num_ships[2] - 1
                on_board = False  # reset occupancy flag

            elif list_num_ships[3] != 0:      # place minesweepers last
                # produces a random integer, 0 results in horizontal placement,
                # 1 in vertical
                temp = random.randint(0, 1)
                if temp == 0:   # horizontal placement
                    temp_x = random.randint(0, (self.l - 3))
                    temp_y = random.randint(0, (self.w - 1))
                    # list that contains coordinates (tuples)
                    # of potential coordinates
                    temp_list = [(temp_x, temp_y), (temp_x + 1, temp_y)]
                else:           # veritcal placement
                    temp_x = random.randint(0, (self.l - 1))
                    temp_y = random.randint(0, (self.w - 3))
                    temp_list = [(temp_x, temp_y), (temp_x, temp_y + 1)]
                for i in temp_list:
                    if i in self.coordinates:
                        # boolean value to check if any of
                        # the coordinates are occupied
                        on_board = True
                if not on_board:
                    for i in temp_list:
                        self.coordinates.append(i)  # add coordinates to board
                    # remove one from number of minesweepers to put on board
                    list_num_ships[3] = list_num_ships[3] - 1
                on_board = False  # reset occupancy flag

    def opp_coord_copy(self, lst):
        '''(self, list) -> NoneType
        Return a copy of the opponents list to place each of the hits
        '''
        self.opp_list = lst

    def random_hit(self):
        '''(self) -> NoneType
        Attack a random square on the player's board. Keep track of whether or
        not the game is a victory.
        '''
        x = random.randint(0, (self.l - 1))    # a random x-coordinate
        y = random.randint(0, (self.w - 1))    # a random y-coordinate
        t = (x, y)
        if t in self.hitlist:  # If an attack has already been made
            self.random_hit()  # Recurse the function to ask again
        else:
            self.hitlist.append(t)  # add the attack to the list of attacks
            if t in self.opp_list:
                self.opp_list.remove(t)

        if self.opp_list == []:
            self.victory()

    def victory(self):
        ''' (Self, None) -> str
        Return the winner of the game.
        '''
        print "Congratulations Computer, you win!"
        sys.exit("Thank you for playing!")
