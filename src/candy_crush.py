def candy_crush(board):
    """
    :type board: List[List[int]]
    :rtype: List[List[int]]
    """

    crushed = True
    while crushed:
        crushed = False
        marked = set()

        # search for horizontally curshed candies
        for i in range(0, len(board)):
            for j in range(0, len(board[i]) - 2):
                if board[i][j] == board[i][j + 1] == board[i][j + 2] and board[i][j] != 0:
                    marked.add((i, j))
                    marked.add((i, j + 1))
                    marked.add((i, j + 2))
                    crushed = True

        # search for vertically crushed candies
        for j in range(0, len(board[0])):
            for i in range(0, len(board) - 2):
                if board[i][j] == board[i + 1][j] == board[i + 2][j] and board[i][j] != 0:
                    marked.add((i, j))
                    marked.add((i + 1, j))
                    marked.add((i + 2, j))
                    crushed = True

        # crush all marked candies
        for i, j in marked:
            board[i][j] = 0

        # make candies fall after crushing
        for j in range(0, len(board[0])):
            fill_ind = None
            for i in range(len(board) - 1, -1, -1):
                if fill_ind is None and board[i][j] == 0:
                    fill_ind = i
                elif fill_ind is not None:
                    board[fill_ind][j] = board[i][j]
                    if board[fill_ind][j] != 0:
                        fill_ind -= 1
            # fill spaces on the top with zeros
            if fill_ind is not None:
                for i in range(fill_ind, -1, -1):
                    board[i][j] = 0

    return board
