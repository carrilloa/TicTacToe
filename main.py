# Tic Tac Toe
# Anna Carrillo
# Started: Thurs Sep 1 2022

import random
import time
import sys

sys.setrecursionlimit(1500)

def main():
    game()


def game():
    board_position = board()
    rules()
    letter = choose_letter()
    comp_letter = ""
    game_won = False

    if letter == "X":
        comp_letter = "O"
    elif letter == "O":
        comp_letter = "X"
    else:
        print("ERROR!")
        exit()

    print(f"Ok, you are playing as {letter}. The computer will be {comp_letter}. ")
    # time.sleep(4)
    print("Now, lets see who starts. ")
    # time.sleep(1)
    for i in range(3):
        print(".", end="")
        # time.sleep(2)
    # time.sleep(1)

    a = random_starting()
    your_turn = False

    if a == 0:
        print("Player starts! ")
        player_turn(letter, board_position, comp_letter)
        your_turn = False
    else:
        print("Computer starts! ")
        computer_turn(board_position, comp_letter, letter)
        your_turn = True
    cat = False
    who_won = ""
    while not game_won:
        if your_turn:
            player_turn(letter, board_position, comp_letter)
            if check_for_win(board_position, letter, comp_letter):
                who_won = "You"
                game_won = True
            if check_for_cat(board_position):
                cat = True
                game_won = True
            else:
                your_turn = not your_turn
        else:
            computer_turn(board_position, comp_letter, letter)
            if check_for_win(board_position, letter, comp_letter):
                who_won = "The computer"
                game_won = True
            if check_for_cat(board_position):
                cat = True
                game_won = True
            your_turn = not your_turn
    if cat:
        print("It was a tie! ")
    else:
        print(f"{who_won} won!")


def board():
    board_set_up = [["e", "e", "e"],
                    ["e", "e", "e"],
                    ["e", "e", "e"]]
    return board_set_up


def rules():
    print("Welcome to Tic Tac Toe! ")
    # time.sleep(1)
    print("The board is set up as follows: ")
    # time.sleep(1)
    print('''["e", "e", "e",]''')
    print('''["e", "e", "e",]''')
    print('''["e", "e", "e",]''')
    print("")
    # time.sleep(3)
    print("Each column, from left to right, has a letter. Respectively, they are 'A', 'B', and 'C'")
    # time.sleep(3)
    print("Each row has a number: '1', '2', and '3'")
    # time.sleep(3)
    print("To play a turn, please type the letter followed by the number where you want to place your mark.")
    # time.sleep(4)
    print("")
    print("The start will be determined randomly to see if you go first or second. ")
    # time.sleep(4)
    print("")


def choose_letter():
    answer = input("Would you like to play as X or O? ")
    x_list = []
    o_list = []
    if answer in x_list:
        answer = "X"
    elif answer in o_list:
        answer = "O"
    return answer

def is_empty(board, x, y):
    if board[x][y] == "e":
        return True
    else:
        return False

def random_starting():
    return random.randint(0, 1)


