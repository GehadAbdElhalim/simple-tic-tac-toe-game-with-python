import random

def create(matrix):
    i = 0
    
    while i < 3 :
        print(3*(" ---"))
        print("|",end = '')
        if matrix[i][0] == 1 :
            print(" X ",end = '')
        elif matrix[i][0] == 2 :
            print(" O ",end = '')
        else :
            print("   ",end = '')
        print("|",end = '')
        
        if matrix[i][1] == 1 :
            print(" X ",end = '')
        elif matrix[i][1] == 2 :
            print(" O ",end = '')
        else :
            print("   ",end = '')
        print("|",end = '')
        
        if matrix[i][2] == 1 :
            print(" X ",end = '')
        elif matrix[i][2] == 2 :
            print(" O ",end = '')
        else :
            print("   ",end = '')
        print("|")
        i += 1
    
    print(3*(" ---"))
    
    return

def place(board,player,position):
    integer_position = position.strip().split(',')
    i = 0
    j = 0
    while i < 3 :
        if int(integer_position[0])-1 == i :
            while j < 3 :           
                if int(integer_position[1])-1 == j :
                    if board[i][j] == 0 :
                        board[i][j] = player
                        return True
                j += 1
        i += 1 
    
    print("you can't put your piece here")
    return False

def winner(matrix) :
    player1 = 1
    player2 = 2
    
    ''' checking the diagonals '''
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == player1 :
        return True
    elif matrix[0][0] == matrix[1][1] == matrix[2][2] == player2 :
        return True
    elif matrix[0][2] == matrix[1][1] == matrix[2][0] == player1 :
        return True
    elif matrix[0][2] == matrix[1][1] == matrix[2][0] == player2 :
        return True
    
    ''' checking the horizontal '''
    i = 0 
    while i < 3 :
        if (matrix[i][0] == matrix[i][1] == matrix[i][2] == player1):
            return True
        elif (matrix[i][0] == matrix[i][1] == matrix[i][2] == player2) :
            return True
        i += 1
    ''' checking the vertical '''
    j = 0
    while j < 3 :
        if (matrix[0][j] == matrix[1][j] == matrix[2][j] == player1) :
            return True
        elif (matrix[0][j] == matrix[1][j] == matrix[2][j] == player2) :
            return True
        j += 1
        
    return False

def isFull(board):
    for x in range(3) :
        for y in range(3) :
            if board[x][y] == 0 :
                return False
    return True

def play(name1, name2):
    
    player1 = 1
    player2 = 2
    
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    while True :
        create(board)
        if isFull(board) == False :
            p1 = input(name1 + " :")
            while place(board,player1,p1) == False :
                p1 = input(name1 + " :")
            
            if winner(board) == False :
                create(board)
                if isFull(board) == False :
                    p2 = input(name2 + " :")
                    while place(board, player2, p2) == False :
                        p2 = input(name2 + " :")
                    
                    if winner(board) == True :
                        create(board)
                        return 2
                else :
                    return 0
            else :
                create(board)
                return 1
        else :
            return 0

