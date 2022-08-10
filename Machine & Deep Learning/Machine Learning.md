# Machine Learning

Machine learning - field of study that gives computers the ability to learn without being explicitly programmed (Andrew Samuel).

## Types of Machine Learning

- Supervised learning: algorithms that learn input to output mapping (Input(X) -> Output(Y)). In this type of learning, you give your algorithm examples to learn from that include correct labels for a particular input. For example, you might provide your algorithm with AD and USER INFO data and get CLICK (0/1) probability (used in online advertising).

- Unsupervised learning: in this type of learning, we are given data that is not associated with any output labels Y. In other words, data only comes with inputs X, but not output labels Y. The job here is to find some structure, pattern, or just something interesting about the unlabeled data.

- Recommender systems:

- Reinforcement learning: 

## Terminology

- Training set: data used to train the model. Usually consists of features and targets (supervised learning).
- x: "input" variable; feature.
- y: "output", "target" variable.
- m: number of training examples;
- (x,y): single training example.
- $(x^i, y^i)$: $i^{th}$ training example.
- cost function: error, measurment of how a prediction is distant from the truth value.

## Applications

### Supervised Learning

| Input(X) | Output(Y) | Application |
| -------- | --------- | ----------- |
| email | spam?(0/1) | spam filtering |
| audio | text transcripts | speech recognition |
| English | Spanish | machine translation |
| ad, user info | click?(0/1) | online advertising |
| image, radar info | position of other cars | self-driving car |
| image of phone | defect?(0/1) | visual inspection |

### Unsupervised Learning

| Input(X) | Output(Y) | Application |
| -------- | --------- | ----------- |
| DNA of an individual | - | **clustering** DNA data |
| customer data | - | **clustering** into different market segments |
| news articles | - | **clustering** into sets of articles about the same story |
| transcations | - | **anomaly detection** |
