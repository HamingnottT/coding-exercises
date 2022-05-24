# Array Operations: Reorder

You are given integer 'N'. 

You are given array 'arr' of 'N' integers.
Let's call a pair of indices i, j good if 1<=i<j<=N (1-indexing) and 
gcd(arr[i],2*arr[j])>1. 

The gcd(x,y) is the greatest common divisor of x and y). 

Find the maximum number of good index pairs if you can reorder the array 'arr' in an arbitrary way. 

# Function Description
In the provided code snippet, implement the provided reorder(...). method.
You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.
There will be multiple test cases running so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.

# Input Format
First line contains an integer N.
Second line contains N space-separated integers of arr.  

# Sample Input
4            -- denotes N
3 6 5 3   -- denotes arr[]

# Constraints
1 <= N <= 2000
1 <= arr[i] <= 10^5

# Output Format
The output should return the minimum and maximum amount of money you have to pay to buy all items by using special offer.

# Sample Output
4

# Explanation
For sample testcase N = 4 and arr = {3,6,5,3}
One of the order {6,3,3,5} will give maximum good index pairs i.e. 4.
Good index pairs - (1,2), (1,3), (1,4), (2,3).
So answer is 4.
Note: There may be another order of array but 4 is the maximum number of good index pairs.
 
# Skill: Coding - Medium

# Sample input:

INPUT	                                                                                                                        ACTUAL OUTPUT	    EXPECTED OUTPUT
4 3 6 5 3	                                                                                                                    3	                    4
5 1 4 2 4 1	                                                                                                                    6	                    9
2 1 7		                                                                                                                    0                       0
33 27 49 32 95 100 20 58 39 92 30 67 89 58 81 100 66 73 29 75 81 70 55 18 28 7 35 98 52 30 11 69 48 84	                        496	                    433
4 54 13 14 15	                                                                                                                3	                    5
7 86 34 82 92 26 8 53	                                                                                                        15	                    21