import torch
import torch.nn as nn

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

# NOTE: no global monkey-patch here (no `tasks.Concat = WeightedConcat`).
# This class is registered per-run in Colab via:
#   import ultralytics.nn.tasks as tasks
#   tasks.WeightedConcat = WeightedConcat
# which makes it resolvable by NAME for YAML layers explicitly typed
# 'WeightedConcat', while layers typed 'Concat' remain the stock class.
# Safe to reuse unmodified across F1/F2/F3/F4 selective ablation experiments -
# only the YAML determines which single layer becomes weighted.
