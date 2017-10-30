TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10), (7,7))
TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

def make_scrabble_board():
    board=[]
    for i in range(15):
        line=[]
        for i in range(15):
            line.append('_')
        board.append(line)

    for r,c in TRIPLE_WORD_SCORE:
        board[r][c] = 'T'

    for r,c in DOUBLE_WORD_SCORE:
        board[r][c] = 'D'

    for r,c in TRIPLE_LETTER_SCORE:
        board[r][c]='t'

    for r,c in DOUBLE_LETTER_SCORE:
        board[r][c] = 'd'
    return board

board = make_scrabble_board()


def print_board(b):
    for line in b:
        print ( ' '.join(line))
        
        
def score(w):
    w = w.upper()
    total = 0
    scoremaster = {
        'AEIOULNRST':1,
        'DG':2,
        'FHVWY':4,
        'K':5,
        'JX':8,
        'QZ':10
        }
    for i in w:
        for v in scoremaster.keys():
            if i in v:
                total += scoremaster[v]
    return total


def add_word_across(board,word,r,c):
    T = 0
    D = 0
    occupied = []
    total = 0
    for i in range(len(word)):
        occupied.append((r,c+i)) 
    for i in range(len(occupied)):
        if occupied[i] in TRIPLE_WORD_SCORE:
            T += 1
            total += score(word[i])
        elif occupied[i] in DOUBLE_WORD_SCORE:
            D += 1 
            total += score(word[i])
        elif occupied[i] in TRIPLE_LETTER_SCORE:
            total += score(word[i])*3
        elif occupied[i] in DOUBLE_LETTER_SCORE:
            total += score(word[i])*2
        else:
            total += score(word[i])
    if T != 0:
        total = total*(3**T)
    if D != 0:
        total = total*(2**D)
    if len(word) == 7:
        total += 50
    return total

def add_word_down(board,word,r,c):
    T = 0
    D = 0
    occupied = []
    total = 0
    for i in range(len(word)):
        occupied.append((r+i,c)) 
    for i in range(len(occupied)):
        if occupied[i] in TRIPLE_WORD_SCORE:
            T += 1
            total += score(word[i])
        elif occupied[i] in DOUBLE_WORD_SCORE:
            D += 1 
            total += score(word[i])
        elif occupied[i] in TRIPLE_LETTER_SCORE:
            total += score(word[i])*3
        elif occupied[i] in DOUBLE_LETTER_SCORE:
            total += score(word[i])*2
        else:
            total += score(word[i])
    if T != 0:
        total = total*(3**T)
    if D != 0:
        total = total*(2**D)
    if len(word) == 7:
        total += 50
    return total
    
print(print_board(board))
print(add_word_across(board,'word',0,0))
print(score('word'))
print(add_word_across(board,'word',4,0))
print(add_word_across(board,'word',0,1))
print(add_word_down(board,'word',0,0))
print(score('word'))
print(add_word_down(board,'word',4,0))
print(add_word_down(board,'word',0,1))