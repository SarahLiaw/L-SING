
import numpy as np
import torch
from models.UMNN import MonotonicNN


def mapS_losses(sk_zi, jacobian):
    """
    Compute the losses wrt to kth feature for a transport map, S.
    Parameters:
    - sk_zi: S^k(z_i) for all i. It's a function of z_i and h_i, where h_i are the samples that are not kth feature.
    - jacobian: ∂_kS^k(z_i)
    - kth: kth feature

    Returns:
    - Tensor of losses wrt to kth feature.
    """
    s_losses_tensor = 0.5 * sk_zi**2 - torch.log(jacobian)
    return s_losses_tensor



def test_map(samples, not_kth_ind, kth_ind, Sk):
    """
    Compute the transport map, S, for kth feature of the testing dataset.
    Parameters:

    - samples: samples from the dataset
    - not_kth_ind: indices of features that are not kth feature
    - kth_ind: index of kth feature
    - Sk: transport map

    Returns:
    - Tensor of Sk(z_i) for all i.
    - Jacobian of Sk(z_i) for all i.
    """
    Sk.eval()
    zk = samples.detach().requires_grad_(True)
    h = zk[:, not_kth_ind]
    x = zk[:, [kth_ind]]
    Sk_zi = Sk(x, h)
    jacobian = torch.autograd.grad(Sk_zi, x, torch.ones_like(Sk_zi), create_graph=True)[0]
    return Sk_zi, jacobian


def test_coeffs(Sk_zi, jacobian, kth):
    all_testing_losses = mapS_losses(Sk_zi, jacobian, kth) - np.log(1/np.sqrt(2 * np.pi))
    return all_testing_losses


def test_losses(Sk_zi, jacobian):#, kth):
    """
    Compute the losses wrt to kth feature for a transport map, S.
    Parameters:
    - samples: samples from the dataset
    - not_kth: indices of features that are not kth feature
    - kth: kth feature
    - Sk: transport map

    Returns:
    - Standard deviation and mean of losses wrt to kth feature.
    """
    all_testing_losses = mapS_losses(Sk_zi, jacobian) - np.log(1/np.sqrt(2 * np.pi))
    return (torch.std(all_testing_losses).item(), all_testing_losses.mean().item())


def train_map(samples, num_epochs, optimizer, not_kth_ind, kth_ind, Sk, regLambda=0.0):
    """
    Compute the transport map, S, for kth feature of the training dataset.
    Parameters:
    - samples: training samples from the dataset
    - num_epochs: number of epochs
    - optimizer: optimizer
    - not_kth_ind: indices of features that are not kth feature
    - kth_ind: index of kth feature
    - Sk: transport map
    - kth: kth feature
    - regLambda: regularisation parameter

    Returns:
    - Learnt map for kth component
    """
    n = samples.shape[0]
    for _ in range(num_epochs):
        zk = samples.detach().requires_grad_(True)
        h = zk[:, not_kth_ind]
        x = zk[:, [kth_ind]]

        sk_zi = Sk(x, h)
        print(sk_zi.shape)
        jacobian = torch.autograd.grad(sk_zi, x, torch.ones_like(sk_zi), create_graph=True)[0]
        print(jacobian.shape)
        loss = mapS_losses(sk_zi, jacobian, kth_ind)
        print(loss.shape)
        regulariser = torch.sum(torch.sqrt(torch.sum(jacobian[:, not_kth_ind]**2, dim=0)/n))
        print(regulariser.shape)
        loss += regLambda * regulariser

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
    return Sk