def machine(board):
    ''' winning diagonal'''
    if board[0][0] == board[1][1] == 2 :
        if board[2][2] == 0 :
            board[2][2] = 2
            return
    if board[0][2] == board[1][1] == 2 :
        if board[2][0] == 0 :
            board[2][0] = 2
            return
    if board[2][0] == board[1][1] == 2 :
        if board[0][2] == 0 :
            board[0][2] = 2
            return
    if board[2][2] == board[1][1] == 2 :
        if board[0][0] == 0 :
            board[0][0] = 2
            return
    ''' winning smart diagonal '''
    if board[0][0] == board[2][2] == 2 or (board[0][2] == board[2][0] == 2) :
        if board[1][1] == 0 :
            board[1][1] = 2
            return
    
    ''' winning horizontal'''
    for i in range(3) :
        for j in range(2) :
            if board[i][j] == board[i][j+1] == 2 :
                if j == 0 : 
                    if board[i][2] == 0 :
                        board[i][2] = 2
                        return
                elif j == 1 :
                    if board[i][0] == 0 : 
                        board[i][0] = 2
                        return
    ''' winning vertical '''
    for c in range(3) :
        for r in range(2) :
            if board[r][c] == board[r+1][c] == 2 :
                if r == 0 : 
                    if board[2][c] == 0 :
                        board[2][c] = 2
                        return
                elif r == 1 :
                    if board[0][c] == 0 : 
                        board[0][c] = 2
                        return
    ''' winning smart horizontal '''
    for m in range(3) :
        if board[m][0] == board[m][2] == 2 :
            if board[m][1] == 0 :
                board[m][1] = 2
                return
    ''' winning smart vertical '''
    for n in range(3) :
        if board[0][n] == board[2][n] == 2 :
            if board[1][n] == 0 :
                board[1][n] = 2
                return
            
    ''' defensive '''
                    
    ''' dangerzone diagonal'''
    if board[0][0] == board[1][1] == 1 :
        if board[2][2] == 0 :
            board[2][2] = 2
            return
    if board[0][2] == board[1][1] == 1 :
        if board[2][0] == 0 :
            board[2][0] = 2
            return
    if board[2][0] == board[1][1] == 1 :
        if board[0][2] == 0 :
            board[0][2] = 2
            return
    if board[2][2] == board[1][1] == 1 :
        if board[0][0] == 0 :
            board[0][0] = 2
            return
    ''' smart diagonal '''
    if board[0][0] == board[2][2] == 1 or (board[0][2] == board[2][0] == 1) :
        if board[1][1] == 0 :
            board[1][1] = 2
            return
    
    ''' dangerzone horizontal'''
    for i in range(3) :
        for j in range(2) :
            if board[i][j] == board[i][j+1] == 1 :
                if j == 0 : 
                    if board[i][2] == 0 :
                        board[i][2] = 2
                        return
                elif j == 1 :
                    if board[i][0] == 0 : 
                        board[i][0] = 2
                        return
    ''' dangerzone vertical '''
    for c in range(3) :
        for r in range(2) :
            if board[r][c] == board[r+1][c] == 1 :
                if r == 0 : 
                    if board[2][c] == 0 :
                        board[2][c] = 2
                        return
                elif r == 1 :
                    if board[0][c] == 0 : 
                        board[0][c] = 2
                        return
    ''' smart horizontal '''
    for m in range(3) :
        if board[m][0] == board[m][2] == 1 :
            if board[m][1] == 0 :
                board[m][1] = 2
                return
    ''' smart vertical '''
    for n in range(3) :
        if board[0][n] == board[2][n] == 1 :
            if board[1][n] == 0 :
                board[1][n] = 2
                return
    ''' out of the dangerzone and no wining capability'''
    while True :
        row = random.randint(0,2)
        col = random.randint(0,2)
        if board[row][col] == 0 :
            board[row][col] = 2
            return

def playAI(name):
    player1 = 1
    
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    while True :
        create(board)
        if isFull(board) == False :
            p1 = input(name + " :")
            while place(board,player1,p1) == False :
                p1 = input(name + " :")
            
            if winner(board) == False :
                create(board)
                if isFull(board) == False :
                    print("AI plays ...")
                    machine(board)
                    
                    if winner(board) == True :
                        create(board)
                        return 2
                else :
                    return 0
            else :
                create(board)
                return 1
        else :
            return 0

    
    
if __name__ == "__main__" :
    print("This is an XO game for 2 player")
    print("each player should make his move by stating the position")
    print("of each piece he/she wants to play , example : 1,1")
    print("the first 1 means the first row and the second 1 means the first column")
    print("OK ?? ")
    print("let's Start")
    
    choice = int(input("choose 1 to play against the computer and 2 to play against a player : "))
    if choice == 1 :
        name = input("what is your name ? ")
        
        c1 = 0
        c2 = 0
        
        while True :
            AIRound = playAI(name)
            if AIRound == 1 :
                print(name + " wins ")
                c1 += 1
            elif AIRound == 2 :
                print("AI wins ")
                c2 += 1
            else :
                print("Draw")
            
            print("\n\n\n" +name + " : " + str(c1) + "  " + "AI" + " : " + str(c2) + "\n\n\n")
        
            answer = input("Game ended , wanna go again ? (yes/no)")
        
            if answer == "no" :
                print("Thank you for trying the game , Bye !!!")
                break

        
    else :
        print("Btw , player 1 is X and player 2 is O")
        
        name1 = input("Player 1 , pleasse enter your name :")
        name2 = input("Player 2 , pleasse enter your name :")
        
        counter1 = 0
        counter2 = 0
        
        while True :
            a_round = play(name1,name2)
            if a_round == 1 :
                print(name1 + " wins ")
                counter1 += 1
            elif a_round == 2 :
                print(name2 + " wins ")
                counter2 += 1
            else :
                print("Draw")
                
            print("\n\n\n" +name1 + " : " + str(counter1) + "  " + name2 + " : " + str(counter2) + "\n\n\n")
            
            answer = input("Game ended , wanna go again ? (yes/no)")
            
            if answer == "no" :
                print("Thank you for trying the game , Bye !!!")
                break
                   
    
