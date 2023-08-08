# Bayes' Theorem

Bayes' theorem is a fundamental concept in probability theory that allows us to calculate the probability of a hypothesis given some observed evidence. It is named after Reverend Thomas Bayes, an 18th-century British statistician and theologian who first formulated the theorem.

Bayes' theorem states that the probability of a hypothesis H given some observed evidence E can be calculated as:

$$P(H | E) = \frac{P(E | H) * P(H)}{P(E)}$$

where:

- $P(H | E)$ is the posterior probability of the hypothesis H given the evidence E
- $P(E | H)$ is the likelihood of observing the evidence E given the hypothesis H
- $P(H)$ is the prior probability of the hypothesis H (i.e., the probability of H before observing any evidence)
- $P(E)$ is the probability of observing the evidence E (i.e., the probability of E under all possible hypotheses)

Bayes' theorem is widely used in fields such as statistics, data analysis, and machine learning to update our beliefs about a hypothesis based on new evidence.

## Example

In the sports injuries unit of a hospital, 40% of the patients are rugby players, 20% are swimmers
and the remaining 40% play soccer. For a rugby player, the probability to be released on the first day is 10%; for
a swimmer, it is 20%; for a soccer player, it is 80%.

Given a patient is released on the first day, the probability of her/him being a soccer player is 80%. Proof: 

$P(soccer|release) = P(release|soccer) ∗ P(soccer)/P(release) = \frac{0.8·0.4}{0.4} = 0.8$
