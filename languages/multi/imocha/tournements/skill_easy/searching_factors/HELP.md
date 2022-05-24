# Searching Algorithms: Searching Factors

You are given an array of size N.
A number in the array is called a mutual number if it has at least 2 of its unique factors, excluding the number itself in the array.
Write a program to count the number of mutual numbers and print them in ascending order.

# Note
1. All the elements in the array are unique.
2. Mutual numbers having 2 factors (e.g. A and B) are present in the array such that A!=B

# Function Description
In the provided code snippet, implement the provided searchFactors(...) method using the variables to count the number of mutual numbers and print them in ascending order.
You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”. 

There will be multiple test cases running so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.

# Input Format
The code provided handles the input and stores them in variables for you.
The first line contains an integer N, denoting the size of the array.
The next line contains N space-separated integers of the array.

# Sample Input
6                    -- denotes N
2 6 3 4 12 8   -- denotes N elements of array

# Constraints
3<= N <=1000
1<= A[i] <=100000
 
# Output Format
The first line contains the count of the mutual numbers.
In the next line, print all the space-separated mutual numbers in ascending order.

# Sample Output
3
6 8 12
 
# Explanation
Factors of 6: 1, 2, 3 out of which 2 and 3 are present in the array.
Factors of 12: 1, 2, 3, 4, 6 out of which 2, 3, 4, 6 are present in the array.
Factors of 8: 1, 2, 4 out of which 2, 4 are present in the array.
Hence, the output:
3
6 8 12.