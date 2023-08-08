# The Law of Total Probability

The Law of Total Probability is a fundamental concept in probability theory that describes how to calculate the probability of an event by considering all possible ways in which the event can occur. It is also known as the Law of Total Probability or the Partition Theorem.

The Law of Total Probability states that if we have a sample space S and a set of events $B_1, B_2, ..., B_n$ that partition S (meaning that they are mutually exclusive and their union is S), then the probability of any event A can be expressed as the sum of the probabilities of A given each of the possible outcomes of the partition events:

$$P(A) = P(A | B1)P(B1) + P(A | B2)P(B2) + ... + P(A | Bn)P(Bn)$$

In other words, the law of total probability tells us that to find the probability of an event A, we can break down the sample space into mutually exclusive events, and calculate the probability of A given each of those events, weighted by the probability of each event occurring.

## Example

In the sports injuries unit of a hospital, 40% of the patients are rugby players, 20% are swimmers
and the remaining 40% play soccer. For a rugby player, the probability to be released on the first day is 10%; for
a swimmer, it is 20%; for a soccer player, it is 80%.

The probability that a patient is released on the first day can be calculated with the law of total probability: 0.4 · 0.1 + 0.2 · 0.2 + 0.4 · 0.8 = 0.4.
