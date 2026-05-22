import numpy as np 
def forward_pass(time,N:int,mu,rate,sigma,pi_star,w_t):
    dt = time/N
    time_grid=np.linspace(0,time,N+1)
    wealth_path=np.zeros(N+1)
    wealth_path=w_t
    dW = np.random.normal(0, np.sqrt(dt), N)
    for i in range(N):
        t=time_grid[i]
        W=wealth_path[i]
        pi=pi_star(t,W)
    drift= rate*W+np.dot(pi,mu-rate)
    diffusion=(np.dot(pi,sigma))*dW[i]
    wealth_path[i+1]=W+(drift*dt)+diffusion
    return time_grid,wealth_path



