# Algorithms: XOR
 
You are given two arrays A & B of positive integers each of size N.
Write a program to merge the two arrays A and B and find the XOR of the largest element and smallest element of the newly formed merged array.

Note
Here, "XOR" is bitwise XOR.
 
INPUT	OUTPUT
A	B	A XOR B
0	0	0
0	1	1
1	0	1
1	1	0


# Function Description
In the provided code snippet, implement the provided mergedArray(...) method using the variables to print a single integer denoting the XOR of the largest element and the smallest element of the newly formed merged array. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”. 

There will be multiple test cases running so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.

# Input Format
The code provided handles the input and stores them in variables for you.
The first line of input contains a positive integer N denoting the size of the arrays A and B.
The second line of input contains space-separated N positive integers of array A.
The third line of input contains space-separated N positive integers of array B.

# Sample Input
5                -- denotes N
7 5 8 7 1    -- denotes N elements of Array A
5 4 6 9 2    -- denotes N elements of Array B
 
# Constraints
1<= N,M <= 1000
1<= A[i],B[i] <= 10^9
 
# Output Format
The output contains a single integer denoting the XOR of the largest element and the smallest element of the newly formed merged array.
 
# Sample Output
8

# Explanation
Given array A = {7,5,8,7,1}
Given array B = {5,4,6,9,2}
After merging the arrays A & B, newly formed array = {7,5,8,7,1,5,4,6,9,2}.
The largest element of the newly formed array = 9.
The smallest element of the newly formed array = 1.
The XOR of the largest and smallest element of the newly formed array is = 9 ^ 1= 8.                     
Hence, the output is 8.