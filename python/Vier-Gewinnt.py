def check_winner_version2():

    row = len(spielfeld)
    column = len(spielfeld[1])
   

    for ro in range(1, row+1):
        for col in range(column):
            if col >= 3 and ro <= 3:
                if all(spielfeld.get(ro+i)[col-i] == 1 for i in range(4)):
                    return 1
                elif all(spielfeld.get(ro+i)[col-i] == 2 for i in range(4)):
                    return 2
    


    for ro in range(1, row+1):
        for col in range(0, column):
            if col <= 3 and ro <= 3:
                if all(spielfeld.get(ro+i)[col+i] == 1 for i in range(4)):
                    return 1
                elif all(spielfeld.get(ro+i)[col+i] == 2 for i in range(4)):
                    return 2

    
    for ro in range(1, row+1):
        for col in range(column):
            if col <= 4:
                if all(spielfeld.get(ro)[col+i] == 1 for i in range(4)):
                    return 1
                elif all(spielfeld.get(ro)[col+i] == 2 for i in range(4)):
                    return 2
    
    for ro in range(1, row+1):
        for col in range(column):
            if ro <= 3:
                if all(spielfeld.get(ro+i)[col] == 1 for i in range(4)):
                    return 1
                elif all(spielfeld.get(ro+i)[col] == 2 for i in range(4)):
                    return 2



    return 0
                




spielfeld = {
   1: [0,0,0,0,0,0,0],
   2: [0,0,0,0,0,0,0],
   3: [0,0,0,0,0,0,0],
   4: [0,0,0,0,0,0,0],
   5: [0,0,0,0,0,0,0],
   6: [0,0,0,0,0,0,0]
}


# print(spielfeld)

# spielfeld.get(1)[1] = 1

# print(spielfeld.get(1))
i = 0
while True:
    for a in range(0, len(spielfeld)):
        print(spielfeld[a+1])
    


    x = check_winner_version2()
    if x == 0:
        pass
    elif x == 2:
        print('player 2 won')
        break
    elif x == 1:
        print('player 1 won')
        break
    

    
    column_player1 = (input("player 1 which column? 1-7: "))
   
    if column_player1== 'quit':
        break
    elif column_player1.isnumeric() is True:
        column_player1 = int(column_player1)-1

        if column_player1 >= 8:
            print('number is too high')
            break
        if column_player1 < 0:
            print('number is too low')
            break
        else:
            pass
    else:
        print("Please type a valid column")
        break
    
    for row in range(len(spielfeld), 0, -1):
        if spielfeld.get(row)[column_player1] == 0:
            spielfeld.get(row)[column_player1] = 1
            break



    for a in range(0, len(spielfeld)):
        print(spielfeld[a+1])





    x = check_winner_version2()
    if x == 0:
        pass
    elif x == 2:
        print('player 2 won')
        break
    elif x == 1:
        print('player 1 won')
        break






    
    column_player2 = (input("player 2 which column? 1-7: "))
    if column_player2 == 'quit':
        break
    elif column_player2.isnumeric() is True:
        column_player2 = int(column_player2)-1
        if column_player2 >= 7:
            print('number is too high')
            break
        if column_player2 < 0:
            break
    else:
        print("Please type a valid column")
        break
    

    
    for row_ in range(len(spielfeld), 0, -1):
        if spielfeld.get(row_)[column_player2] == 0:
            spielfeld.get(row_)[column_player2] = 2
            break