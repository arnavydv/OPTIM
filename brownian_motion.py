import numpy as np
import torch
def brownian_motion(num_paths,num_steps,dt):
    noise=torch.randn(num_paths,num_steps)
    dw=noise*np.sqrt(dt)
    W=torch.cumsum(dw,axis=1)
    return dw,W
