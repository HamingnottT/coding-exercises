# Binary Search: Painter's Dilemma

You can draw a painting by using two shades of watercolor and zero shades of poster color to draw a painting of a size 1-meter cube.
To draw a painting of a size 2-meter cube, you need to add two more shades of watercolor and 1 more shade of poster color to your color collection.
For a 3-meter cube painting, you again need to add 2 more shades of watercolor and 1 more shade of poster color to your collection and so on.
You are given a box with an unlimited supply of color shades of both types but you can only use N of them.
You start with these N shades and create a painting of the largest area possible.
If some shades are left, then you create another painting of the largest area possible with those remaining shades.
You can do this again and again until it becomes impossible to create a painting.
Print the count of the maximum number of paintings you can paint.
 
# Function Description
In the provided code snippet, implement the provided paintersDilemma(...) method using the variables to print the maximum number of paintings you can paint. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.

There will be multiple test cases running so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.

# Input Format
The first line contains T denoting the number of test cases.
Next T lines contain an integer N.
 
# Sample Input
2     -- denotes T test cases.
14   -- denotes N shades. 
15   -- denotes N shades.
 
# Constraints
1 <= T <= 1000.
1 <= N <=109.

# Output Format
The output contains the maximum number of paintings you can paint.

# Sample Output
2
1
 
# Explanation
T = 2 and N = {14, 15}
For N = 14, you can create 2 paintings of a 2-meter cube using 7 shades each.
7 shades - (2 watercolors + 0 poster color) and then (4 watercolors + 1 poster color) which in total comes out to be 7 shades.
For N = 15, you can create a painting of size 3 meter cube which would require 15 shades in total which include (2 + 4 + 6) watercolors and (0 + 1 + 2) postercolors.