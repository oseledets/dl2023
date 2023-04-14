import random

import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader
from matplotlib import pyplot as plt


class SqrDataset(Dataset):
    def __len__(self):
        return 10**6
    
    def __getitem__(self, _):
        x = random.random() * 6 - 3
        return torch.tensor([x]), torch.tensor([x**2])
            

class Network(nn.Module):
    def __init__(self):
        super().__init__()
        
        self.linear1 = nn.Linear(1, 32)
        self.linear2 = nn.Linear(32, 1)
        
    def forward(self, x):
        x = self.linear1(x)
        x = nn.functional.relu(x)
        x = self.linear2(x)
        
        return x
        
        
dataset = SqrDataset()
dataloader = DataLoader(dataset, 2**10, False, num_workers=0)
    
N = 32
network = Network().cuda()
optimizer = torch.optim.Adam(network.parameters())

for x, y in dataloader:
    network_output = network(x.cuda())
    loss = ((network_output - y.cuda())**2).mean()

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print(loss.item())
    
    
xs = torch.linspace(-3, 3, 1000)[:, None]
ys = network(xs.cuda()).detach().cpu()

plt.plot(xs.numpy(), ys.numpy())
plt.plot(xs.numpy(), xs.numpy()**2)
plt.savefig('./a.png')
plt.show()