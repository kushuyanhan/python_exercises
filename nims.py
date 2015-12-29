# Name:
# Section:
# nims.py


def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''

    ## Basic structure of program (feel free to alter as you please):

#    while [pile is not empty]:
#        while [player 1's answer is not valid]:
#            [ask player 1]
#            [execute player 1's move]
#
#        while [player 2's answer is not valid]:   
#            [ask player 2]
#            [execute player 2's move]
#
#    print "Game over"
    is_input_valid = False
    current_player = 0 #keep track of current player
    #current_player % 2 == 0 player1
    #current_player % 2 == 1 player2
    #if there are 4 players, %4

    while pile > 0:
        is_input_valid = False
        while is_input_valid == False:

            take_stones = raw_input("enter the number(must 1 to max_stones inclusive) of stones you want to take:")
            if not take_stones.isdigit():
                continue
            if int(take_stones) >= 1 and int(take_stones) <= max_stones and int(take_stones) <= pile:

                current_player += 1
                is_input_valid = True
                pile -= int(take_stones)
                #print 'pile is', pile,'current_player is', current_player%2


    if pile == 0:
        print 'the winner is'
        print current_player
        if current_player % 2 == 1:
            print 'player1'
        else:
            print 'player2'



play_nims(5,2)