def player_turn(starting_letter, board_position, computer_letter):
    turn = input(f"Where would you like to place your {starting_letter}? ")
    rules_list = ["rules", "rule", "Rules", "Rule", "Help", "help"]
    if turn in rules_list:
        return rules
    if turn == "A1":
        if board_position[0][0] == "e":
            board_position[0][0] = starting_letter
        elif board_position[0][0] == computer_letter:
            print("Try again. That spot is taken. ")
            player_turn(starting_letter, board_position, computer_letter)
        else:
            print("Something went wrong. Try again. ")
            player_turn(starting_letter, board_position, computer_letter)
    if turn == "A2":
        if board_position[1][0] == "e":
            board_position[1][0] = starting_letter
        elif board_position[1][0] == computer_letter:
            print("Try again. That spot is taken. ")
            player_turn(starting_letter, board_position, computer_letter)
        else:
            print("Something went wrong. Try again. ")
            player_turn(starting_letter, board_position, computer_letter)
    if turn == "A3":
        if board_position[2][0] == "e":
            board_position[2][0] = starting_letter
        elif board_position[2][0] == computer_letter:
            print("Try again. That spot is taken. ")
            player_turn(starting_letter, board_position, computer_letter)
        else:
            print("Something went wrong. Try again. ")
            player_turn(starting_letter, board_position, computer_letter)
    if turn == "B1":
        if board_position[0][1] == "e":
            board_position[0][1] = starting_letter
        elif board_position[0][1] == computer_letter:
            print("Try again. That spot is taken. ")
            player_turn(starting_letter, board_position, computer_letter)
        else:
            print("Something went wrong. Try again. ")
            player_turn(starting_letter, board_position, computer_letter)
    if turn == "B2":
        if board_position[1][1] == "e":
            board_position[1][1] = starting_letter
        elif board_position[1][1] == computer_letter:
            print("Try again. That spot is taken. ")
            player_turn(starting_letter, board_position, computer_letter)
        else:
            print("Something went wrong. Try again. ")
            player_turn(starting_letter, board_position, computer_letter)
    if turn == "B3":
        if board_position[2][1] == "e":
            board_position[2][1] = starting_letter
        elif board_position[2][1] == computer_letter:
            print("Try again. That spot is taken. ")
            player_turn(starting_letter, board_position, computer_letter)
        else:
            print("Something went wrong. Try again. ")
            player_turn(starting_letter, board_position, computer_letter)
    if turn == "C1":
        if board_position[0][2] == "e":
            board_position[0][2] = starting_letter
        elif board_position[0][2] == computer_letter:
            print("Try again. That spot is taken. ")
            player_turn(starting_letter, board_position, computer_letter)
        else:
            print("Something went wrong. Try again. ")
            player_turn(starting_letter, board_position, computer_letter)
    if turn == "C2":
        if board_position[1][2] == "e":
            board_position[1][2] = starting_letter
        elif board_position[1][2] == computer_letter:
            print("Try again. That spot is taken. ")
            player_turn(starting_letter, board_position, computer_letter)
        else:
            print("Something went wrong. Try again. ")
            player_turn(starting_letter, board_position, computer_letter)
    if turn == "C3":
        if board_position[2][2] == "e":
            board_position[2][2] = starting_letter
        elif board_position[2][2] == computer_letter:
            print("Try again. That spot is taken. ")
            player_turn(starting_letter, board_position, computer_letter)
        else:
            print("Something went wrong. Try again. ")
            player_turn(starting_letter, board_position, computer_letter)
    print(board_position[0])
    print(board_position[1])
    print(board_position[2])
    print("")
    

def computer_turn(board_position, computer_letter, player_letter):
    print("")
    print("Computer's turn!")
    time.sleep(1)
    for i in range(3):
        print(".", end="")
        time.sleep(1)
    print("")

    score = minimax(board_position, 0, True, computer_letter, player_letter)
    if board_position[0][0] == "e":
        board_position[0][0] = f"{computer_letter}"
        print(board_position[0])
        print(board_position[1])
        print(board_position[2])
        print("")
        return
    else:
        pass
    if board_position[0][1] == "e":
        board_position[0][1] = f"{computer_letter}"
        print(board_position[0])
        print(board_position[1])
        print(board_position[2])
        print("")
        return
    else:
        pass
    if board_position[0][2] == "e":
        board_position[0][2] = f"{computer_letter}"
        print(board_position[0])
        print(board_position[1])
        print(board_position[2])
        print("")
        return
    else:
        pass
    if board_position[1][0] == "e":
        board_position[1][0] = f"{computer_letter}"
        print(board_position[0])
        print(board_position[1])
        print(board_position[2])
        print("")
        return
    else:
        pass
    if board_position[1][1] == "e":
        board_position[1][1] = f"{computer_letter}"
        print(board_position[0])
        print(board_position[1])
        print(board_position[2])
        print("")
        return
    else:
        pass
    if board_position[1][2] == "e":
        board_position[1][2] = f"{computer_letter}"
        print(board_position[0])
        print(board_position[1])
        print(board_position[2])
        print("")
        return
    else:
        pass
    if board_position[2][0] == "e":
        board_position[2][0] = f"{computer_letter}"
        print(board_position[0])
        print(board_position[1])
        print(board_position[2])
        print("")
        return
    else:
        pass
    if board_position[2][1] == "e":
        board_position[2][1] = f"{computer_letter}"
        print(board_position[0])
        print(board_position[1])
        print(board_position[2])
        print("")
        return
    else:
        pass
    if board_position[2][2] == "e":
        board_position[2][2] = f"{computer_letter}"
        print(board_position[0])
        print(board_position[1])
        print(board_position[2])
        print("")
        return
    else:
        pass
    print(board_position[0])
    print(board_position[1])
    print(board_position[2])
    print("")

    # best_score = -1000
    # best_move = 0

    # for i in board_position:
    #     for j in i:
    #         if board_position[board_position.index(i)][i.index(j)] == "e":
    #             board_position[board_position.index(i)][i.index(j)] == computer_letter
    #             score = minimax(board_position, 0, False, computer_letter, player_letter)
    #             board_position[board_position.index(i)][i.index(j)] == "e"
    #             if score > best_score:
    #                 best_score = score
    #                 best_move = [i, j]

    # board_position[best_move.index(0)][best_move.index(1)] = computer_letter
    # return

