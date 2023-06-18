
This code solves a `system of linear equations` using the `Gauss-Seidel method`. It takes as input a `coefficient matrix`, a `right-hand side vector`, `an initial guess for the solution vector`, and `the number of iteration steps to perform`.

#########################################################################################
#                                     FUNCTION                                          #
#########################################################################################

## Function:
gauss_seidel(A, b, x0, num_of_iteration)

## Description:
This function implements the Gauss-Seidel method for solving a system of linear equations.

## Parameters:
- A: Coefficient matrix (list of lists)
- b: Right-hand side vector (list)
- x0: Initial guess for the solution vector (list)
- num_of_iteration: Number of iteration steps to perform (integer)

Returns:
- The final solution vector (list)

#########################################################################################
#                                   IMPORTED MODULES                                    #
#########################################################################################

## Module:
art

Description:
This module provides ASCII art text for the program logo.

#########################################################################################
#                                     USED METHOD                                       #
#########################################################################################

## Method:
copy()

Description:
This method is used to create a deep copy of the initial guess solution vector 'x0'. It ensures that the original 'x0' remains unchanged during the iterations.

#########################################################################################
#                                      MAIN CODE                                        #
#########################################################################################

- Coefficient matrix:
  - A = [[1, 9, -2], [2, -1, 8], [6, 1, 1]]

- Right-hand side vector:
  - b = [36, 121, 107]

- Initial guess for the solution vector:
  - x0 = [0, 0, 0]

- Number of iteration steps:
  - num_steps = 10

- Solve the system of equations using the Gauss-Seidel method:
  - solution = gauss_seidel(A, b, x0, num_steps)

- Print the program logo:
  - print(logo)

- Print the solution rounded to 6 significant digits:
  - for i, value in enumerate(solution):
      - print(f"x{i + 1} = {value:.6g}")

#########################################################################################
#                                  HOW TO RUN LOCALLY                                  #
#########################################################################################

1. Ensure that you have the required dependencies installed. You can install the necessary packages using pip:

2. Copy the code into a Python file (e.g., `linear_equations_solver.py`).

3. Run the Python script:


The solution for the system of linear equations will be displayed in the console output.

#########################################################################################
