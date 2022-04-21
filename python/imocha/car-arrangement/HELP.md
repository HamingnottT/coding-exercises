# Array Operations: Car Arrangement

You have visited a shopping mall that has a very long parking space. 
It has N continuous parking lots available, in which some parking lots are occupied and some are empty. However, cars cannot be parked in adjacent parking lots. 
You are given an integer array containing 0 and 1 where 0 means the parking lot is empty and 1 means the parking lot is not empty. 

Print the maximum number of new cars that can be parked in a given arrangement without violating conditions and the total number of cars after parking the new cars.   

# Note
Each parking lot can contain only one car, and you cannot move an already parked car.
Two cars cannot be parked in adjacent parking lots. 

# Function Description
In the provided code snippet, implement the provided carArrangement(...) method using the variables to print the two space-separated integers representing the maximum number of new cars that can be parked in a given arrangement without violating conditions and total numbers of cars after parking the new cars on a single line. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”. 

There will be multiple test cases running so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.

# Input Format 
The first line contains a single integer N.
The second line contains N space-separated integers, either 0 or 1. 

# Constraints 
3 <= N <= 100000. 
  
# Sample Input 1
3          -- denotes the total number of parking lots N
0 0 0    -- denotes initial arrangements of cars.
 
# Output Format
The output contains two space-separated integers representing the maximum number of new cars that can be parked in a given arrangement without violating conditions and the total number of cars after parking the new cars on a single line.
 
# Sample Output
2 2 

# Explanation 
N = 3 
Array: [0,0,0] 
In the given arrangement, initially, no cars are parked in the parking lot.
We can park the car at the 0th index as well as the 2nd index so that no two cars are adjacent to each other. 
Thus, a maximum of 2 new cars can be parked in a given arrangement and the total car count becomes 2.
Hence, the answer is 2 2.