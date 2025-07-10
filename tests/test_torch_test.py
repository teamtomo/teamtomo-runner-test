import torch


SHAPE = (10, ) * 3


def test_cpu():
    x = torch.zeros(SHAPE, device='cpu')
    assert x.shape == SHAPE


def test_gpu():
    x = torch.zeros(SHAPE, device='cuda')
    assert x.shape == SHAPE

