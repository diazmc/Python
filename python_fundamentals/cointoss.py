def cointoss():
    print "Starting program..."
    
    import random
    
    heads = 0
    tails = 0
    
    for att in range(1, 5001):
        flip = random.randint(1,2)
        if flip % 2 == 0: 
            heads += 1
            print "Attempt #",att,"Throwing a coin... It's a head...Got",heads,"head(s) so far and", tails, "tail(s) so far"

        else:
            tails += 1
            print "Attempt #",att,"Throwing a coin... It's a tail...Got",tails,"head(s) so far and", tails, "tail(s) so far"
cointoss()