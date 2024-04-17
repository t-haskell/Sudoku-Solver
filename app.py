from flask import Flask, render_template
import csp9x9

# CSP for a blank 9x9 Sudoku board
blank_csp = [csp9x9.variables9x9, csp9x9.constraint9x9]
# CSP for Puzzle 1
puzzle1 = [csp9x9.puzzle1var, csp9x9.constraint9x9]


app = Flask(__name__)

## PART 1 - 4x4 Constraints/CSP -----------------------------------------------------------------------
constraint4x4 = [
    # Variables
    {'C11': [1], 'C12': [1, 2, 3, 4], 'C13': [1, 2, 3, 4], 'C14': [1, 2, 3, 4],
    'C21': [1, 2, 3, 4], 'C22': [2], 'C23': [1, 2, 3, 4], 'C24': [1, 2, 3, 4],
    'C31': [1, 2, 3, 4], 'C32': [1, 2, 3, 4], 'C33': [3], 'C34': [1, 2, 3, 4],
    'C41': [1, 2, 3, 4], 'C42': [1, 2, 3, 4], 'C43': [1, 2, 3, 4], 'C44': [4]},
    
    # Constraints
    # Row 1
    {('C11', 'C12'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C11', 'C13'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C11', 'C14'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    # Row 2
    ('C21', 'C22'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C21', 'C23'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C21', 'C24'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    # Row 3
    ('C31', 'C32'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C31', 'C33'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]], 
    ('C31', 'C34'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    # Row 4
    ('C41', 'C42'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C41', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C41', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    # Column 1
    ('C11', 'C21'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C11', 'C31'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C11', 'C41'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    # Column 2
    ('C12', 'C22'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C12', 'C32'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C12', 'C42'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    # Column 3
    ('C13', 'C23'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C13', 'C33'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C13', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    # Column 4
    ('C14', 'C24'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C14', 'C34'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C14', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    # Sub-grid 1
    ('C11', 'C12'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C11', 'C21'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C11', 'C22'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    # Sub-grid 2 
    ('C13', 'C14'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C13', 'C23'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C13', 'C24'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],   
    # Sub-grid 3
    ('C31', 'C32'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],  
    ('C31', 'C41'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C31', 'C42'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    # Sub-grid 4
    ('C33', 'C34'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C33', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C33', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]]}
]


## PART 2 - Creating the REVISE function ---------------------------------------------------------

def revise(input_csp, cell1, cell2):
    '''
    Revises the domain of a given cell in a constraint satisfaction problem (CSP) based on the constraints with another cell.

    Args:
        input_csp (dict): The CSP to be revised, where the keys are cell names and the values are lists of possible values for that cell.
        cell1 (str): The name of the cell whose domain should be revised.
        cell2 (str): The name of the cell whose constraints should be used to revise the domain of cell1.

    Returns:
        bool: True if the domain of cell1 was changed, False otherwise.
    '''
    # Boolean value to return, indicates if changes were made
    revised = False
    for value1 in input_csp[0].get(cell1, []):
        found_valid = False
        # Checking the values in cell 2's domain 
        for value2 in input_csp[0].get(cell2, []):
            #### DEBUGGING print(f"Checking if {value1} in {cell1}'s domain is valid with {value2} in {cell2}'s domain")
            # Checking for validity of values in constraints, need to check both orders
            if [value1, value2] in input_csp[1].get((cell1, cell2), []) or [value2, value1] in input_csp[1].get((cell2, cell1), []):
            # If values are in constraints, proving validity, 
                # then we have found a valid value pair between cell1 and cell2
                found_valid = True
                #### DEBUGGING print("VERIFIED")
                break
            #### DEBUGGING print("NOT VALID")
        if found_valid is False:
            # If no satisfactory value pair, then value1 (from cell1 domain) is removed from cell1's domain
            #### DEBUGGING print("DOMAIN REMOVAL")
            input_csp[0][cell1].remove(value1)
            revised = True
    return revised
    

## Part 3 - Implementing AC-3 function, with its helper function for finding 'neighbors'

def get_neighbors(cell, csp):
    '''
    Helper function for the AC-3 algorithm, finds a list of the cells that are in the same row,
    column, and sub-box as the given cell.
    
    Args:
        cell (str): The name of the cell
        csp (list): Contains two dictionaries, one for the variables/domains and the other for contraints
    
    Returns:
        neighbors (list): List of names of cells that are 'neighbors' of the given cell
    '''
    neighbors = []
    # Not going to worry about adding the cell itself, will remove at the end
    # Add row neighbors
    for r in range(9):
        # Appending each cell by incrmenting the last character of the cell name
        neighbors.append('C' + cell[1] + str(r+1))
    # Add column neighbors
    for c in range(9):
        # Appending each cell by incrmenting the middle character of the cell name
        neighbors.append('C' + str(c + 1) + cell[2])
    # Add sub-box neighbors
    # Nested lists of the cells in each sub-box of a classic 9x9 Sudoku board
    subboxes = [
                ['C11', 'C12', 'C13', 'C21', 'C22', 'C23', 'C31', 'C32', 'C33'],
                ['C14', 'C15', 'C16', 'C24', 'C25', 'C26', 'C34', 'C35', 'C36'],
                ['C17', 'C18', 'C19', 'C27', 'C28', 'C29', 'C37', 'C38', 'C39'],
                ['C41', 'C42', 'C43', 'C51', 'C52', 'C53', 'C61', 'C62', 'C63'],
                ['C44', 'C45', 'C46', 'C54', 'C55', 'C56', 'C64', 'C65', 'C66'],
                ['C47', 'C48', 'C49', 'C57', 'C58', 'C59', 'C67', 'C68', 'C69'],
                ['C71', 'C72', 'C73', 'C81', 'C82', 'C83', 'C91', 'C92', 'C93'],
                ['C74', 'C75', 'C76', 'C84', 'C85', 'C86', 'C94', 'C95', 'C96'],
                ['C77', 'C78', 'C79', 'C87', 'C88', 'C89', 'C97', 'C98', 'C99']
                ]
    # Iterating through sub-box of cells to check which one the input cell is in
    for box in subboxes:
        if cell in box:
            # Appending each cell name in the list to the neighbors list
            for square in box:
                neighbors.append(square)
    # Removing all the instances of the input cell itself being its own neighbor
    neighbors = list(filter(lambda x: x != cell, neighbors))
    return neighbors
    

def ac3(input_csp):
    '''
    Utilizing the revise function to modify a CSP object and ensures all variables are consistent
    with the constraints given.
    
    Args:
        input_csp (dict): The CSP to be revised, where the keys are cell names and the values are lists of possible values for that cell.
    
    Returns:
        bool: True if all variables still have at least one value in their domains, False otherwise
    '''
    # Pushing all cell pairs onto the queue, each as a list
    queue = [[cell1, cell2] for (cell1, cell2) in input_csp[1].keys()]

    while queue:
        # Popping the top cell pair off queue
        cell_pair = queue.pop(0)
        if revise(input_csp, cell_pair[0], cell_pair[1]):
            # Only have to check first cell variable since its domain has been changed (revise resulted in true)
            if input_csp[0][cell_pair[0]] == []:
                return False
            # Creating list of neighboring arc with the changed cell
            # (In Sudoku, this is all cells in its row, column, and sub-box)
            neighbors = get_neighbors(cell_pair[0], input_csp)
            #### DEBUGGING print(neighbors) 
            for neighbor in neighbors:
                queue.append([neighbor, cell_pair[0]])
    return True



## PART 4 -> MINIMUM-REMAINING-VALUE FUNCTION

def minimum_remainng_values(csp, var_assignments):
    '''
    Helps find the next best move, finding the variable with the fewest remaining possibilities
    that isn't already assigned a final value (Assigned variables are in var_assignments)
    
    Args:
        csp (dict): The CSP with variables/domains and constraints
        var_assignments (dict): Keys are variables and values are the assigned values
    
    Returns:
        min_cell (str): Name of the variable with the fewest remaining possibilities
    '''
    min_cell = ''
    # Iterate over all the variables/domains in the csp
    for cell in csp[0]:
        if cell not in var_assignments:
            # Count remaining possibilities
            num_poss = len(csp[0][cell])
            # If domain is less than current min OR min name is an empty string
            if num_poss < len(csp[0][min_cell]) or min_cell == '':
                # Then set the new minimum cell 
                min_cell = cell
    return min_cell
        
     


        
    
    

@app.route('/')
def home():
    currCSP = puzzle1
    #test = revise(currCSP, 'C11', 'C12')
    possible = ac3(currCSP)
    neighbors = get_neighbors('C11', currCSP)
    return (f"Hello, World! Is it possible? {possible} \n {currCSP[0]}")
    #return render_template('index.html', board=board)

if __name__ == '__main__':
    app.run(debug=True)
    