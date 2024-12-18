import numpy as np
import torch
from models.UMNN import MonotonicNN



def generate_easy_bf(num_samples, num_pairs):
    samples = []

    for _ in range(num_samples):
        sample = []
        for _ in range(num_pairs):
            X = np.random.normal(0, 1)
            W = np.random.normal(0, 1)
            Y = X * W #0.25 * X**3 + np.random.normal(0, 1)
            sample.append(X)
            sample.append(Y)
        samples.append(sample)
    samples = torch.tensor(samples, dtype=torch.float32)

    return samples



def generate_non_linear_maps(tot_features, hidden_layers, nb_steps, dev):
    """
    Generate a list of non-linear maps using UMNN.

    Parameters:
    - tot_features: Number of all features.
    - hidden_layers: Number of hidden layers.
    - nb_steps: Number of integration steps.
    - dev: Device to use.

    Returns:
    - List of non-linear maps.
    """
    non_linear_maps = []
    for _ in range(tot_features):
        non_linear_map = MonotonicNN(tot_features, hidden_layers, nb_steps, dev)
        non_linear_maps.append(non_linear_map)
    return non_linear_maps
