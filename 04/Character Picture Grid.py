def Character_Picture_Grid(Z):
    a = 0
    b = 0
    while b != len(Z[0]):
        while a != len(Z):
            if a == len(Z)-1:
                print (Z[a][b])
            else:
                print (Z[a][b], end='')
            a+=1
        a=0
        b+=1

grid = [['.', '.', '.', '.', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['.', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.']]

Character_Picture_Grid(grid)