def minimax(board_position, depth, isMaximizing, cl, pl):
    depth = 0
    print(check_for_win(board_position, pl, cl))
    print(check_for_cat(board_position))
    if check_for_win(board_position, pl, cl) == 1:
        return -100
    elif check_for_win(board_position, pl, cl) == 2:
        return 100
    elif check_for_cat(board_position):
        return 0
    
    # if isMaximizing:
    #     best_score = -1000
    #     for i in board_position:
    #         for j in i:
    #             if board_position[board_position.index(i)][i.index(j)] == "e":
    #                 board_position[board_position.index(i)][i.index(j)] == cl
    #                 score = minimax(board_position, 0, False, cl, pl)
    #                 board_position[board_position.index(i)][i.index(j)] == "e"
    #                 if score > best_score:
    #                     best_score = score
    #     return best_score
    # else: 
    #     best_score = 800
    #     for i in board_position:
    #         for j in i:
    #             if board_position[board_position.index(i)][i.index(j)] == "e":
    #                 board_position[board_position.index(i)][i.index(j)] == pl
    #                 score = minimax(board_position, 0, True, cl, pl)
    #                 board_position[board_position.index(i)][i.index(j)] == "e"
    #                 if score < best_score:
    #                     best_score = score
    #     return best_score



def check_for_win(board_position, starting_letter, computer_letter):
    player_win = 1
    comp_win = 2
    b = board_position
    s = starting_letter
    c = computer_letter
    if b[0][0] == s and b[1][0] == s and b[2][0] == s:
        return player_win
    if b[0][0] == c and b[1][0] == c and b[2][0] == c:
        return comp_win
    if b[0][1] == s and b[1][1] == s and b[2][1] == s:
        return player_win
    if b[0][1] == c and b[1][1] == c and b[2][1] == c:
        return comp_win
    if b[0][2] == s and b[1][2] == s and b[2][2] == s:
        return player_win
    if b[0][2] == c and b[1][2] == c and b[2][2] == c:
        return comp_win
    if b[0][0] == s and b[0][1] == s and b[0][2] == s:
        return player_win
    if b[0][0] == c and b[0][1] == c and b[0][2] == c:
        return comp_win
    if b[1][0] == s and b[1][1] == s and b[1][2] == s:
        return player_win
    if b[1][0] == c and b[1][1] == c and b[1][2] == c:
        return comp_win
    if b[2][0] == s and b[2][1] == s and b[2][2] == s:
        return player_win
    if b[2][0] == c and b[2][1] == c and b[2][2] == c:
        return comp_win
    if b[0][0] == s and b[1][1] == s and b[2][2] == s:
        return player_win
    if b[0][0] == c and b[1][1] == c and b[2][2] == c:
        return comp_win
    if b[0][2] == s and b[1][1] == s and b[2][0] == s:
        return player_win
    if b[0][2] == c and b[1][1] == c and b[2][0] == c:
        return comp_win
    else:
        return False


def check_for_cat(board_position):
    for i in board_position:
        if "e" in i:
            return False
        else:
            pass
    return True


def player_won():
    print("You won! ")


def computer_won():
    print("You lost! ")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()




