from art import logo


def gauss_seidel(A, b, x0, num_of_iteration):
    """
    :param A:Coefficient matrix
    :param b:Right-hand side vector
    :param x0:Initial guess
    :param num_of_iteration:Number of iteration
    :return: the final solution vector
    """
    n = len(A)
    x = x0.copy()

    for step in range(num_steps):
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = round((b[i] - s) / A[i][i], 6)

    return x


# Coefficient matrix
A = [[1, 9, -2],
     [2, -1, 8],
     [6, 1, 1]]

# Right-hand side vector
b = [36, 121, 107]

# Initial guess
x0 = [0, 0, 0]

# Number of iteration steps
num_steps = 10

# Solve the system of equations
solution = gauss_seidel(A, b, x0, num_steps)

print(logo)
# Print the solution rounded to 6 significant digits
print("Solution:")
for i, value in enumerate(solution):
    print(f"x{i + 1} = {value:.6g}")
