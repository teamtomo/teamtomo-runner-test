import torch
from torch_test import cover_me


SHAPE = (10, ) * 3


def test_cpu():
    x = torch.ones(SHAPE, device='cpu')
    y = cover_me(x)
    assert y.shape == SHAPE


def test_gpu():
    x = torch.ones(SHAPE, device='cuda')
    y = cover_me(x)
    assert y.shape == SHAPE
    assert 'cuda' in str(y.device)

