# Strings: Shortest String

You are given a binary string S of size N.
You can perform the following operation on the string any number of times: 
In one operation, you can either delete substring "01" or "11" from the string and that substring gets deleted from the string and the remaining parts of the string get concatenated. 
Find the length of the shortest string you can make after performing the above operation any number of times. 
 
# Note 
A binary string is a string that contains only 0s and 1s. 

# Function Description 
In the provided code snippet, implement the provided shorteststring(...) method to print the length of the shortest string.
You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.
There will be multiple test cases running so the Input and Output should match exactly as provided. 
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables. 

# Input Format
The first line of input contains an integer N denoting the size of the string. 
The second line of input contains a binary string S. 
 
# Sample Input 
4          -- denotes N
1011   -- denotes binary string S

# Constraints 
1≤ N ≤10 

# Output Format 
The output contains a single integer denoting the length of the shortest string. 
 
# Sample Output 
0 

# Explanation 
Considering 0 based indexing in the first operation, we can delete the characters present at index 1 and 2 as there is a substring "01" present at the index at 1.
The following operation looks like this:
1010 => 10 
After the above operation, the string becomes "11". We can further delete this string as there is a substring "11" present at the index at 0.
The following operation looks like this:
10 =>Empty string  
Hence, 0 is the length of the shortest string.

# Skill: Coding - Medium

# Tests

INPUT	        ACTUAL OUTPUT	EXPECTED OUTPUT
4 1011	            0	            0
3 000	            3	            3
1 1	                1	            1
1 0	                1	            1
2 11	            0	            0
2 10	            0	            2
