import sys
import copy

STARTING_PIECES = {'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR', 'a7': 'bP', 'b7': 'bP',
'c7': 'bP', 'd7': 'bP', 'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',
'a1': 'wR', 'b1': 'wN', 'c1': 'wB', 'd1': 'wQ', 'e1': 'wK', 'f1': 'wB',
'g1': 'wN', 'h1': 'wR', 'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP'}

def print_chessboard(board):
    squares = []
    is_white_square = True
    for y in '87654321':
        for x in 'abcdefgh':
            # print(x, y, is_white_square) # DEBUG: Show Coordinates
            if x +y in board.keys():
                squares.append(board[ x + y ])
            else:
                if is_white_square:
                    squares.append(WHITE_SQUARE)
                else:
                    squares.append(BLACK_SQUARE)
            is_white_square = not is_white_square
        is_white_square = not is_white_square
    print(BOARD_TEMPLATE.format(*squares))

BOARD_TEMPLATE = """
    a    b    c    d    e    f    g    h
   ____ ____ ____ ____ ____ ____ ____ ____
  ||||||    ||||||    ||||||    ||||||    |
8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
"""
WHITE_SQUARE = '||'
BLACK_SQUARE = '  '

print('Interactive Chessboard')
print('by Parth Adokar parthadokar@duck.com')
print()
print('Pieces:')
print('  w - White, b - Black')
print('  P - Pawn, N - Knight, B - Bishop, R - Rook, Q - Queen, K - King')
print('Commands:')
print('  move e2 e4 - Moves the piece at e2 to e4')
print('  remove e2 - Removes the piece at e2')
print('  set e2 wP - Sets square e2 to a white pawn')
print('  reset - Resets pieces back to their starting squares')
print('  clear - Clears the entire board')
print('  fill wP - Fills entire board with white pawns.')
print('  quit - Quits the program')
def isValidChessBoard(board):
    # Define kings
    white_king_count = 0
    black_king_count = 0

    # Define pieces and pawns
    white_pieces_count = 0
    black_pieces_count = 0
    white_pawn_count = 0
    black_pawn_count = 0

    valid_squares = []
    for col in 'abcdefgh':
        for row in '12345678':
            # FIX 1: was `row + col` (e.g. '1a'), but chess squares are col+row (e.g. 'a1')
            valid_squares.append(col + row)

    # FIX 2: pieces use shorthand letters, not full names — 'R' not 'rook', 'K' not 'king', etc.
    valid_pieces = ['P', 'N', 'B', 'R', 'Q', 'K']

    for square,piece in board.items():
        if square not in valid_squares:
            return False, f"Invalid square name found: {square}"

        # FIX 3: pieces use 'w'/'b' prefix, not 'white'/'black' — e.g. 'wR', 'bK'
        if piece[0] not in ('w', 'b'):
            return False, f"Invalid player indicator: {piece}"

        player_color = piece[0]
        piece_type = piece[1:]

        if piece_type not in valid_pieces:
            return False,f"Invalid piece found: {piece_type}"

        # FIX 4: player_color is 'w' or 'b' (piece[0]), not "white"/"black"
        #         Also updated piece_type comparisons to match shorthand ('K', 'P')
        if player_color == 'w':
            white_pieces_count += 1
            if piece_type == 'K':
                white_king_count += 1
            elif piece_type == 'P':
                white_pawn_count += 1
        else:
            black_pieces_count += 1
            if piece_type == 'K':
                black_king_count += 1
            elif piece_type == 'P':
                black_pawn_count += 1

    if white_king_count != 1:
        return False, f"White king count is invalid: {white_king_count}"
    if black_king_count != 1:
        return False, f"Black king count is invalid: {black_king_count}"
    
    if white_pieces_count > 16:
        return False, f"White total piece count exceeds 16: {white_pieces_count}"
    if black_pieces_count > 16:
        return False, f"Black total piece count exceeds 16: {black_pieces_count}"

    
    if white_pawn_count > 8:
        return False, f"White pawn count exceeds 8: {white_pawn_count}"
    if black_pawn_count > 8:
        return False, f"Black pawn count exceeds 8: {black_pawn_count}"

    return True, "Board is valid"

board_valid_sample = {'h1': 'wR', 'a1': 'wR', 'e1': 'wK', 'd8': 'bK', 'h7': 'bP', 'a7': 'bP', 'e2': 'wP'}
is_valid, message = isValidChessBoard(board_valid_sample)
print(f"Board 1: {is_valid} - {message}")

def isValidChessBoard_v2(board):
    """
    Checks if the given dictionary represents a valid chessboard state 
    based on basic piece counts, square validity, and naming conventions 
    using shorthand notation (e.g., 'bK' for black king).
    The prompt asked for 'pawn', 'knight', etc. names *after* the color prefix.
    The user input example was 'bK', 'wQ'. This suggests the user actually wants 
    the *function* to accept the standard *shorthand* representation ('K', 'Q', etc).
    Let's stick to the prompt's written instructions: names should be 'pawn', 'king', etc.
    The first function `isValidChessBoard(board)` follows the text instructions perfectly.
    """
    # We will use the first function defined above. The example dictionary in the prompt 
    # uses shorthand (e.g., 'bK') which doesn't follow the prompt's instruction ("followed 
    # by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'"). 
    # Assuming the instructions are primary and the example dictionary needs adjustment:

    prompt_example_adjusted = {'h1': 'bking', 'c6': 'wqueen', 'g2': 'bbishop', 'h5': 'bqueen', 'e3': 'wking'}
    is_valid_p, message_p = isValidChessBoard(prompt_example_adjusted)
    print(f"Prompt Example (Adjusted Names): {is_valid_p} - {message_p}")


# An invalid board (too many kings) — FIX: updated to shorthand notation to match the function
board_invalid_kings = {'a1': 'wK', 'h8': 'bK', 'e1': 'wK'}
is_valid_k, message_k = isValidChessBoard(board_invalid_kings)
print(f"Board Invalid (Kings): {is_valid_k} - {message_k}")

# An invalid board (invalid square) — FIX: updated to shorthand notation to match the function
board_invalid_square = {'9z': 'wK', 'a1': 'bK'}
is_valid_s, message_s = isValidChessBoard(board_invalid_square)
print(f"Board Invalid (Square): {is_valid_s} - {message_s}")
main_board = copy.copy(STARTING_PIECES)
while True:
    print_chessboard(main_board)
    response = input('> ').split()

    if response[0] == 'move':
        main_board[response[2]] = main_board[response[1]]
        del main_board[response[1]]
    elif response[0] == "remove":
        del main_board[response[1]]
    elif response[0] == "set":
        main_board[response[1]] = response[2]
    elif response[0] == 'reset':
        main_board = copy.copy(STARTING_PIECES)
    elif response[0] == 'clear':
        main_board = {}
    elif response[0] == 'fill':
        for y in '87654321':
            for x in 'abcdefgh':
                main_board[x + y] = response[1]
    elif response[0] == 'quit':
        sys.exit()
        
