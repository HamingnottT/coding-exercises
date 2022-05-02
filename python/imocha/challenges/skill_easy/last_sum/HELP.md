# Recursion: Last Sum

Given N numbers, print the sum of the last digits of all the numbers using recursion.
Since the sum can be very large, print its modulo 109 + 7.  

# Function Description 
In the provided code snippet, implement the provided lastSum(...) method to print the sum of the last digits of all numbers. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.
  
There will be multiple test cases running so the Input and Output should match exactly as provided. The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.  

# Input Format
The first line contains N.
The second line contains N space-separated integers.

# Constraints
0 <= N <= 105
0 <= Each number <= 1018

# Sample Input
3                       -- denotes number of elements N.
123 324 2133   -- denotes N space separated integers.

# Output Format 
The output contains the sum of the last digits of the N numbers.
  
# Sample Output 
10  

# Explanation 
The last digit of 123 is 3.
The last digit of 324 is 4.
The last digit of 2133 is 3.
Hence, the output is (3+4+3)%109 + 7 = 10.


# Skill: Coding - Easy

INPUT	                                                                                                                ACTUAL OUTPUT	                EXPECTED OUTPUT
3 123 324 2133	                                                                                                            10	                                10
4 1 1223 324 2133	                                                                                                        11	                                11
4 12 1223 324 2133	                                                                                                        12	                                12
10 1804289383 846930886 1681692777 1714636915 1957747793 424238335 719885386 1649760492 596516649 1189641421	            47	                                47
3 1901802457 864293623 1495873484	                                                                                        14	                                14
4 606244339 574633330 1253247853 441236111	                                                                                13	                                13