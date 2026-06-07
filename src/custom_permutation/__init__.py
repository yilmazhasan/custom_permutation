__version__ = "1.0.8"

from .core import generate as _generate
from . import cli  # backward compat


class CustomPermutation:
    @staticmethod
    def generate(items, includes=None, excludes=None, separator=','):
        return _generate(items, includes, excludes, separator)


__all__ = ['CustomPermutation', 'cli', '__version__']
