# tiktaktoe

import random


def draw_board(board):

    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def input_player_letter():

    letter = ''
    while not(letter == 'X' or letter == 'O'):
        print('Select X or O:')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def make_move(board, letter, move):

    board[move] = letter


def is_winner(b: object, l: object) -> object:

    return ((b[7] == l and b[8] == l and b[9] == l) or
            (b[4] == l and b[5] == l and b[6] == l) or
            (b[1] == l and b[2] == l and b[3] == l) or
            (b[1] == l and b[4] == l and b[7] == l) or
            (b[2] == l and b[5] == l and b[8] == l) or
            (b[3] == l and b[6] == l and b[9] == l))


def get_board_copy(board):

    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy


def is_space_free(board, move):
    return board[move] == ' '


def get_player_move(board):

    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split(' ') or not is_space_free(board, int(move)):
        move = input('Next move (1-9): ')
    return int(move)


def choose_random_move(board, move_list):

    possible_moves = []
    for i in move_list:
        if is_space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) !=0:
        return random.choice(possible_moves)
    else:
        return None


def get_ai_move(board, ai_letter):

    if ai_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, ai_letter, i)
            if is_winner(board_copy, ai_letter):
                return i

    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, player_letter, i)
            if is_winner(board_copy, player_letter):
                return i

    move = choose_random_move(board, [1, 3, 7, 9])
    if move is not None:
        return move

    if is_space_free(board, 5):
        return 5

    return choose_random_move(board, [2, 4, 6, 8])


def is_board_full(board):

    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


def who_goes_first():

    if random.randint(0, 1) == 0:
        return 'AI'
    else:
        return 'HUMAN'


print('TicTacToe')

while True:
    board = [' '] * 10
    player_letter, ai_letter = input_player_letter()
    turn = who_goes_first()
    print('' + turn + ' goes first')
    game_is_active = True

    while game_is_active:
        if turn == 'HUMAN':
            draw_board(board)
            move = get_player_move(board)
            make_move(board, player_letter, move)
            if is_winner(board, player_letter):
                draw_board(board)
                print('You win!')
                game_is_active = False
            else:
                if is_board_full(board):
                    draw_board(board)
                    print('DRAW')
                    break
                else:
                    turn = 'AI'
        else:
            move = get_ai_move(board, ai_letter)
            make_move(board, ai_letter, move)
            if is_winner(board, ai_letter):
                draw_board(board)
                print('AI win!')
                game_is_active = False
            else:
                if is_board_full(board):
                    draw_board(board)
                    print('DRAW')
                    break
                else:
                    turn = 'HUMAN'

    print('Play again (y/n)?')
    if not input().lower().startswith('y'):
        break
