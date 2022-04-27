# Array Operations: Trips Required

There are N cities and each city has A[i] number of people.
You have to take the people to a safe-house via a helicopter.
The helicopter has the capacity of carrying only K people at a time.

Find the minimum number of trips the helicopter will need to make to take all the people from all the cities to the safe-house.

# Note 
You are allowed to fill the helicopter from different cities on one trip.

# Function Description
In the provided code snippet, implement the provided tripsRequired(...) method using the variables to print the minimum number of trips the helicopter needs to make. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”. 

There will be multiple test cases running so the Input and Output should match exactly as provided.
The base output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.
 
# Input Format
The first line contains a single integer N, denoting the size of the array.
The second line contains a single integer K.
Next N lines contain an integer A[i].
 
# Sample Input
5     -- denotes N
3     -- denotes K
1     -- denotes A[0]
4     -- denotes A[1]
1     -- denotes A[2]
3     -- denotes A[3]
2     -- denotes A[4]

# Contraints
1 <= N, K <= 105
1 <= A[i] <= 105

# Output Format
The output contains a single integer denoting the minimum number of trips the helicopter needs to make.
 
# Sample Output
4
 
# Explanation
The given array is {1,4,1,3,3} and capacity K = 3.
On the first trip: 1 person from city1 and 2 people from city2.
On the second trip: the remaining 2 people from city2 and 1 from city3.
On the third trip: all 3 people from city4.
On the fourth trip: all 2 people from city5.
Hence, the minimum trips required are 4.