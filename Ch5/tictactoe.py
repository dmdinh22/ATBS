# dictionary to store board data
the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# function to print out tictactoe board
def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# set first player to X marker
turn = 'X'
# iterate over the 9 properties of dictionary
for i in range(9):
    # print out the board
    print_board(the_board)
    # print out text 
    print('Turn for ' + turn + '. Move on which space?')
    # record the move from the player
    move = input()
    # set the dictionary value of the move to chosen turn
    the_board[move] = turn
    # change to other marker
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    # reprint board with new board data including markers
    print_board(the_board)
