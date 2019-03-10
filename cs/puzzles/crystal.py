
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
"""
