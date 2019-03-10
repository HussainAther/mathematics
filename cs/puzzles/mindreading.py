
"""
You are a Magician and a Mind Reader Extraordinaire. The Assistant goes into the
audience with an authentic deck of 52 cards while you are outside the room and can’t
possibly see anything. Five audience members each select one card from the deck. The
Assistant then gathers up the five cards. The Assistant shows the entire audience four
cards, one at a time. For each of these four cards, the Assistant asks the audience to
mentally focus on the card, while you look away and try to read their collective minds.
Then, after a few seconds you are shown the card. This helps you calibrate your mind
reading to the particular audience.

After you see these four cards, you claim that you are well calibrated to this audience and
leave the room. The Assistant shows the fifth card to the audience and puts it away.
Again, the audience mentally focuses on the fifth card. You return to the room,
concentrate for a short time and correctly name the secret, fifth card!

You are in cahoots with your Assistant and have planned and practiced this trick.
However, everyone is watching closely and the only information that the Assistant can
give you is the four cards.

How does this trick work?

It turns out that the order in which the Assistant reveals the cards tells the Magician what
the fifth card is! The Assistant needs to be able to decide which of the cards is going to be
hidden – he or she cannot allow the audience to pick the hidden card out of the five cards
that the audience picks. Here’s one way that the Assistant and the Magician can work
together.
"""

deck = ['A_C', 'A_D', 'A_H', 'A_S', '2_C', '2_D', '2_H', '2_S', '3_C', '3_D', '3_H', '3_S',
        '4_C', '4_D', '4_H', '4_S', '5_C', '5_D', '5_H', '5_S', '6_C', '6_D', '6_H', '6_S',
        '7_C', '7_D', '7_H', '7_S', '8_C', '8_D', '8_H', '8_S', '9_C', '9_D', '9_H', '9_S',
        '10_C', '10_D', '10_H', '10_S', 'J_C', 'J_D', 'J_H', 'J_S',
        'Q_C', 'Q_D', 'Q_H', 'Q_S', 'K_C', 'K_D', 'K_H', 'K_S']

def outputFirstCard(numbers, oneTwo, cards):
    """
    This procedure figures out which card should be hidden based on the distance
    between the two cards that have the same suit.
    It returns the hidden card, the first exposed card, and the distance
    """
    
