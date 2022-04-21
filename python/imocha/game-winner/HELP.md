# Array: Game Winner

Alice and Bob are playing a game. The game has N sets and the player who wins more number of sets at the end of the game is declared as the winner.
You are given two arrays of integers A and B of size N where A consists of scores of Alice in respective sets and B consists of scores of Bob in respective sets.
For an element Ai in A and its corresponding element Bi in B, if Ai > Bi, Alice is the winner of the ith set, and if Ai < Bi, Bob is the winner of the ith set, and if Ai = Bi, the set is tied.
Print the winner of the game along with the number of sets they won, or print “tied”. 

# Function Description 
In the provided code snippet, implement the provided gameWinner(...) method using the variables to print the winner of the game or tied. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.   
There will be multiple test cases running so the Input and Output should match exactly as provided. 
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables. 
 
# Input Format 
The first line contains an integer N, denoting the number of sets. 
The second line contains an array of integers A.
The third line contains an array of integers B.

# Sample Input 
5                 -- denotes the N number of sets.
4 7 3 2 9     -- denotes the points scored by Alice A.
6 9 2 6 3     -- denotes the points scored by Bob B.

# Constraints 
1 <= N <= 105 
0 <= Ai <= 20
 
# Output Format 
The output contains a character A or B - the winner of the game - followed by the number of sets won by the winner or “tied” if the match is tied. 

# Sample Output 
B 3

# Explanation 
A1 = 4, B1 = 6 i.e. A1 < B1, hence B is the winner of set 1.
A2 = 7, B2 = 9 i.e. A2 < B2, hence B is the winner of set 2. 
A3 = 3, B3 = 2 i.e. A3 > B3, hence A is the winner of set 3. 
A4 = 2, B4 = 6 i.e. A4 < B4, hence B is the winner of set 4. 
A5 = 9, B5 = 3 i.e. A5 > B5, hence A is the winner of set 5.  
Hence, B is the winner of the game as he won 3 out of 5 sets.
Hence, the output is B 3.