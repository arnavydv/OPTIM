import numpy as np 
from neural_networks import pi_star
model=pi_star()
def forward_pass(time:float,N:int,mu:float,rate_in_percent:float,sigma_in_percent:float,model,w0):
    rate=rate_in_percent/100
    sigma=sigma_in_percent/100
    dt = time/N
    time_array=np.linspace(0,time,N+1)
    wealth_array=np.zeros(N+1)
    wealth_array=w0
    dW = np.random.normal(0, np.sqrt(dt), N)
    for i in range(N):
        t=time_array[i]
        W=wealth_array[i]
        pi=model(t,W)
    drift= rate*W+np.dot(pi,mu-rate)
    diffusion=(np.dot(pi,sigma))*dW[i]
    wealth_array[i+1]=W+(drift*dt)+diffusion
    return time_array,wealth_array

