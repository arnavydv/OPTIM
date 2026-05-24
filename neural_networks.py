import torch 
from torch import nn

class pi_star(nn.Module):
    def __init__(self):
        super().__init()
        self.network=nn.Sequential(
            nn.Linear(2,32),
            nn.ReLU(),
            nn.Linear(32,32),
            nn.ReLU(),
            nn.Linear(32,32),
            nn.ReLU(),
            nn.Linear(32,32),
            nn.Tanh(),
            nn.Linear(32,1)
        )
    def forward(self,x,y):
        input_tensor=torch.cat([x,y],dim=1)
        output_tensor=self.network(input_tensor)
        return output_tensor
    
class Z_net(nn.Module):
    def __init__(self):
        super().__init()
        self.network=nn.Sequential(
            nn.Linear(2,32),
            nn.ReLU(),
            nn.Linear(32,32),
            nn.ReLU(),
            nn.Linear(32,32),
            nn.ReLU(),
            nn.Linear(32,32),
            nn.Tanh(),
            nn.Linear(32,1)
        )
    def forward(self,t,W):
        input_tensor=torch.cat([t,W],dim=1)
        output_tensor=self.network(input_tensor)
        return output_tensor