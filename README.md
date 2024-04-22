# Sudoku Solver via Constraint Satsifaction Approach
By: Tommy Haskell

---------------------![image](https://github.com/t-haskell/Sudoku-Solver/assets/94083215/81d22b2e-827a-47b2-8ea4-5f8ceeb6dda5)
![image](https://github.com/t-haskell/Sudoku-Solver/assets/94083215/9d06a2c0-c8ce-4bf6-b250-616c3cf869af)----------------------



### Environment Setup
Created using the Flask web development package. Ensure an updated version of Python is downloaded and installed. There were three external packages that were utilized:
1. *ast* - allowed for literal evaluation of the input from the query parameter in the url, enabling valid input to the backtrack search
2. *copy* - copies of CSP states allowed for easy maintanence of action sequences in recursion
3. *random* - randomized a cell's domain in the search algorithm
4. *request* (Flask) - retrieves the query parameter from the url

   
### Running the Application
To run the application, open the terminal and navigate to the directory containing the application. Then, run the following command:

```
python3 app.py
```
The application will then be accessible at the following URL:
```
http://localhost:5000/
```

### Custom Puzzle Input by User
Query parameter functionality was used to implement this feature. To input a custom puzzle to be solved, follow the format of the example puzzles in the project write-up. 


For example, to solve puzzle 2 you could paste this into your search bar:
```
http://localhost:5000/?puzzle=((1%20nil%20nil%202%20nil%203%208%20nil%20nil)%20(nil%208%202%20nil%206%20nil%201%20nil%20nil)%20(7%20nil%20nil%20nil%20nil%201%206%204%20nil)%20(3%20nil%20nil%20nil%209%205%20nil%202%20nil)%20(nil%207%20nil%20nil%20nil%20nil%20nil%201%20nil)%20(nil%209%20nil%203%201%20nil%20nil%20nil%206)%20(nil%205%203%206%20nil%20nil%20nil%20nil%201)%20(nil%20nil%207%20nil%202%20nil%203%209%20nil)%20(nil%20nil%204%201%20nil%209%20nil%20nil%205))
```
This string will be transformed into a nested list to be handled by the backtrack search. The '%20' is just URL encoding for a whitespace or return, and it will work whether these are included or not.

#### File Structure Information
The domain values for the puzzle 1 cells are in the csp9x9.py file, along with the porvides constraints for a 9x9 puzzle. These variables are imported into app.py where blank and puzzle 1 CSPs are created, as a list of two dictionaries. The first dictionary of a CSP contains the variables/domains and the second dictionary is the cosntraints for the board. 
