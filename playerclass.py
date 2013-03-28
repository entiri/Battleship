import media
import random
import sys
from board import Board


class Player(Board):

    def __init__(self, l, w, a, b, c, d, name):
        '''(Player) -> NoneType
        Stores all of the instance variables and method calls needed for the
        the human player.
        '''
        Board.__init__(self, l, w, a, b, c, d, name)
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

        # The coordinates for the random pick (meant for the random pick for
        # the computer class
        self.coordlist = []

        # a list of all of the coordinates the player has hit
        self.hitlist = []

        # a list of where the opposing player has attacked, regardless of a hit
        # or a miss
        self.attack = []

        # A list containing two seperate images, the first being the player's
        # board, and the second being the opponents board
        self.boards = []

        # A list of the opponents coordinates for the ships
        self.opp_list = []

    def place_ships(self):
        '''(self) -> NoneType
        Given the number of each ship, place each ship randomly on the board,
        given the board's boundaries.
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
                # temp produces a random integer,
                # 0 results in horizontal placement, 1 in vertical
                temp = random.randint(0, 1)
                if temp == 0:   # horizontal placement
                    temp_x = random.randint(0, (self.l - 6))
                    temp_y = random.randint(0, (self.w - 1))
                    # list that contains coordinates (tuples)
                    # of potential coordinates
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
                        # boolean value to check if
                        # any of the coordinates are occupied
                        on_board = True
                if not on_board:
                    for i in temp_list:
                        self.coordinates.append(i)  # add coordinates to board
                    # remove one from number of battleships to put on board
                    list_num_ships[0] = list_num_ships[0] - 1
                on_board = False  # reset occupancy flag

            elif list_num_ships[1] != 0:      # place cruisers second
                # produces a random integer,
                # 0 results in horizontal placement, 1 in vertical
                temp = random.randint(0, 1)
                if temp == 0:   # horizontal placement
                    temp_x = random.randint(0, (self.l - 5))
                    temp_y = random.randint(0, (self.w - 1))
                    # list that contains coordinates
                    # (tuples) of potential coordinates
                    temp_list = [(temp_x, temp_y), (temp_x + 1, temp_y),\
                                 (temp_x + 2, temp_y), (temp_x + 3, temp_y)]
                else:           # veritcal placement
                    temp_x = random.randint(0, (self.l - 1))
                    temp_y = random.randint(0, (self.w - 5))
                    temp_list = [(temp_x, temp_y), (temp_x, temp_y + 1),\
                                 (temp_x, temp_y + 2), (temp_x, temp_y + 3)]
                for i in temp_list:
                    if i in self.coordinates:
                        # boolean value to check if any
                        # of the coordinates are occupied
                        on_board = True
                if not on_board:
                    for i in temp_list:
                        self.coordinates.append(i)  # add coordinates to board
                    # remove one from number of cruisers to put on board
                    list_num_ships[1] = list_num_ships[1] - 1
                on_board = False  # reset occupancy flag

            elif list_num_ships[2] != 0:      # place frigates third
                # produces a random integer,
                # 0 results in horizontal placement, 1 in vertical
                temp = random.randint(0, 1)
                if temp == 0:   # horizontal placement
                    temp_x = random.randint(0, (self.l - 4))
                    temp_y = random.randint(0, (self.w - 1))
                    # list that contains coordinates
                    # (tuples) of potential coordinates
                    temp_list = [(temp_x, temp_y), (temp_x + 1, temp_y), \
                                 (temp_x + 2, temp_y)]
                else:           # veritcal placement
                    temp_x = random.randint(0, (self.l - 1))
                    temp_y = random.randint(0, (self.w - 4))
                    temp_list = [(temp_x, temp_y), (temp_x, temp_y + 1), \
                                 (temp_x, temp_y + 2)]
                for i in temp_list:
                    if i in self.coordinates:
                        # boolean value to check if any
                        # of the coordinates are occupied
                        on_board = True
                if not on_board:
                    for i in temp_list:
                        self.coordinates.append(i)  # add coordinates to board
                    # remove one from number of frigates to put on board
                    list_num_ships[2] = list_num_ships[2] - 1
                on_board = False  # reset occupancy flag

            elif list_num_ships[3] != 0:      # place minesweepers last
                # produces a random integer,
                # 0 results in horizontal placement, 1 in vertical
                temp = random.randint(0, 1)
                if temp == 0:   # horizontal placement
                    temp_x = random.randint(0, (self.l - 3))
                    temp_y = random.randint(0, (self.w - 1))
                    # list that contains coordinates
                    # (tuples) of potential coordinates
                    temp_list = [(temp_x, temp_y), (temp_x + 1, temp_y)]
                else:           # veritcal placement
                    temp_x = random.randint(0, (self.l - 1))
                    temp_y = random.randint(0, (self.w - 3))
                    temp_list = [(temp_x, temp_y), (temp_x, temp_y + 1)]
                for i in temp_list:
                    if i in self.coordinates:
                        # boolean value to check if
                        # any of the coordinates are occupied
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

    def opp_attack_copy(self, L):
        '''(self, list) -> NoneType
        Update the list of where the opposing player has attacked.
        '''
        for item in L:
            if item not in self.attack:
                self.attack.append(item)

    def attack_place(self):
        '''(self) -> NoneType
        Retrieve an x and y coordinate, attack the opposing board at that given
        location.
        '''
        x = int(raw_input('Enter the x-coordinate of where to attack: '))
        while x > (self.w - 1):  # A given value on the x-axis
            x = int(raw_input('Try again. Enter the x-coordinate' + \
                              'of where to attack: '))
        y = int(raw_input('Enter the y-coordinate of where to attack: '))
        while y > (self.l - 1):  # A given value on the y-axis
            y = int(raw_input('Try again.' +
                              'Enter the y-coordinate of where to attack: '))
        t = (x, y)  # save to coodinates as a tuple
        if t in self.hitlist:  # If an attack has already been made
            return self.attack_place()  # Recurse the function to ask again
        else:
            self.hitlist.append(t)
            self.update_boards(t[0], t[1])
            if t in self.opp_list:
                self.opp_list.remove(t)

        if self.opp_list == []:
            self.victory()

    def victory(self):
        ''' (self, None) -> NoneType
        Return the winner of the game.
        '''
        f = self.name
        print "Congratulations " + self.name + ", you win!"
        sys.exit("Thank you for playing!")

    def draw_board(self):
        '''(self) -> NoneType
        draw player board and opponent board and return in list'''

        # Each space will be 25 pixels long, with a 10 pixel border on top
        board_l = self.l * 25 + 10
        # Each space will be 25 pixels wide, with a 10 pixel border on the side
        board_w = self.w * 25 + 10

        list_boards = []   # list holding boards

        # Draw player's board
        board_player = media.create_picture(board_w, board_l, media.navy)

        # Draw opponent's board
        board_opponent = media.create_picture(board_w, board_l, media.gray)

        list_boards.append(board_player)   # Add player board to list
        list_boards.append(board_opponent)  # Add opponent board to list

        for item in list_boards:  # loop through list of boards to add borders
            # Draw bar along top
            media.add_rect_filled(item, 0, 0, 10, board_l, media.white)
            media.add_rect_filled(item, 0, 0, board_w, 10, media.white)
            counter = 0  # counter for while loop to draw numbers to board
            while counter < self.w:  # loop to draw x coordinates on board
                temp = str(counter)
                x_val = (counter) * 25 + 10
                media.add_text(item, x_val, 2, temp, media.black)
                counter += 1
            counter = 0
            while counter < self.l:  # draw y coordinates on board
                temp = str(counter)
                y_val = (counter) * 25 + 10
                media.add_text(item, 2, y_val, temp, media.black)
                counter += 1

        # Loop through list of player ships to place them on board
        for item in self.coordinates:
            media.add_rect_filled(list_boards[0], item[0] * 25 + 10,\
                                  item[1] * 25 + 10, 25, 25, media.gray)
        media.show(list_boards[0])
        media.show(list_boards[1])

        self.boards = list_boards

    def update_boards(self, x, y):
        ''' (self, x, y) -> NoneType
        Given an x and a y coordinate, turn the cooresponding board co-ordinate
        red if it is a hit, or white if it is a miss.
        '''
        # tuple holding coordinates of attack
        coordinates = (x, y)

        # If attack coordinates correspond to a point at which
        # a ship is occupying on the opponent board, draw a red square.
        # if it doesn't, draw a white square.
        if coordinates not in self.opp_list:
            media.add_rect_filled(self.boards[1], x * 25 + 10,\
                                  y * 25 + 10, 25, 25, media.white)
        else:
            media.add_rect_filled(self.boards[1], x * 25 + 10,\
                                  y * 25 + 10, 25, 25, media.red)

        # Draw player's board using opponent's last move.
        # A white block is drawn if they missed, a red block if they hit.
        if self.attack != []:
            if self.attack[-1] not in self.coordinates:
                media.add_rect_filled(self.boards[0], self.attack[-1][0] * 25\
                                      + 10, self.attack[-1][1] * 25 + 10, 25,\
                                      25, media.white)
            else:
                media.add_rect_filled(self.boards[0], self.attack[-1][0] * 25\
                                      + 10, self.attack[-1][1] * 25 + 10, 25,\
                                      25, media.red)

        media.show(self.boards[0])
        media.show(self.boards[1])
