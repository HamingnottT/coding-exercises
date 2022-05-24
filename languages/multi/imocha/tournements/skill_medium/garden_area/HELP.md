# Recursion: Garden Area

You are given a “N*M” grid representing a map where A[i][j] = 1 represents garden (or a part of garden) and A[i][j] = 0 represents mud.
Grid cells are connected horizontally or vertically but not diagonally.
The grid is surrounded by mud and there is exactly one garden (i.e., one or more connected garden cells).
One cell is a square with a side length 2. The grid is rectangular.
Determine the perimeter and area of the garden.

# Note
An integer N is a positive integer (where N is the no. of rows).
An integer M is a positive integer (where M is the no. of columns).
 

# Function Description
In the provided code snippet, implement the provided gardenArea(...) method using the variables to print the perimeter and area of the garden area. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.

There will be multiple test cases running so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.


# Input Format
The first line contains an integer N and an integer M.
The next N lines contain M integers each representing the grid.

# Sample Input

3 2
0 1
1 1
1 0

# Constraints
 2 <= N <= 40.
 2 <= M <= 40.
A [ i ][ j ] = 1 ( garden area)  A [ i ][ j ] = 0 ( mud )

# Output Format
The output contains the perimeter and area of the garden area.

# Sample Output

20
16