def generate_pascal(n):
    triangle = []

    for i in range(n):
        # Start each row with 1
        row = [1] * (i + 1)
        
        # Calculate the interior values
        for j in range(1, i):
            # Sum the two numbers directly above
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            
        triangle.append(row)
        
    return triangle

def print_triangle(triangle):
    # Determine the width for formatting
    n = len(triangle)
    max_width = len(" ".join(map(str, triangle[-1])))

    for row in triangle:
        # Convert numbers to string and join with space
        row_str = " ".join(map(str, row))
        # Center the string to create the triangle shape
        print(row_str.center(max_width))

# --- Run the Program ---
rows = int(input("Enter the number of rows: "))
my_triangle = generate_pascal(rows)
print_triangle(my_triangle)
