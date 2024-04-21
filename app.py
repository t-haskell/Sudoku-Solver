import ast
import copy
import random
from flask import Flask, request
import csp9x9


# CSP for a blank 9x9 Sudoku board
blank_csp = [csp9x9.variables9x9, csp9x9.constraint9x9]
# CSP for Puzzle 1
puzzle1 = [csp9x9.puzzle1var, csp9x9.constraint9x9]


app = Flask(__name__)



## PART 1 -> 4x4 Constraints/CSP -----------------------------------------------------------------------
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
    ('C12', 'C13'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C12', 'C14'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C13', 'C14'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    # Row 2
    ('C21', 'C22'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C21', 'C23'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C21', 'C24'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C22', 'C23'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C22', 'C24'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C23', 'C24'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    
    # Row 3
    ('C31', 'C32'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C31', 'C33'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C31', 'C34'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C32', 'C33'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C32', 'C34'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C33', 'C34'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    # Row 4
    ('C41', 'C42'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C41', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C41', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C42', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C42', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C43', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
# Columns
    # Column 1
    ('C11', 'C21'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C11', 'C31'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C11', 'C41'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C21', 'C31'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C21', 'C41'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C31', 'C41'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    # Column 2
    ('C12', 'C22'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C12', 'C32'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C12', 'C42'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C22', 'C32'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C22', 'C42'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C32', 'C42'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    # Column 3
    ('C13', 'C23'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C13', 'C33'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C13', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C23', 'C33'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C23', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C33', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    # Column 4
    ('C14', 'C24'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C14', 'C34'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C14', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C24', 'C34'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C24', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C34', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
# Sub-Grids
    # Sub-grid 1
    ('C11', 'C12'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C11', 'C21'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C11', 'C22'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C12', 'C21'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C12', 'C22'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C22', 'C21'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    # Sub-grid 2 
    ('C13', 'C14'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C13', 'C23'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C13', 'C24'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]], 
    ('C14', 'C23'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C14', 'C24'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C23', 'C24'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],   
    # Sub-grid 3
    ('C31', 'C32'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],  
    ('C31', 'C41'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C31', 'C42'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C32', 'C41'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],  
    ('C32', 'C42'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C41', 'C42'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    # Sub-grid 4
    ('C33', 'C34'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C33', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C33', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C34', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C34', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]],
    ('C43', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4]]}
]



## PART 2 -> Creating the REVISE function ---------------------------------------------------------

def revise(input_csp, cell1, cell2):
    """
    Revises the domain of a given cell in a constraint satisfaction problem (CSP) based on the constraints
    with another cell. A value is removed from 'cell1' domain if no values in 'cell2' domain can
    satisfy the list of valid arcs. 

    Args:
        input_csp (list): The CSP to be revised, index 0 being the dictionary of variables/domains and index 1 being the constraints.
        cell1 (str): The name of the cell whose domain should be revised.
        cell2 (str): The name of the cell whose constraints should be used to revise the domain of cell1.

    Returns:
        bool: True if the domain of cell1 was changed, False otherwise.
    """
    # Boolean value to return, indicates if changes were made
    revised = False
    for value1 in input_csp[0].get(cell1, []):
        found_valid = False
        # Checking the values in cell 2's domain 
        for value2 in input_csp[0].get(cell2, []):
            # Checking for validity of values in constraints, need to check both orders
            if [value1, value2] in input_csp[1].get((cell1, cell2), []) or [value2, value1] in input_csp[1].get((cell2, cell1), []):
            # If values are in constraints, proving validity, 
                # then we have found a valid value pair between cell1 and cell2
                found_valid = True
                break
        if found_valid is False:
            # If no satisfactory value pair, then value1 (from cell1 domain) is removed from cell1's domain
            input_csp[0][cell1].remove(value1)
            revised = True
    return revised
    


## Part 3 -> Implementing AC-3 function, with its helper function for finding 'neighbors'

def get_neighbors(cell):
    """
    Helper function for the AC-3 algorithm, finds a list of the cells that are in the same row,
    column, and sub-box as the given cell.

    Args:
        cell (str): The name of the cell

    Returns:
        neighbors (list): List of names of cells that are 'neighbors' of the given cell
    """
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
    """
    Utilizing the revise function to modify a CSP object and ensures all variables are consistent
    with the constraints given.
    
    Args:
        input_csp (list): The CSP to be revised, where the first element is a dict of cells mapping
            to lists of possible values, and the second element is a dict of constraints represented as 
            tuples mapping to lists of valid value pairs.
    
    Returns:
        bool: True if all variables still have at least one value in their domains, False otherwise
    """
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
            neighbors = get_neighbors(cell_pair[0])
            for neighbor in neighbors:
                queue.append([neighbor, cell_pair[0]])
    return True



## PART 4 -> MINIMUM-REMAINING-VALUE FUNCTION

def minimum_remainng_values(csp, var_assignments):
    """
    Helps find the next best move, finding the variable with the fewest remaining possibilities
    that isn't already assigned a final value (Assigned variables are in var_assignments)
    
    Args:
        csp (list): The CSP with variables/domains and constraints
        var_assignments (dict): Keys are variables and values are the assigned values
    
    Returns:
        min_cell (str): Name of the variable with the fewest remaining possibilities
    """
    min_cell = ''
    # Iterate over all the variables/domains in the csp
    for cell in csp[0]:
        if cell not in var_assignments:
            # Count remaining possibilities
            num_poss = len(csp[0][cell])
            # If domain is less than current min OR min name is an empty string
            if min_cell == '' or num_poss < len(csp[0][min_cell]):
                # Then set the new minimum cell 
                min_cell = cell
                
    return min_cell


## PART 5 -> BACKTRACKING SEARCH

def order_domain_values(csp, cell):
    """
    Randomly shuffles a cell's domain values to prevent getting stuck in local minima

    Args:
        csp (list): The CSP object with the variables/domains and constraints, needed to get domain
        of cell in argument
        cell (str): String value of the cell who's domain is being shuffled

    Returns:
        list: The newly shuffled domain list, showing the valid values this cell can have
    """
    domain = csp[0][cell]
    # Random order to shuffle domain values and prevent getting stuck
    random.shuffle(domain)
    return domain
    

def is_consistent(cell, value, assignment):
    """
    Checks if a given value for a cell is consistent with the current assignment.

    Args:
        cell (str): The cell being assigned.
        value (str): The value being assigned to the cell.
        assignment (dict): The current assignment of values to cells.

    Returns:
        bool: True if the value is consistent with the current assignment, False otherwise.
    """
    # Check if value is consistent with assignment so far
    relevant = get_neighbors(cell)
        
    for square in relevant:
        # If the neighbor has been assigned AND if the potential value is the same as an already assigned value
        if square in assignment and value == assignment[square]:
            # Then this potential value is inconsistent with the current state
            return False
            
    return True
    

def backtrack_search(csp):
    """
    Performs a backtracking search to solve the given constraint satisfaction problem (CSP). Contains
    a function definition for backtrack(csp, assignment) that recursively tries assignments for cells

    Args:
        csp (dict): The CSP with variables/domains and constraints.

    Returns:
        tuple: A tuple containing the following:
            - assignment (dict): The final variable assignments that solve the CSP.
            - ordered_assignments (list): The order in which the variables were assigned.
            - remaining_domains (list): The remaining domains of unassigned variables after
            each assignment.
    """
    
    ordered_assignments = []    # Stores order of assignments
    remaining_domains = []      # Stores remaining domains after each assignment
    
    # Setting assignments to the cells with a single valued domain
    new_assignment = {}
    for cell in csp[0]:
        if len(csp[0][cell]) == 1:
            ordered_assignments.append(cell)
            new_assignment[cell] = csp[0][cell][0]
    
    # Ensuring the CSP is arc-consistent before starting
    ac3(csp)
    
    # Function definition for recursive portion of backtrack search 
    def backtrack(csp, assignment):
        """
        Recursive backtracking function that tries assignments for the next cell.

        Args:
            csp (list): The current state's CSP with variables/domains and constraints.
            assignment (dict): This state's current assignment of cells to values

        Returns:
            None: If no solution is found for the current test cell, None is returned
        """
        # If every cell is assigned, return variable assignments
        if len(assignment) == len(csp[0]): 
            return assignment, ordered_assignments, remaining_domains
        
        # Get the next cell based on minimum remaining values function
        test_cell = minimum_remainng_values(csp, assignment)
        
        # Store the remaining domains of unassigned variables before making the assignment
        remaining_domains.append({cell: csp[0][cell] for cell in csp[0] if cell not in assignment})
        
        # Iterating through domain values for test cell, shuffled for randomness
        for value in order_domain_values(csp, test_cell):
            # If value is consistent with the assignment so far
            if is_consistent(test_cell, value, assignment):
                assignment[test_cell] = value   # Add cell/value pair to assignment
                ordered_assignments.append(test_cell)   # Adding to ordered list                
                
                # Making a copy of current csp in case we backtrack
                cspCopy = copy.deepcopy(csp)
                infer = ac3(cspCopy)
                
                # If inference succeeded
                if infer:
                    # (**) Dont have to add inferences back to original CSP, used a copy cspCopy
                    # Recursively calling backtrack with updated assignment
                    result = backtrack(cspCopy, assignment)                    
                    if result is not None:
                        return result
                    # (**) Dont have to remove inferences from CSP, used a copy as input to recursion
                    
                del assignment[test_cell]   # Removing the assignment
                ordered_assignments.pop()   # Removing from ordered list
                remaining_domains.pop()     # Removing the domain of the unassigned variable                
                
        return None # No solution found
    
    # Starting backtrack search
    return backtrack(csp, new_assignment)     



## PART 6 - Displaying the backtrack search step by step

def display_csp(current_domains):
    """
    Generates an HTML table representation of the current state of a Constraint Satisfaction Problem
    (CSP). Each cell displaying either the assigned value (if the domain has only one element) or a
    space (if the domain has multiple elements).

    Args:
        current_domains (dict): A dictionary mapping each cell in the CSP to its current domain (a list of possible values).

    Returns:
        str: An HTML string representing the current state of the CSP.
    """
    html = "<h2>Sudoku Puzzle</h2>"
    html += "<head> <title>Sudoku Puzzle</title> <link rel='stylesheet' type='text/css' href='static/styles.css'></head>"
    html += "<table class='sudoku-table'>"
    # Iterating through all cell values in 9x9 board
    for row in range(1, 10):
        # Starting a row
        html += "<tr>"
        for col in range(1, 10):
            cell = "C" + str(row) + str(col)
            # If the cell is in unassigned, then make the value None
            value = current_domains[cell][0] if len(current_domains[cell]) == 1 else " "
            # Board Square value thats shown in the board
            html += f"<td class='sudoku-cell'>{value}</td>"
            # Adding thicker lines for sub-boxes
            if col in (3, 6):
                html += "<td class='sub-box'></td>"
        # Ending the row
        html += "</tr>"
        # Adding thicker lines for sub-boxes
        if row in (3, 6):
            html += "<tr class='sub-box'></tr>"
    html += "</table>"
    return html
    
    
def parse_input_puzzle(puzzle):
    """
    Creates a new empty CSP (Constraint Satisfaction Problem) by copying the blank CSP, and then
    iterates through the provided puzzle, replacing the domains of blank CSP with the numeric values found
    
    Args:
        puzzle (list): A list of strings representing the puzzle to be solved, each list being a row
    
    Returns:
        tuple: A new CSP with the puzzle values added to the domains.
    """
    # Creates a new empty CSP
    newCSP = [copy.deepcopy(blank_csp[0]), copy.deepcopy(blank_csp[1])]
    
    # Turning input string into a nested list
    comma_seperated = puzzle.replace("%20", ",")
    # Extra step needed due to URL encoding of '%20'
    comma_seperated = comma_seperated.replace(" ", ",")
    comma_seperated = comma_seperated.replace("(", "[")
    comma_seperated = comma_seperated.replace(")", "]")
    comma_seperated = comma_seperated.replace("nil", "0")
    # After making replacements to string input, create nested list structue w eval()
    nested_list = ast.literal_eval(comma_seperated)
    
    # Iterate on each row
    for j, row in enumerate(nested_list):
        # Iterate on each character in the row
        for i, cell in enumerate(row):
            # If value is not a number, then dont change that cell's domain
            if cell != 0:
                cellName = "C" + str(j+1) + str(i+1)
                # Add the cell to the CSP with the found value
                newCSP[0][cellName] = [int(cell)]
    print(newCSP[0])
                
    return newCSP


@app.route('/')
def home():
    '''
    PUZZLE INPUT AS QUERY PARAMETER IN URL - Programmed to accept the same format as
    the example puzzles 
    '''
    # Get puzzle from the query parameter
    puzzle = request.args.get('puzzle')
    
    # Check if a puzzle was provided
    if puzzle is None:
        # If not, use puzzle 1 as default
        currCSP = puzzle1
    else:
        # Parsing the provided puzzle
        currCSP = parse_input_puzzle(puzzle)
        
    starting_domains = copy.copy(currCSP[0])
    assignment_test, ordered_test, remaining_test = backtrack_search(currCSP)
    
    # Creating list of HTML code for each board
    all_boards = []
    step_counter = 0
    for state in ordered_test:
        step_counter += 1
        # Updating domain of cell thats next to be assigned, maintaining list format but with assignment as the only value
        starting_domains[state] = [assignment_test[state]]
        # Add the HTML code to represent this state of the board to list of board states to solution
        all_boards.append(display_csp(starting_domains))
        
    return (f"\n\nScroll down to see step by step solution: {''.join(all_boards)}")

if __name__ == '__main__':
    app.run(debug=True)
    