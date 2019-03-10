
"""
Solving without import.

You are tasked with determining the “hardness coefficient” of a set of identical crystal
balls. The famous Shanghai Tower completed in 2015 has 128 floors, and you have to
figure out from how high you can drop one of these balls so it doesn’t break but rather
bounces off the ground below. We will assume that the surrounding area has been
evacuated while you conduct this important experiment.

What you have to report to your boss is the highest floor number of the Shanghai Tower
from which the ball does not break when dropped. This means that if you report floor f,
the ball does not break at floor f, but does break at floor f + 1. Else you would have
reported f + 1. Your bonus depends on how high a floor you report, and if you report a
floor f from which the ball breaks, you face a stiff fine, which you want to avoid at all
costs.

Once a ball breaks, you can’t reuse it again, but you can if it does not break. Since the
ball’s velocity as it hits the ground is the sole determining factor as to whether it breaks
or not, and this velocity is proportional to the floor number, you can assume that if a ball
does not break when dropped from floor x, it will not break from any floor whose number
< x. Similarly, if it breaks when dropped from floor y, it will break when dropped from
any floor whose number > y.

Sadly, you are not allowed to take an elevator because the shiny round objects you are
carrying may scare off other passengers. You would therefore like to minimize the
number of times you drop a ball, since it is a lot of work to keep climbing up stairs.

Of course, the big question is how many balls do you have to play with? Suppose you are
given exactly one ball. You don’t have much freedom to operate. If you drop the ball
from floor 43, say, and it breaks, you don’t dare report floor 42, because it might break
when dropped from floor 42, floor 41, or floor 1 for that matter. You will have to report
floor 1, which means no bonus. With one ball, you will have to start with floor 1 and if
the ball breaks, report floor 1, and if it does not you move up to floor 2, all the way till
floor 128. If it doesn’t break at floor 128, you happily report 128. If the ball breaks when
dropped from floor f, you will have dropped the ball f times. The number of drops could
be as large as 128, floors 1 through 128 inclusive.

What if you have two balls? Suppose you drop one ball from floor 128. If it does not
break, you report floor 128 and you are done with the experiment and rich. However, if it breaks,
you are down to one ball and all you know is that the balls you are given
definitely break at floor 128. To avoid a fine and to maximize your bonus, you will have
start with the second ball at floor 1 and move up as described earlier possibly all the way
up to floor 127. The number of drops in the worst case is 1 drop (from floor 128) plus
drops from floors 1 through 127 inclusive, a total of 128. No improvement from the case
of one ball.

Intuition says that you should guess the midpoint of the interval [1, 128] for the 128-floor
building. Suppose you drop a ball at floor 64. There are two cases as always:

1. The ball breaks. This means that you can focus on floors 1 through 63, i.e.,
interval [1, 63] with the remaining ball.

2. The ball does not break. This means that you can focus on floors 65 through 128,
i.e., interval [65, 128] with both balls.

The worst-case number of drops is 64 because in Case 1 you will need to start with the
lowest floor in the interval and work your way up. Better than 128 but only by a factor of
two.

You would like to do better than the worst case of 64 drops when you have two balls.
You don’t want to give up any part of your bonus, and a fine is a no-no.

Can you think of a way to maximize your bonus and avoid a fine while using no more
than 21 drops in the case of two balls? What if you had more balls or what if the
Shanghai Tower suddenly doubled in size in terms of number of floors?

We should be able to do better than 64 drops. The problem with beginning with floor 64
when we only have two balls is that if the first ball breaks, we have to start with floor 1
and go all the way to floor 63. What if we started at floor 20? If the first ball breaks, we
have to search the smaller interval [1, 19] with the second ball one floor at a time. That is
20 drops total in the worst case. If the first ball does not break, we search the large
interval [21, 128] but we have two balls. Let’s next go to floor 40 and drop the first ball
(second drop of the first ball). If the first ball breaks we search [21, 39] one floor at a
time. This is, in the worst case, a total of 2 drops for the first ball (at floors 20 and 40)
and 19 drops of the second ball for a total of 21. Onto floor 60 and so on. Trying floors
20, 40, 60, 80, etc., is going to get us a worst-case solution of less than 30 drops for sure. 
"""
