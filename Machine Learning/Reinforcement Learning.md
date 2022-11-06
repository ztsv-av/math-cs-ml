# Reinforcement Learning

Reinforcement learning is a machine learning training method based on rewarding desired behaviors and/or punishing undesired ones. In general, a reinforcement learning agent is able to perceive and interpret its environment, take actions and learn through trial and error.

In reinforcement learning, you tell an algorithm **what** to do, instead of how to do it with the help of a reward function.

For example, think of an autonomous helicopter. The reward function is going to look something like this:
- positive reward: helicopter flying well $+1$;
- negative reward: helicopter flying poorly/crushes $-1000$.

## Terminology

- $s=$ state.
- $a=$ action.
- $R(s)=$ *immediate reward* = reward associated with state $s$.
- $s'=$ state you get after taking action $a$.
- $a' =$ action you take in state $s'$.
- $\gamma =$ discount factor, describes patience of an algorithm.
- $R_t =$ terminal state - state where an algorithm gets a reward, but nothing happens after that. For example, states 1 and 6 are terminal states.

![image](https://user-images.githubusercontent.com/73081144/199886789-21ed03d7-c519-4490-be16-83c15cfc476c.png)

*Fig. 1. Terminal state examples.*

- Markov Decision Process (MDP) - MDP states that the future only depends on the current state and not on anything that might have occurred prior to getting to the current state.

## The Return

The Return in reinforcement learning allows algorithm to understand which particular set of rewards is better or worse than different set of rewards. Based on the return value, your algorithm will know which action to take.

Return function:

$$return = R_1 + \gamma R_2 + \gamma^2R_3 + ... + \gamma^{t - 1}R_t$$

, where

- $R_n =$ reward at state $n$;
- $\gamma =$ discount factor.

Common choice for discount factor $\gamma$ is usually pretty close to $1$, like $0.9, 0.99, 0.999$, etc.

![image](https://user-images.githubusercontent.com/73081144/199888571-1ebac6d8-c4c7-4556-b4bb-5a12a70b65fb.png)

*Fig. 2. Example of the return.*

Negative rewards cause the algorithm to push out negative rewards as far into the future as possible.

## Policy

In reinforcement learning, our goal is to come up with a function which is called a policy $\pi$, whose job it is to take as input any state $s$ and map it to some action $a$ that it wants us to take to **maximize the return**.

For example, in figure below the policy will tell us to go left if we are in states 1,2,3,4, because the reward is greater. If we are in states 5 and 6, then the policy will tell us to go right. So, policy maps every state to an action to maximize the return.

![image](https://user-images.githubusercontent.com/73081144/199889126-55466b01-7ae3-4f26-8e17-243cf8236f59.png)

*Fig. 3. Policy explained.*

## State-action Value Function | Optimal $Q$ Function

State-action value function $Q(s,a) = Q^* =$ optimal $Q$ function $=$ *max return* if you:

- start in state $s$;
- take action $a$ (once);
- then behave optimally after that (actions that will result in highest possible return).

Example:

|   Reward   | 100 | 0 | 0 | 0 | 0 | 40 |
| ---------- | --- | - | - | - | - | -- |
| State $s$  |  1  | 2 | 3 | 4 | 5 | 6  | 

$Q(2, <=) = 0 + \gamma * 100 = \gamma * 100$

$Q(2, =>) = 0 + \gamma * 0 + \gamma^2 * 0 + \gamma^3 * 100 = \gamma^3 * 100$ (go right, left, left, left, since going left is still better then going right all the way down to the terminal state)

$Q(4, <=) = 0 + \gamma * 0 + \gamma^2 * 0 + \gamma^3 * 100 = \gamma^3 * 100$

Thereby, the best possible *return* from state $s$ is $max_aQ(s,a)$ ($Q(4, <=) = 12.5 > Q(4, =>) = 10$)

The best possible action in state $s$ is the action $a$ that gives $max_aQ(s,a)$

$\pi(s) = a = max_aQ(s,a)$

In some sence, building a table with optimal $Q$ function values (each state going right and left) is a recursive function.

## Bellman Equation

Bellman equation helps to compute the state-action value function $Q(s,a)$.

$$Q(s,a) = R(s) + \gamma max_{a'}Q(s', a')$$

, where

- $R(s) =$ immediate reward;
- $\gamma max_{a'}Q(s', a') =$ return from behaving optimally starting from state $s'$.

## Random (stochastic) Environment

Stochatic environment is an environment where actions you take have a probability where the result of that action is not what you expect it to be. For example, if you go left, you have 90% of succeeding (going left) and 10% of perfoming another action, like going right or slippering.

So, in a stochastic reinforcement learning problem, what we're interested in is not maximizing the return because that's a random number. What we're interested in is maximizing the average value of the sum of discounted rewards. By average value, we mean if you were to take your policy and try it out a thousand times or a 100,000 times or a million times, you get lots of different reward sequences and if you were to take the average over all of these different sequences of the sum of discounted rewards, then that's what we call the expected return.

Then, the return function is going to change to:

$$expected \space return = avg(R_1 + \gamma R_2 + \gamma^2R_3 + ... + \gamma^{t - 1}R_t) = E[R_1 + \gamma R_2 + \gamma^2R_3 + ... + \gamma^{t - 1}R_t]$$

And Bellman equation:

$$Q(s,a) = R(s) + \gamma E[max_{a'}Q(s', a')]$$

The higher the misstep probability, the lower the $Q(s,a)$ at each state.

*Funny fact: if the misstep probablity is $>0.5$, it is actually better to go the opposite direction you would normally go.*

## Continious State Spaces

Most system can be in continious number of states/positions (such as system location). 

For example, for a car, the state might include 6 numbers: $x$ position, $y$ position, $\theta$ orientation (where it faces), $\dot{x}$ how quickly $x$ coordinate changing, $\dot{y}$ how quickly $y$ coordinate changing, $\dot{\theta}$ how quickly angle of a car changing. Each number here can take any value of a valid number range.

For an autonomous helicopter, we will have 12 numbers associating the state of the system: $x, y, z,$ $\phi$ (row), $\theta$ (pitch), $\omega$ (yaw), $\dot{x}, \dot{y}, \dot{z}, \dot{\phi}, \dot{\theta}, \dot{\omega}$.

## Applications

Reinforcement learning has been applied in:
- controlling robots;
- factory optimization;
- financial (stock) trading;
- playing games.
 