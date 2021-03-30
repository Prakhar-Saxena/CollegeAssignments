
cardValues = [1, 2, 3, 4]

# hand is a list

hand1 = []
hand2 = []

def whoWon(hand1, hand2):
    if sum(hand1) > 4 and sum(hand2) > 4:
        return None
    if sum(hand1) > 4 and sum(hand2) <= 4:
        return 2
    if sum(hand1) <= 4 and sum(hand2) > 4:
        return 1
    if sum(hand2) < sum(hand1) <= 4:
        return 1
    elif sum(hand1) < sum(hand2) <= 4:
        return 2
    else:
        return None

def initialise()