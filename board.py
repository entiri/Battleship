import random


class Board(object):
    ''' Create a theoretical board based on the coordinates.
    '''

    def __init__(self, length, width, a, b, c, d, game):
        '''
        '''

        self.num_battleships = a
        self.num_cruisers = b
        self.num_frigates = c
        self.num_minesweepers = d
        self.length = length
        self.width = width
        self.game = game

        def draw_board(self):
            '''(self) -> list
            Draw player board and opponent board and return the values
            in a list.
            '''

            # Each space will be 25 pixels long,
            # with a 10 pixel border on top
            board_l = self.l * 25 + 10
            # Each space will be 25 pixels wide,
            # with a 10 pixel border on the side
            board_w = self.w * 25 + 10

            # list holding boards
            list_boards = []
            # Draw player's board
            board_player = media.create_picture(board_w, board_l, media.navy)
            # Draw opponent's board
            board_opponent = media.create_picture(board_w, board_l, media.gray)

            list_boards.append(board_player)    # Add player board to list
            list_boards.append(board_opponent)  # Add opponent board to list

            # Loop through list of boards to add borders
            for item in list_boards:
                # Draw bar along top
                media.add_rect_filled(item, 0, 0, 10, board_l, media.white)
                media.add_rect_filled(item, 0, 0, board_w, 10, media.white)
                counter = 0  # Counter for while loop to draw numbers to board
                # While loop to draw x coordinates on board
                while counter < self.w:
                    temp = str(counter)
                    media.add_text(item, ((counter + 1) * \
                                          25 + 10), 2, temp, media.black)
                    counter += 1
                counter = 0
                #while loop to draw y coordinates on board
                while counter < self.l:
                    temp = str(counter)
                    media.add_text(item, 2, (counter + 1) * \
                                   25 + 10, temp, media.black)
                    counter += 1

            #Loop through list of player ships to place them on board
            for item in self.coordinates:
                media.add_rect_filled(list_boards[0], item[0] * 25 + 10, \
                                      item[1] * 25 + 10, 25, 25, media.gray)

            return list_boards

    def update_boards(self, x, y):
        ''' (self, int, int) -> NoneType
        As coordinates for the board are input, update the board to show if the
        attack was a hit by showing red, or a miss by showing white.
        '''
        coordinates = (x, y)   # Tuple holding coordinates of attack

        # If attack coordinates correspond to a point at which a ship is
        # occupying on the opponent board, draw a red square.
        # If it doesn't, draw a white square
        if coordinates not in self.opp_list:
            media.add_rect_filled(self.boards[1], x * 25 + 10, \
                                  y * 25 + 10, 25, 25, media.white)
        else:
            media.add_rect_filled(self.boards[1], x * 25 + 10, \
                                  y * 25 + 10, 25, 25, media.red)

        # Draw player's board using opponent's last move.
        # A white block is drawn if they missed, a red block if they hit.
        if self.attack != []:
            if self.attack[-1] not in self.coordinates:
                media.add_rect_filled(self.boards[0], self.attack[-1][0] * \
                                      25 + 10, self.attack[-1][1] * 25 + 10, \
                                      25, 25, media.white)
            else:
                media.add_rect_filled(self.boards[0], self.attack[-1][0] * \
                                      25 + 10, self.attack[-1][1] * 25 + 10, \
                                      25, 25, media.red)

        media.show(self.boards[0])
        media.show(self.boards[1])

    def player_vs_computer(self, Player, ComputerPlayer, L, M):
        '''(self, class, class, list, list) -> NoneType
        The general sequence of the game, given the occurence that the game is
        player against computer.
        '''
        # note: Player.opp_coord_copy(ComputerPlayer.coordinates)
        while (L != []) and (M != []):

            Player.attack_place()
            # Attack a random area on the player's board
            ComputerPlayer.random_hit()

            Player.opp_coord_copy(ComputerPlayer.coordinates)
            Player.opp_attack_copy(ComputerPlayer.hitlist)
            # Update the list with the computer's latest random attack

    def player_vs_player(self, A, B, L, M):
        '''(self, class, class, list, list) -> NoneType
        Run through the sequence of the game if the game is player vs player
        '''
        # Note: Player.opp_coord_copy(ComputerPlayer.coordinates)
        while (L != []) and (M != []):

            A.attack_place()  # Attack a location on Player 1's board
            B.attack_place()  # Attack a location on Player 2's board

            B.opp_attack_copy(A.hitlist)
            B.opp_coord_copy(A.hitlist)

            A.opp_attack_copy(B.hitlist)
            A.opp_coord_copy(B.hitlist)
