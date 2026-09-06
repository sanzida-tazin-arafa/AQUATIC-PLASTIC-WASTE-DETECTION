import torch
import torch.nn as nn
import ultralytics.nn.tasks as tasks

class WeightedConcat(nn.Module):
    def __init__(self, dimension=1, n=2):
        super().__init__()
        self.d = dimension
        self.w = nn.Parameter(torch.ones(n), requires_grad=True)
        self.epsilon = 1e-4

    def forward(self, x):
        w = torch.relu(self.w)
        w = w / (w.sum() + self.epsilon)
        x = [xi * wi for xi, wi in zip(x, w)]
        return torch.cat(x, self.d)

tasks.Concat = WeightedConcat
