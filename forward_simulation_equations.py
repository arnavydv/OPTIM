import numpy as np 
import torch 
from neural_networks import pi_star,Z_net
from brownian_motion import brownian_motion

def forward_simulation(model,dw,mu,sigma,w0,rate,T,num_steps):
    time_grid=np.linspace(0,T,num_steps+1)
    dt=T/num_steps
    num_paths = len(dw)/2
    wealth_grid = torch.zeros(num_paths, num_steps + 1)
    wealth_grid[:,0]=w0
    for i in range(num_steps):
        t=time_grid[i]
        w=wealth_grid[:,i]
        pi=model(t,w)
        drift=rate*w+(pi*(mu-rate))
        diffusion=(np.dot(pi,sigma))*dw[:,i]
        wealth_grid[i+1]=w+(drift*dt)+diffusion
    return time_grid,wealth_grid
model=pi_star()
dw=brownian_motion(1000,252,1/252)
mu= 0.20164940530246397 
sigma= 0.016162564586327234 
rate= 0.036800000000000 
w0= 1
forward_simulation(model,dw,mu,sigma,w0,rate,1,252)