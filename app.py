from flask import Flask
app = Flask(__name__)

## PART 1 - 4x4 Constraints
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


## PART 2 - Creating the REVISE function 

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
    print(cell1)
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
    

## Part 3 - Implementing AC-3 function, modifies a CSP removing all inconsistent domain values

def ac3(input_csp):
    '''
    Utilizing the revise function to modify a CSP object and ensures all variables are consistent
    with the constraints given.
    
    Args:
        input_csp (dict): The CSP to be revised, where the keys are cell names and the values are lists of possible values for that cell.
    
    Returns:
        bool: True if all variables still have at least one value in their domains, False otherwise
    '''
    # 4x Nested loop allows for every pair of cells to be considered, using the revise function to fix CSP
    for row1 in range(0, 10):
        for col1 in range(0, 10):
            for row2 in range(row1+1, 10):
                for col2 in range(0, 10):
                    # This nested loop will allow for every pair of cells on 9x9 board
                    revise(input_csp, 'C' + str(row1) + str(col1), 'C' + str(row2) + str(col2))
                    
    if [] in input_csp[:9]:
        return False
    return True
                    
                    
def csp_to_sudoku_board(csp):
    board = [[csp['C' + str(i) + str(j)] for j in range(1, 10)] for i in range(1, 10)]
    return board
        
    
    

@app.route('/')
def home():
    test = revise(constraint4x4, 'C12', 'C11')
    return (f"Hello, World!, {test}")

if __name__ == '__main__':
    app.run(debug=True)
    