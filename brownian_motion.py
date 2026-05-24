import numpy as np
def brownian_motion(num_paths,num_steps,dt):
    noise=np.randn(num_paths,num_steps)
    dw=noise*np.sqrt(dt)
    W=np.cumsum(dw,axis=1)
    return dw,W
