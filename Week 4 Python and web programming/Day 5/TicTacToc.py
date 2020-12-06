data = [[1,2,3],[4,5,6],[7,8,9]]
data2 = [1,2,3,4,5,6,7,8,9]


def display_board():
    print("                 tic Tac Toe")
    print("**********************************************")
    print("*                  |        |                *")
    print("*          {}       |   {}    |    {}           *".format(data[0][0],data[0][1],data[0][2]))
    print("*   _______________|________|_______________ *")
    print("*                  |        |                *")
    print("*          {}       |   {}    |    {}           *".format(data[1][0],data[1][1],data[1][2]))
    print("*   ______________ |________|________________*")
    print("*                  |        |                *")
    print("*          {}       |   {}    |    {}           *".format(data[2][0],data[2][1],data[2][2]))

    print("**********************************************")


def player_input(player):
    position = int(input('Player '+player+" enter the position(from 1 to 9): "))
    print(data2)
    while position not in data2:
        position = int(input("Please, enter a new input: "))
    else:
        for i in data:
            try:
                post_index = i.index(position)
                i[post_index] = player
            except ValueError:
                continue
        display_board()
        data2.remove(position)


    #display_board()


# player_input()

def play():
    display_board()
    turn = 0
    player1 = 'X'
    player2 = 'o'
    while turn < 9:
        if turn % 2 == 0:
            player_input(player1)
        else:
            player_input(player2)
        turn += 1

def check_win():
