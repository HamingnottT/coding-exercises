def tournamentWinner(N):
    # this is default OUTPUT. You can change it.
    
    def test1():
        players = []
        num_winners_tally = 0
        for i in range(0, (N+1)):
            players.append(i%2)         # because there can only be one winner per pair

        for i in range(0, len(players)):
            num_winners_tally += players[i]
        
        return num_winners_tally
        
    result = test1()

    # DEBUG: show raw output
    # result = N

    return result


# INPUT [uncomment & modify if required]
N = int(input())

# OUTPUT [uncomment & modify if required]
print(tournamentWinner(N))