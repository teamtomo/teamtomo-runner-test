import torch_test


def test_imports_with_version():
    assert isinstance(torch_test.__version__, str)
