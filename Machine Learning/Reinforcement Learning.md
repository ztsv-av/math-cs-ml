# Reinforcement Learning

Reinforcement learning is a machine learning training method based on rewarding desired behaviors and/or punishing undesired ones. In general, a reinforcement learning agent is able to perceive and interpret its environment, take actions and learn through trial and error.

In reinforcement learning, you tell an algorithm **what** to do, instead of how to do it with the help of a reward function.

For example, think of an autonomous helicopter. The reward function is going to look something like this:
- positive reward: helicopter flying well $+1$;
- negative reward: helicopter flying poorly/crushes $-1000$.

## Terminology

- $s=$ state.
- $a=$ action.
- $R(s)=$ reward associated with state $s$.
- $s'=$ next state.
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

## Applications

Reinforcement learning has been applied in:
- controlling robots;
- factory optimization;
- financial (stock) trading;
- playing games.
 