import torch
from torch.distributions import Categorical

from policy import Policy
from constants import *

import numpy as np


def select_action(state, policy):
    print(state)
    state = torch.FloatTensor(state).unsqueeze(0)
    # state2 = torch.from_numpy(np.array(state)).float().unsqueeze(0)
    probs = policy(state)
    m = Categorical(probs)
    action = m.sample()  # sample an action based on stochastic policy
    policy.saved_log_probs.append(m.log_prob(action))  # save log of policy decision (\log \pi_\theta)
    return action.item()


def run_inference(state):
    policy = Policy()
    policy.load_state_dict(torch.load(SAVED_MODEL_PATH))  # load saved model parameters
    policy.eval()  # set dropout and batch normalization layers to evaluation mode
    action = select_action(state, policy)
    return action


# run_inference(np.zeros((309)))
