# Queue: Minimum Cost of Contiguous Sub Arrays

You are given an array of N elements.
You have to split the array into M subarrays.
The cost you have to pay to make a subarray is the addition of two values at the two corners. 
Formally, a subarray Ai, Ai+1, … Aj costs (Ai + Aj).
The total cost is the addition of all individual subarray costs.

For a given value of M, find the minimum cost you need to pay to split the array into M subarrays.
 
# Note
Subarray is a contiguous part of the array.
Contiguous subarrays of [1,2,3,4] are [1], [2], [3], [4], [1,2], [2,3], [3,4], [1,2,3], [2,3,4], [1,2,3,4].
Each element must be a part of any 1 subarray.
Subarrays can also be of size 1.

# Example
If the given array is [1, 2, 3, 4] and M = 2
We get subarrays [1, 2] and [3,4]
The cost will be the addition of two values at the two corners of every sub-array.
Cost of 1st sub array= 1+2 = 3
Cost of 2nd sub array= 3+4 = 7
The total cost will be 3+7 = 10.

# Function Description
In the provided code snippet, implement the provided minimumCost(...) method using the variables to return a single integer denoting the minimum cost you need to pay. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”. 

There will be multiple test cases running so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.

# Input Format
The first line contains two space-separated integers, N and M.
The next line contains N space-separated integers denoting the array elements.

# Sample Input
3 1       -- denotes N & M
1 2 3    -- denotes N elements of the array

# Output Format
The output contains a single integer denoting the minimum cost you need to pay.

# Sample Output
4
 
# Explanation
We need to split the array into 1 subarray.
As the array is already 1 block, we don’t need to split it at all. So the solution is simply the cost of the array as a whole i.e. 1+3 = 4.
Hence, the output is 4.