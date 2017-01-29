import copy
import pdb

assignments = [] 

# A couple of auxiliary objects and methods to support the strategy functions
rows = 'ABCDEFGHI'
cols = '123456789'

def cross(a, b):
    return [s+t for s in a for t in b]

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diagonal_units = [[rows[x]+cols[x] for x in range(0, 9)],[rows[x]+cols[8-x] for x in range(0, 9)]]

unitlist = row_units + column_units + square_units + diagonal_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def assign_value(values, box, value):
    """
    Whenever a box is reduced to a single number, the values of the sudoku are saved in the assignments array
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):

    """
    Takes the sudoku as dictionary and executes the 'naked twins' strategy: Looping over units trying to find 
    two find two boxes in this unit having the same two numbers as possible solutions. If found, it removes 
    those numbers from all other boxes in the unit. 
    """

    for unit in unitlist:  
        for box in unit:
            if len(values[box])==2:
                twin =  [values[peer] for peer in unit if values[peer]==values[box]]
                if len(twin)==2:
                    for peer in unit:
                        if len(values[peer])>2:
                            values = assign_value(values,peer,values[peer].replace(values[box][0],"").replace(values[box][1],""))
    return values



def grid_values(grid):

    """
    Takes a sudoku grid with "." for unknown numbers and the set number otherwise. Returns a dictionary
    with box position as key and the string of possible numbers as number.
    """

    values = []
    all_digits = '123456789'
    for c in grid:
        if c == '.':
            values.append(all_digits)
        elif c in all_digits:
            values.append(c)
    return dict(zip(boxes, values))

def display(values):

    """
    Takes a dictionary and visualises the sudoku values
    """

    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)

def eliminate(values):

    """
    Takes a dictionary and executes the 'eliminate' stategy. For all boxes which are reduced 
    to one possible solution it removes the box's number from all peer boxes. 
    """

    for key, boxString in values.items():
        if len(boxString)==1:
            for peer in peers[key]:
                values = assign_value(values,peer,values[peer].replace(boxString,""))
    return values

def only_choice(values):

    """
    Takes a dictionary and executes the 'only choice' strategy. In each unit it looks for 
    possible locations of a number. If there is only one box, it assigns the number.
    """

    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values = assign_value(values,dplaces[0], digit)
    return values

def reduce_puzzle(values):

    """
    Takes a dictionary and applies all three strategies as long as solved_values
    increases.
    """

    solved_values = [box for box in values.keys() if len(values[box]) == 1]

    stalled = False #becomes true when solved_values does not change after strategy execution.

    while not stalled:

        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])


        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)

        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after

    return values


def search(values):

    """
    Takes a dictionary and traverses the tree of possible solutions using Depth First Search. 
    If reduce_puzzle does not lead to a solution, it assigns a number to a box and tries to solve
    this sudoku. This is done recursevely until a valid solution is found or variations are found to
    be impossible.
    """
   
    values = reduce_puzzle(values)
    
    if values is False:
        return False
    
    #check if sudoku is solved
    if all(len(values[box])==1 for box in boxes): 
        return values
        
    #el is the the first box in the sudoku with more than one solution    
    el = min((box for box in boxes if len(values[box])>1), key=lambda box:values[box])   


    for value in values[el]:
        sudoku_alt = values.copy()
        sudoku_alt[el] = value
        attempt = search(sudoku_alt)

        #attempt becomes False when the sudoku is not solvable. This node can be ignored

        if attempt:
            return attempt

def solve(grid):
    values = grid_values(grid)

    return search(values)

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
