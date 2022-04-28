# Recursion: Minimum Cost

Alex has N chocolates. Each chocolate can be taken as full or can be taken half a fraction (X/2) or can be ignored.
Alex has a chocolate array A, and a cost array B.  ith element of this array A determines the amount of  ith chocolate (in kg) and cost array "cost" which determines the cost of i’th (1=i<=N) chocolate.
The cost of the half fraction of chocolate is the ceil value of the cost of full chocolate when divided by 2.
For example, if the cost of the full chocolate is 11, then the cost of half chocolate is 6.
Bob wants to buy at least X kg of chocolate from Alex.
Find the minimum cost that Bob needs to spend so that he can buy at least X kg of chocolate. 

# Note
Ceil(a,b) is the integer value when (a/b) is rounded off to next integer.
It is guaranteed that the value of X doesn't exceed the sum of the total amount of chocolate. 
Alex can choose 1 chocolate only once. 

# Function Description
In the provided code snippet, implement the provided getMinCost(...) method using the variables to print the pattern for each line from 1 to i.
You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.  
 
There will be multiple test cases running so the Input and Output should match exactly as provided. 
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables. 

# Input Format
The first line contains N and X. 
The second line contains the chocolate array. 
The third line contains the cost array. 

# Sample Input

3 5      => N,X 
1 2 3   => Chocolate Array 
4 5 6   => Cost Array  

# Constraints
1<=N<=10 
1<=X<=1000 
1<=cost[i]<=1000 
1<=chocolate[i]<=1000 

# Output Format 
The output contains a single integer denoting the minimum cost. 
 
# Sample Output 
11 

# Explanation 
Bob needs to buy at least 5kgs.
So we have 1kg, 2kg, 3kg these 3 types of chocolates
So to buy 5 kg we have the following choices:
1)Take 5 chocolates of 1kg will cost 5*(cost of 1kg type) = 5*4 = 20 units
2)Take 2kg and 3 kg type. So cost in this case will be cost of 2 + cost of 3 = 5 + 6 = 11 units
Similarly among all the possible ways, 11 is the minimum cost which we can get.
Hence the output is 11.