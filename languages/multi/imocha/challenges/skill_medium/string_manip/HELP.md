# String Manipulation

There are two strings A and B of unequal length.
Strings should be made the same by deleting a sub-string from the larger string.

Write a program to check if the strings can be made equal by deleting sub-strings.
- If Yes, print the number of ways in which the strings can be made equal.
- If No, print 0.

# Note
If the string is divided into two parts, then the two parts get concatenated. e.g. after deleting "xy" from "axyb", the remaining string becomes "ab".
Two ways are considered different if the sub-strings deleted in them are different.

# Function Description
In the provided code snippet, implement the provided subString(...) method using the variables to print a single integer denoting the number of ways in which the strings can be made equal. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”. 

There will be multiple test cases running so the Input and Output should match exactly as provided.
The base output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.

# Input Format
The first line of input contains string A.
The second line of input contains string B.
  
# Sample Input
acbegdbd   -- denotes A
acbd           -- denotes B
 
# Output Format
The output contains a single integer denoting the number of ways in which the strings can be made equal.
 
# Sample Output
2

# Explanation
There are 2 ways in which the strings can be made equal.
FIRST-> by deleting the substring "begd"
SECOND-> by deleting the substring "egdb"
Hence, the output is 2.