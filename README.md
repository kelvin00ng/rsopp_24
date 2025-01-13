# rsopp_24
Undergraduate and Master Research Opportunities @ NUS Synthetic Biology

# Question 1
There is a Ben and Jerry's ice cream machine at UTown that charges $1 to play. Given that the price of a small tub is around $6, what is the distribution that best models the expected number of tries before successfully grabbing one of the tubs and how would you derive and compute the parameter(s) for this distribution from actual data? Bonus points for you if you try this in person and provide a GitHub repository to show case your work.

## Answer
We are interested in modelling the number of tries before success. Each tries can be simplified to 2 outcomes. Success(get the ice cream) and failure (Do not get the ice cream). Therefore a geometric distribution is appropriate to model what we want. 
Refer to the python file attached for a rough attempt at modelling.
methodology:
1. Code for vending machine to generate sample data.
    a. I set the probability of success to be 1/7
    b. I utilise the random library to determine if it will succeed or not. each failure is counted and upon succeed, the total number of tries is logged in a list called data. 
2. Using p = n/(total number of trials before success) as a sample probability.
3. We can also calculate the expected number of attempts needed before a success which is defined as 1/p.
4. From this futher analysis can be derived such as potential profit (for example, setting p = 1/7 will imply and expected 7 trials before a success. Since each attempt is a dollar and the price for the ice cream is 6. the profit over a long run is $1.)

# Question 2
m&m candies are manufactured at two different plants in the US with the following color distribution
Cleveland : Red=0.131, Orange=0.205, Yellow=0.135, Green=0.198, Blue=0.207, and Brown=0.124.
Hackettstown : Red=0.125, Orange=0.25, Yellow=0.125, Green=0.125, Blue=0.25, and Brown=0.125.
Suppose you bought many packets of m&m, how can you determine which plant these packets came with statistical testing?
Bonus: The methodology in this article is flawed. Can you explain why?

## Answer
Using a chi-squared test.
1. Find the average proportion for each color in each bag.
2. Repeat step 1 over multiple bags maybe 100.
3. calculate the average poportion of each color.
4. Carry out the chi-square test using the cleveland and hacketstown proportions. 
5. Set the significance level at 0.01. Reject the null hypothesis (From the same plant) if p value from chi-squared test < significance level.
6. Additionally, obtain the 99% confidence interval and check if the cleveland and hacketstown porportions lie within the CI.

In the article, the methodology differes slighty from my proposed method. The author has only access to M&M that have been opened and pour into a jug and he has to take each scoop daily. Taking each scoop daily might not be representative of the population. Additionally, due to this limitation, he is unable to calcualte proportion for each bag and taking the average of all the bags and use it as a proportion. The author method will not account for any variation between bags. Taking the average proportion of all the bags may provide a more robust analysis. 

# Question 3
I have checked back in the project and realised an additional question has been added.

Suppose you observed k people playing the Ben and Jerry's ice cream machine at UTown. You counted the number of times N that the machine was played in order to get k tubs of ice cream. What distribution will best fit the expected number of times N one would have to play to obtain k tubs of ice cream? Bonus point for providing another distribution that does the same. 

I will use a negative binomial distribution to model the number of failure before getting k success. A poisson distribution is also mathematically simliar to a negative binomial distribution. set the rate to be gamma distributed random variable with alpha = k and rate = p/(1-p)