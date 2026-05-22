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
    
class function_f(nn.Module):
    def __init__(self):
        super().__init__()
        self.network=nn.Sequential(
            nn.Linear(4,32),
            nn.ReLU(),
            nn.Linear(32,32),
            nn.ReLU(),
            nn.Linear(32,32),
            nn.ReLU,
            nn.Linear(32,1)
        )
    def forward(self,x,y,z,w):
        input_tensor=torch.cat((x,y,z,w))
        output_tensor=self.network(input_tensor)
        return output_tensor