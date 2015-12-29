#paper,rock, scissors

player1 = raw_input('player1?')
player2 = raw_input("player2?")
VALID_INPUT = ['paper','rock','scissors']
WINNING_COMBO = [['paper','rock'],['rock','scissors'],['scissors','paper']]


def valid_input(inp):
    if inp in VALID_INPUT:
        return True
    else:
        return False

def rps(player1,player2):
    if valid_input(player1) and valid_input(player2):
        if player1 == player2:
            return 'Tie game'
        elif ([player1,player2] in WINNING_COMBO):
            return 'player1 win'
        else:
            return 'player2 win'
    else:
        print "enter a valid option"


print rps(player1,player2)