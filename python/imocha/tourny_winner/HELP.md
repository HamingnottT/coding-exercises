# Dynamic Programming: Tournament Winner

There are N players in the chess tournament. If a player loses a game, he is automatically eliminated from the tournament.
The tournament has established one rule:
Two players can only play against each other if the absolute difference between the number of games played by the players is always less than equal to 1.
Find the maximum number of games the winner of the tournament can take part in (assuming the above rule is used).
 
# Function Description
In the provided code snippet, implement the provided tournamentWinner(...) method using the variables to print the required maximum number of games that can be played by the winner. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.

There will be multiple test cases running so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.

# Input Format
The first line of input contains a single integer N, denoting the number of players to participate in the tournament.

# Sample Input
4                    -- denotes N
 
# Constraints
N <=1<=1018

# Output Format
The output contains a single integer denoting the maximum number of games that can be played by the winner.
 
# Sample Output
2
 
# Explanation
Player 1 can't play with another player as after he plays with players 2 and 3 he can't play against player 4, as he has played 0 games, while player 1 already played with player 2.
Thus, the answer is 2, and to achieve the maximum number of games that can be played we make pairs (1, 2) and (3, 4) and then clash the winners.