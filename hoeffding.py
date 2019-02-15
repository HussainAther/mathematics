import sympy
import sypy.stats as ss


"""
Hoeffding’s Inequality is similar, but less loose, than Markov’s Inequality. Let X1,...,Xn be iid observations
such that E(Xi) = μ and a ≤ Xi ≤ b. Then, for any ε > 0, we have:

P(|Xn − μ| ≥ ε) ≤ 2 exp(−2nε2/(b − a)2)

Corollary: If X1,...,Xn are independent with P(a≤Xi ≤b) = 1 and all with
E(Xi ) = μ. Then, we have

|Xn−μ| ≤ sqrt((c/2n)(log2/δ))

where c = (b−a)2. We will see this inequality again in the machine learning chapter. Figure 2.23 shows the Markov and
Hoeffding bounds for the case of ten identically and uniformly distributed random variables, X i ∼ U [0, 1].
The solid line shows P(|Xn − 1/2| > ε). Note that the Hoeffding Inequality is tighter than the Markov Inequality and
that both of them merge when ε gets big enough.
"""
