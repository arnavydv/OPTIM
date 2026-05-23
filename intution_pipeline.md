

# first thing is that we need to know about 
- optimal control(pi_star) its a decision or action that would be taken and it affects the happiness 
- value function: its the value of scalar that tells the happiness and affects the optimal control 
    
    majorly mertons problem connect both of them
    - so for both of them we are going to create neural networks which learns these 
# what acutally HJB is saying to us 
 - is that from wealth x at time t what could be the maximum happiness for a user for that we have to choose the control value 

 # whats the problem is ?
 pde solving is very computationally expensive on grids 
- so we are going to solve them using the solutiono of stochastic paths (one possible outcome of a random process)

# how we can solve a stochastic path ?
- find the formula for the distribution 
- first sample as many paths as you can 
- approximate the mean ,covariance and other quantity of interest

that how we can solve the stochastic paths

# how we are approaching this 
- using the forward simulation we are going to simulate paths which are X_t
- using backward simutlation we are going to propagate the value function 


so we can understand in a way that forward means we are taking the paths forward and writing all the paths possible \
and backward means we are using that paths in such a way we know what things we should take to get the maximum expected utility next time \
this is the whole crux of forward backward simulatino 

# what does the forward equation do 
- it simulates 1000s of different market scenarios (like some stock going up some stock going down some stays same )
- it simulates those paths and calculate the final wealth using that paths under randomness(how the wealth is evolving under randomness)
# what does the backward equation do 
We start at the end ($T$) \
where we know the truth: $U(W_T)$.\
We run the Backward Equation backwards along that same frozen path. 

It asks: "Given this final outcome, what was the optimal thing to do at every previous step to get here?"
It calculates a "Target Control" ($Z_t^{target}$) for every point on the path. \
Crucial Insight: If your Forward Pass (Actor) made a bad decision (e.g., invested too much before a crash), the Backward Pass will reveal a large gap between your action and the "Target Control" required to maximize utility.


# somethings to understand 
### THE TERMINAL CONDITION 
$Y_T$: it tells us thatt what would be the final condition like after that we dont have to optimize anything else 
\
if at the end we have $1000 we dont have to optimize another future we just have to simulate the backward equation which tells how the thing is allocated so that we can reach the $1000 mark 
### $ Y_T$
IT IS THE VALUE FUNCTION WHICH TELLS THE CURRENT HAPPINES OF THE USER OR THE INVESTOR \
FUTURE EXPECTED UTILITY 
### $Z_T$
THIS IS THE VALUE FUCNTION 