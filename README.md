# Sudoku CSP Solver
### Author: <Tommy Haskell>

## ENVIRONMENT SETUP
Created using the Flask web development package. Ensure an updated version of Python is downloaded and installed. 

## RUNNING THE APPLICATION
To run the application, open the terminal and navigate to the directory containing the application. Then, run the following command:

```
python3 app.py
```
The application will then be accessible at the following URL:
```
http://localhost:5000/
```

## CUSTOM PUZZLE INPUT BY USER
Query parameter functionality was used to implement this feature. To input a custom puzzle to be solved, follow the format of the example puzzles in the project write-up. For example, to solve puzzle 2 you would paste this into your search bar:
```
http://localhost:5000/?puzzle=((1%20nil%20nil%202%20nil%203%208%20nil%20nil)%20(nil%208%202%20nil%206%20nil%201%20nil%20nil)%20(7%20nil%20nil%20nil%20nil%201%206%204%20nil)%20(3%20nil%20nil%20nil%209%205%20nil%202%20nil)%20(nil%207%20nil%20nil%20nil%20nil%20nil%201%20nil)%20(nil%209%20nil%203%201%20nil%20nil%20nil%206)%20(nil%205%203%206%20nil%20nil%20nil%20nil%201)%20(nil%20nil%207%20nil%202%20nil%203%209%20nil)%20(nil%20nil%204%201%20nil%209%20nil%20nil%205))
```
This string will be transformed into a nested list to be handled by the backtrack search. The '%20' is just URL encoding for a whitespace or return, and it will work whether these are included or not.
