# String Manipulation: Frequency

For a given string S, write a program to print the characters in their descending order of frequency of occurrence.
 
The frequency of occurrence is the number of times a character is repeated in a string.
For e.g. In the string banana,
The frequency of occurrence of b is 1.
The frequency of occurrence of a is 3.
The frequency of occurrence of n is 2.
 
# Note
All the characters of the string S are in lowercase.
If two characters have the same frequency, the character with lower precedence in alphabetical order is printed first. 

# Function Description
In the provided code snippet, implement the provided orderOfFrequencies(...) method using the variables to print a single string having the characters in the order of their frequency. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”. 

There will be multiple test cases running so the Input and Output should match exactly as provided.
The base output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.

# Input Format
The first line of input contains a string S.
 
# Sample Input
llljkgghi    -- denotes string S
 
# Output Format
The output contains a single string displaying the characters in the order of their frequency.
 
# Constraints
1 <= |S| <= 100 
 
# Sample Output
lghijk
 
# Explanation
The frequencies are:
l: 3,
g: 2,
h: 1,
i: 1,
j: 1, 
k: 1.
Hence, after sorting the characters of the string according to the frequency of occurrence, the output is lghijk.
# Skill: Coding - Easy

# Sample Input

INPUT	                ACTUAL OUTPUT	EXPECTED OUTPUT
llljkgghi	            ghijkl	        lghijk
aaabbbcccc	            abci	        cab
fhmc	                cfhm	        cfhm
qbb	                    biq	            bq
ezqlufq	                efilquz	        qefluz
rkokigumkvdrcd	        cdgikmoruv	    kdrcgimouv