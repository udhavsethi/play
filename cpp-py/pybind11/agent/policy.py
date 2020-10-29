import torch.nn as nn
import torch.nn.functional as F

from constants import *


class Policy(nn.Module):
    def __init__(self):
        super(Policy, self).__init__()
        # an affine operation: y = Wx + b
        self.fc1 = nn.Linear(INPUT_SIZE, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, OUTPUT_SIZE)

        self.saved_log_probs = []
        self.rewards = []

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.softmax(self.fc3(x), dim=1)
        return x
