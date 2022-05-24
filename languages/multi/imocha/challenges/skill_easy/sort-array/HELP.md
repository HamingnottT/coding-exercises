# Array: Sort Array

An array A of integers is given.
You need to sort the elements of the array by the number of digits present in them in ascending order, i.e. the elements with lesser no. of digits appear before the elements with greater no. of digits. 
Sort the array as specified and print the resulting array. 

## Note
The elements with the same number of digits should appear in the same order in which they appeared in the original array. 

## Function Description 
In the provided code snippet, implement the provided sortArray(...) method using the variables to print the resulting array. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.   

There will be multiple test cases running so the Input and Output should match exactly as provided. 
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables. 
 
## Input Format 
The first line contains an integer N.
The second line contains an array of integers.  

## Sample Input 
5                              -- denotes the size N of an array A.
9 10 122 8 1290      -- denotes the elements of an array A.

## Constraints 
1 <= N <= 105. 
1 <= Ai <= 109.  
 
## Output Format 
The output contains the sorted array according to the condition.  

## Sample Output 
9 8 10 122 1290 

## Explanation 
A1 = 9, number of digits = 1, 
A2 = 10, number of digits = 2, 
A3 = 122, number of digits = 3, 
A4 = 8, number of digits = 1, 
A5 = 1290, number of digits = 4. 
It can be seen that after sorting the elements by the number of digits present in them in ascending order, the sorted array will be: 
9 8 10 122 1290.
9 appears before 8 as it occurs before 8 in the input array. 
Hence, the obtained output is 9 8 10 122 1290.

# INPUT	                                                ACTUAL OUTPUT	                                                EXPECTED OUTPUT
5 9 10 122 8 1290	                                    [8, 9, 10, 122, 1290]	                                        9 8 10 122 1290
4 237 23 11121 82	                                    [23, 82, 237, 11121]	                                        23 82 237 11121
5 98 28 21 12 13	                                    [12, 13, 21, 28, 98]	                                        98 28 21 12 13
2 121 21	                                            [21, 121]	                                                    21 121
8 12 2839293 9384 8923 29 2938 39238239 19209112	    [12, 29, 2938, 8923, 9384, 2839293, 19209112, 39238239]	        12 29 9384 8923 2938 2839293 39238239 19209112
1 273	[273]	273