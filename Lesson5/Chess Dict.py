def isValidChess(**board):
    members = ['king', 'queen', 'pawn', 'bishop', 'rook', 'knight']
    white, black = 0, 0
    pawn, king, bishop, rook, knight, queen = 0, 0, 0, 0, 0, 0
    position2 = '12345678'
    position1 = 'abcdefgh'

    for spot, piece in board.items():
        if spot[0] not in position1 or spot[1] not in position2:
            return False
        if piece[1:] not in members:
            return False

        if piece.startswith('w'):
            white += 1
        elif piece.startswith('b'):
            black += 1

        if piece.endswith('pawn'):
            pawn += 1
        elif piece.endswith('king'):
            king += 1
        elif piece.endswith('bishop'):
            bishop += 1
        elif piece.endswith('rook'):
            rook += 1
        elif piece.endswith('knight'):
            knight += 1
        elif piece.endswith('queen'):
            queen += 1

    if white > 16 or black > 16 or pawn > 16:
        return False
    if king != 2:
        return False
    if bishop > 2 or rook > 2 or knight > 2 or queen > 2:
        return False

    return True

board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChess(**board))
