def find_next_empty(puzzle):
    #finds the next row or col thats not filled (-1)
    #return row, col tuple or (None, None) if there is none
    for r in range(9): #index 0-8
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
            
    return None, None #if no empty spaces

def is_valid(puzzle, guess, row, col):
    #lets start with row check
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    #column check
    #col_vals = []
    #for i in range(9):
        #col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range (9)]
    if guess in col_vals:
        return False
    
    # 3x3 grid 0,3,6
    #iterate over values of 3
    row_start = (row//3) *3 
    col_start = (col//3) *3
    
    for r in range(row_start, row_start +3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] ==guess:
                return False
    
    return True
    
        
def sudoku_solver(puzzle):
    #find empty space
    row, col = find_next_empty(puzzle)
    if row is None:
        return True #puzzle solved
    
    for guess in range(1,10):
        #check for valid guess
        if is_valid(puzzle, guess, row, col):
            #place the guess on the puzzle
            puzzle[row][col] = guess
            #recursion
            #mutate until solution found
            if sudoku_solver(puzzle):
                return True
            
    #not valid or guess did not solve puzzle
    #backtrack and try new number
    puzzle[row][col] = -1 #reset the guess
    
    #if every combination does not work, unsolvable puzzle
    return False


#try on an example
#if __name__ == '__main__':
#   example board =[[]]