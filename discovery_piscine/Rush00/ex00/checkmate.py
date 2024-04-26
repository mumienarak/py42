def incheck(board):
    rows = board.strip().split('\n')
    size_i = len(rows)
    rows = [[char for char in string] for string in rows]
    King_position,enemy = [],[]
    checK ="F"
    # Find King position and enemy
    try:
        for i in range(size_i):
            size_j = len(rows[i])
            if size_j != size_i:
                raise IndexError
            for j in range(size_i):
                if rows[i][j] == 'K':
                    King_position.append((i,j))
                elif rows[i][j] != '.' and rows[i][j] != 'K':
                    enemy.append((i, j, rows[i][j]))
        if len(King_position) == 0:
            raise ValueError
        elif len(King_position) != 1:
            raise ValueError
        #scans "inchecK" for each enemy
        for piece in enemy:
            if piece[2] == 'P':
                if piece[0] == King_position[0][0] + 1 and abs(piece[1] - King_position[0][1]) == 1:
                    print("Success")
                    checK = "T"
            # x-posi of P is on the right or left side of K and Y-posi of P is on the bacK of King then "scess"
            elif piece[2] == 'B' or piece[2] == 'Q':
                if abs(piece[0] - King_position[0][0]) == abs(piece[1] - King_position[0][1]):
                    print("Success")
                    checK = "T"
            elif piece[2] == 'R' or piece[2] == 'Q':
                if piece[0] == King_position[0][0] or piece[1] == King_position[0][1]:#K is on the same row or column of Rk,Qn
                    print("Success")
                    checK = "T"
            else:
                raise NameError
        if checK == "F":
                print("Fail")
    except:
        print("Error Na Kub Bro XD")