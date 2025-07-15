"""Package description."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("torch-test")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Marten Chaillet"
__email__ = "marten.chaillet@gmail.com"


from torch_test.function import cover_me

__all__ = ["cover_me"]
