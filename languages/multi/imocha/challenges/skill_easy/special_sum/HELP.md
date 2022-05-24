# Array Operations: Special Sum

You are given an array of size N and a number K.
Find the special sum of array elements. 

# Note
A special sum is defined as the sum of selected elements from the array. If the value of K is 1, select one element, drop the second element, select the next element and drop the next element, and so on.

# Function Description
In the provided code snippet, implement the provided specialSum(...) method using the variables to print the special sum of array elements. You can write your code in the space below the phrase “WRITE YOUR CODE HERE”.  

There will be multiple test cases running so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.

# Input Format
The first line contains N.
The second line contains N space-separated integers denoting the array elements.
The third line contains the value of K.

# Sample Input

14
1 5 9 7 8 6 4 3 2 1 0 5 8 7
5

# Output Format
The output should be the special sum of the array.
 
# Sample Output

50 

# Explanation 
As K is 5, we need to take 5 values and leave 5 values. 
1 5 9 7 8 6 4 3 2 1 0 5 8 7 
The underlined elements in the above array will sum up to 50.