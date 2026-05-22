import torch 
from torch import nn

class pi_star(nn.Module):
    def __init__(self):
        super.__init()
        self.network=nn.Sequential(
            nn.Linear(2,32),
            nn.tanh(),
            nn.Linear(32,32),
            nn.tanh(),
            nn.Linear(32,1)
        )
    def forward(self,x,y):
        input_tensor=torch.cat(x,y)
        output_tensor=self.network(input_tensor)
        return output_tensor