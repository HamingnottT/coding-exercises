# Algorithms: Sorting Order

Given an array A of integers, sort the array such that : 
- All even numbers are sorted in increasing order.
- All odd numbers are sorted in decreasing order.
- The relative positions of the even and odd numbers remain the same.

## Function Description
In the provided code snippet, implement the provided  customSort(...) method using the variables to custom sort as per the question. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”. 

There will be multiple test cases running so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.

## Input Format
The first line contains an integer N.
The second line contains N space-separated integers of array A.

## Sample Input

5                   -- denotes N
2 8 13 21 6         -- denotes A[ ]

## Constraints
1 >= N <= 103
0 >= A[i] <= 103

## Output Format
The output contains space-separated customized sorted array A.

## Sample Output
2 6 21 13 8

## Explanation
In the output array, the even numbers are sorted in increasing order, odd numbers are sorted in decreasing order, and their relative positions are maintained.