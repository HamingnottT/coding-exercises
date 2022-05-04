# Strings: New String

You are given a string S.
You have to form a new string t which is formed from S only.
To form the string t, initially, you have to make string t equal to string S. Then, one by one, remove all occurrences of one letter from S.
The order in which you will remove letters should be alphabetical. Append the remaining part of string S to string t in every iteration. 
Print the new string t formed after all the iterations.

# Function Description
In the provided code snippet, implement the provided newString(...) method using the variables to print the new string. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.

There will be multiple test cases running so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.

# Input Format
The only line of input contains a string S.

# Sample Input
ababc    -- denotes S
 
# Constraints
1<=|S|<=105

# Output Format
The output contains the string t.

# Sample Output
ababcbbcc
 
# Explanation
S = ababc
t = ababc
We remove a from S so S becomes bbc. We will append it to t.
t = ababcbbc
We will remove b from S so S = c
t = ababcbbcc
This t is our final string.
# Skill: Coding - Easy

# Sample Input: 

NPUT	        ACTUAL OUTPUT	EXPECTED OUTPUT
ababc	        []	               ababcbbcc
abc	            []	               abcbcc
xxyyzz	        []	               xxyyzzyyzzzz
friends	        []	               friendsfriensfrinsrinsrnsrss
office	        []	               officeoffieoffioio
messi	        []	               messimssimssss