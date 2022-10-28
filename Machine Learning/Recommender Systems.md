# Recommender Systems

A recommender system, or a recommendation system (sometimes replacing 'system' with a synonym such as platform or engine), is a subclass of information filtering system that provide suggestions for items that are most pertinent to a particular user. In a very general way, recommender systems are algorithms aimed at suggesting relevant items to users (items being movies to watch, text to read, products to buy or anything else depending on industries).

In the typical recommender system, you have some number of users as well as some number of items (e.g. movies). You might as well have features related to those items (e.g. how much a movie related to romance, action, etc. genres)

![image](https://user-images.githubusercontent.com/73081144/197675433-0c333adc-a344-4bb8-a285-75db5301df5b.png)

*Fig. 1. Recommendation task: movies.*

To predict user's $j$ rating, use **linear regression** model:

$$\hat{y}^{(j)} = w^{(j)} * x^{(i)} + b^{(j)}$$

## Cost function

Notation:

- $r(i, j) = 1$ if user $j$ has rated movie $i$ (0 otherwise);
- $y^{(i, j)} =$ rating given by user $j$ on movie $i$ (if defined);
- $w^{(j)}, b^{(j)} =$ parameters for user $j$;
- $x^{(i)} =$ feature vector for movie $i$;
- $m^{(j)} =$ number of movies rated by user $j$;
- $n =$ number of features.

For user $j$ and movie $i$, predict rating: $w^{(j)} * x^{(i)} + b^{(j)}$

To learn $w^{j}, b^{j}$ for a single user use **Mean Squared Error**:

$min_{w^{(j)}b^{(j)}}J(w^{(j)}, b^{(j)}) = \frac{1}{2m^{(j)}}\sum_{i:r(i,j)=1}(w^{(j)} * x^{(i)} + b^{(j)}-y^{(i, j)})^2  + \frac{\lambda}{2m^{(j)}}\sum_{k=1}^n(w_k^{(j)})^2$

You might remove $m^{(j)}$ term. It a constant and it does not affect cost function much.

So, overall cost function for all users looks like this:

$$J(w^{(1)}, ..., w^{(n_u)}, b^{(1)}, ..., b^{(n_u)}) = \frac{1}{2}\sum_{j=1}^{n_u}\sum_{i:r(i,j)=1}(w^{(j)} * x^{(i)} + b^{(j)}-y^{(i, j)})^2  + \frac{\lambda}{2}\sum_{j=1}^{n_u}\sum_{k=1}^n(w_k^{(j)})^2$$

The difference between simple linear regression model is that now we train different linear regression unit for each user.

## Collaborative Filtering Algorithm

Collaboratiove filtering algorithm is used to  **learn** **parameters** as well as **features**.

Given $w^{(1)}, ..., w^{(n_u)}, b^{(1)}, ..., b^{(n_u)}$, **cost function** to learn $x^{(1)}, ..., x^{(n_m)}$:

$J(x^{(1)}, ..., x^{(n_m)}) = \frac{1}{2}\sum_{i=1}^{n_m}\sum_{j:r(i,j)=1}(w^{(j)} * x^{(i)} + b^{(j)}-y^{(i, j)})^2  + \frac{\lambda}{2}\sum_{i=1}^{n_m}\sum_{k=1}^n(x_k^{(i)})^2$

Putting parameters and features cost functions together, we have a new cost function that we want to minimize, based on parameter values $w, b$ and features values $x$ for each user:

$$J(w, b, x) = \frac{1}{2}\sum_{(i, j):r(i,j)=1}(w^{(j)} * x^{(i)} + b^{(j)}-y^{(i, j)})^2  + \frac{\lambda}{2}\sum_{j=1}^{n_u}\sum_{k=1}^n(w_k^{(j)})^2 + \frac{\lambda}{2}\sum_{i=1}^{n_m}\sum_{k=1}^n(x_k^{(i)})^2$$

To minimize cost function, use **Gradient Descent**:

$repeat \space\{$

- $w_i^{(j)}=w_i^{(j)}-\alpha \frac{\partial}{\partial w_i^{(j)}}J(w,b,x)$

- $b^{(j)}=b^{(j)}-\alpha \frac{\partial}{\partial b^{(j)}}J(w,b,x)$
  
- $x_k^{(i)} = x_k^{(i)} - \alpha \frac{\partial}{\partial x_k^{(i)}}J(w,b,x)$

$\}$

## Limitations of Collaborative Filtering

- Not very good for cold start problems:
  - rank new items that few users have rated;
  - show something reasonable to new users who have rated few items.
- Difficult to use side information about items or users:
  - item: genre, movie stars, studio, etc.;
  - user: demographics (age, gender, location), expressed preferences, etc.

## Binary Labels

Possible recommender binary labels are: favorited, liked, clicked, engaged, etc.

Possible meaning of ratings:
- 1 - engaged after being shown;
- 0 - did not engage after being shown;
- ? - item not yet shown.

Example applications:
- did user $j$ purchase an item after being shown?
- did user $j$ fav/like an item?
- did user $j$ spend at least 30sec with an item?
- did user $j$ click on an item?

To generalize collaborative filtering algorithm from regression to binary classification we will predict a probability of $y^{(i, j)} = 1$ given by $g(w^{(j)} * x^{(i)} + b^{(j)}$, where $g(z) = \frac{1}{1+e^{-z}}$

**Binary cost function**:

$$J(w,b,x) = \sum_{(i, j):r(i,j)=1}L(f_{(w,b,x)}(x), y^{(i,j)}$$

, where

- $g(z) = \frac{1}{1+e^{-z}}$;
- $f_{w,b,x}(x) = g(w^{(j)} * x^{(i)} + b^{(j)})$;
- $L(f_{w,b,x}(x), y^{(i,j)}) = (-y^{(i,j)} \log(f_{w,b,x}( x ) ) - ( 1 - y^{(i,j)}) \log ( 1 - f_{w,b,x}( x ) )$

## Mean Normalization

In the case of building a recommended system with numbers $y$ such as movie ratings from one to five or zero to five stars, it turns out your algorithm will run more efficiently. And also perform a bit better if you first carry out mean normalization, that is if you normalize the movie ratings to have a consistent average value.

That way, when you dont have a user rating for a movie, you will not get weights ($w, b$) with 0 values and will not predict 0 user rating for a movie:

![image](https://user-images.githubusercontent.com/73081144/198196072-eccc33e6-26cc-4684-a506-f2a215356942.png)

*Fig. 2. Weights with 0 values and users with no ratings.*

In other words, mean normalization will cause no ratings to be equal to mean of ratings for a movie on a first iteration.

In order to carry out mean normalization, you subtract mean of one movie with every rating. The result becomes $y^{(i, j)}$:

![image](https://user-images.githubusercontent.com/73081144/198196179-46b4a04a-e1ed-40e7-a764-20c970073d31.png)

*Fig. 3. Mean normalization.*

In order not to predict negative values (e.g. movie ratings), add mean back to the linear function.

## Finding Related Items

To find an item $k$ related to an item $i$, just compare their features. In other words, find an item $x^{(k)}$ with features similar to $x^{(i)}$. To compare features, use **squared distance** between them:

$\sum^n_{l=1}(x_l^{(k)} - x_l^{(i)})^2$

or

$||x^{(k)} - x^{(i)}||^2$


