computer = "X"; human = "O"
scan = [[0,1,2],[3,4,5],[6,7,8], \
[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

# 0 1 2
# 3 4 5
# 6 7 8
priority = [4, 0,2,8,6,  1,5,7,3]

def clrArray():
    a = []    
    for i in range(9):
        a.append(0)
    return a

def print_board():
    def mark(i):
        if board[i] == 0:
            return str(i + 1)
        return board[i]

    for i in range(0,len(board),3):
        print("  " + mark(i)+mark(i+1)+mark(i+2))

# possible values of best
best_draw = -3; best_done = -2; best_common = -1

def scan_board():
    global hcnt, ccnt, best, common1, common0
    common1 = clrArray(); common0 = clrArray()
    best = best_draw
    for i in range(len(scan)):
        empty = []; hcnt = 0; ccnt = 0 
        for j in scan[i]:
            if board[j] == human:
                hcnt += 1
            elif board [j] == computer:
                ccnt += 1
            else:
                empty.append(j)
        if hcnt == 3 or ccnt == 3: best = best_done; return
        if len(empty) == 1 and (hcnt == 2 or ccnt == 2):
            best = empty[0]; return
        if len(empty) == 2 and ccnt == 1:
            best = best_common
            common1 [empty[0]] += 1; common1 [empty[1]] += 1
        elif len(empty)==3 or len(empty) == 2 and ccnt == 1:
            best = best_common;
            common0 [empty[0]] += 1; common0 [empty[1]] += 1
            if len(empty) == 3: common0 [empty[2]] += 1

def find_max(a):
    m = -1; j = -1
    for i in priority:
        if a [i] > m: m = a[i]; j = i
    return j

def choose_move(human_turn):
    global best,common1,common0
    scan_board()
    if hcnt == 3:
        print("You win!")
    elif ccnt == 3:
        print("I win!")
    elif best == best_draw:
        print("It's a draw...")
    elif human_turn:
        return True
    elif best == best_common:
        best = find_max(common1)
        if common1[best] == 0:
            best = find_max(common0)
            if common0[best] == 0:
                print("Error: No common0 found")
                return False
        return best >= 0
    else:
        return best >= 0
    return False

def play_game():
    global msg, first_move
    mv = input(msg + " ")
    if mv == "q" or mv == "Q":
        print("Game Aborted")
        return False
    if mv == "" and first_move:
        if choose_move(False):
            board[best] = computer
            print("------------")
            print_board()
            return True        
    try:
        mi = int(mv) - 1
    except:
        msg = "Input not a number. Try again:"
        return True
    if 0 > mi or mi > 8:
        msg = "Input out of bounds. Try again:"
        return True
    if board[mi] != 0:
        msg = "Requested square occupied. Try again:"
        return True
    board[mi] = human
    msg = "Your square?"
    print_board()
    if choose_move(False):
        board[best] = computer
        print("------------")
        print_board()
        return choose_move(True)
    return False


board = clrArray()
msg = "Your square?"
first_move = True
again = True
print("Hit enter to let computer move first")
print("Enter Q to quit game")
print("Enter 1 through 9 to play a square")
print("Computer is " + computer + "  you are " + human)
print_board()
while again:
    again = play_game()
    first_move = False