import media
import random
import sys
from board import Board
from playerclass import Player
from computerclass import ComputerPlayer


def playerorcomputer():
    ''' (None) -> str
    Start the game by asking whether the player wants to play against a
    computer or against another player. If the game is against a computer,
    return 'c'. If the game is player vs. player, return 'c'
    '''
    a = raw_input('Enter C if you want to play against a computer, or P if ' +\
                  'you want to play against a friend.: '
                  ).replace('\r', '')
    if (a == 'p') or (a == 'P'):
        return 'p'
    elif a == 'c' or a == 'C':
        return 'c'
    else:
        print 'Try again.'
        return playerorcomputer()

def inputlength():
    '''Ask for a given integer value for the length of the board. If the value
    is not an integer, have the user try again.
    '''
    try:
        a = int(raw_input('Length of board: '))
        return a
    except:   # if the value is not an integer
        return inputlength()


def inputwidth():
    '''Ask for a given integer value for the width of the board. If the value
    is not an integer, have the user try again.
    '''
    try:
        a = int(raw_input('Width of board: '))
        return a
    except:  # if the value is not an integer
        return inputwidth()


def space_occupied(a, b, c, d, l, w):
    '''Ask for a given integer value for the width of the board. If the value
    is not an integer, have the user try again. If the space occupied by the
    pieces is greater than the size of the board, (a * b), then have the user
    try again.
    '''
    pieces = [a, b, c, d]

    # set a variable for the total space occupied by the pieces
    total = (pieces[0] * 5) + (pieces[1] * 4) + (pieces[2] * 3) + \
        (pieces[3] * 2)

    if total > (l * w):   # if the total is greater than the size of the board
        print'The number of ships is greater than the size of the board. ' + \
        'Try again.'
        return space_occupied(a, b, c, d, l, w)
    else:
        return pieces


def num_bs():
    '''
    Return the number of battleships the user would like in the game. If the
    value is not a number, have the user try again.
    '''
    a = raw_input('Enter the number of battleships for the' + \
                  ' game: ').replace('\r', '')

    if try_it(a) == True:
        a = int(a)
        return a
    else:
        return num_bs()


def num_cru():
    '''
    Return the number of cruisers the user would like in the game. If the value
    is not a number, have the user try again.
    '''
    a = raw_input('Enter the number of cruisers for the game: ')\
        .replace('\r', '')

    if try_it(a) == True:
        a = int(a)
        return a
    else:
        return num_cru()


def num_frig():
    '''
    Return the number of cruisers the user would like in the game. If the value
    is not a number, have the user try again.
    '''
    a = raw_input('Enter the number of frigates for the game: ')\
            .replace('\r', '')
    if try_it(a) == True:
        a = int(a)
        return int(a)
    else:
        return num_frig()


def num_mine():
    '''
    Return the number of minesweepers
    '''
    a = raw_input('Enter the number of minesweepers for the' + \
                                  ' game: ').replace('\r', '')

    if try_it(a) == True:
        a = int(a)
        return a
    else:
        print 'Oops. Something went wrong.'
        return num_mine()


def try_it(i):
    '''(str) -> Bool
    Return true if the value can be made into an integer, and False
    otherwise
    '''
    try:
        i = int(i)
        return True
    except:
        return False


if __name__ == '__main__':
    menu_val = 0

    while menu_val != 1:
        print "Battleship"
        print "----------"
        print "1. Start Game \n2. Instructions \n3. Exit Game"
        menu_val = raw_input("Enter the number of your choice: ")
        if (menu_val.isdigit()):
            menu_val = int(menu_val)
        else:
            menu_val = 0

        if menu_val == 2:
            instructions = open('instructions.txt', 'r')
            print "\nInstructions\n------------"
            for line in instructions:
                print line,
            print "\n"
        elif menu_val == 3:
            sys.exit("Thank you for playing.")

    game = playerorcomputer()
    l = inputlength()
    w = inputwidth()
    a = space_occupied(num_bs(), num_cru(), num_frig(), num_mine(), l, w)
    b, c, d, e = a[0], a[1], a[2], a[3]
    name1 = raw_input('Enter the name of player 1: ')
    name2 = raw_input('Enter the name of player 2: ')

    g = Board(l, w, a, b, c, d, game)

    if game == 'c':
        a = Player(l, w, b, c, d, e, name1)
        f = ComputerPlayer(l, w, b, c, d, e, name2)
        a.place_ships()
        a.draw_board()
        f.place_ships()
        a.opp_coord_copy(f.coordinates)
        f.opp_coord_copy(a.coordinates)
        g = Board(l, w, a, b, c, d, game)
        g.player_vs_computer(a, f, a.coordinates, f.coordinates)

    elif game == 'p':
        a = Player(l, w, b, c, d, e, name1)
        f = Player(l, w, b, c, d, e, name2)
        a.place_ships()
        a.draw_board()
        f.place_ships()
        f.draw_board()
        a.opp_coord_copy(f.coordinates)
        f.opp_coord_copy(a.coordinates)
        g = Board(l, w, a, b, c, d, game)
        g.player_vs_player(a, f, a.coordinates, f.coordinates)
