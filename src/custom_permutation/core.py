from .scripts import custom_permutate_by_options
from .lib import get_options


def generate(items, includes=None, excludes=None, separator=','):
    if includes is None:
        includes = []
    if excludes is None:
        excludes = []
    if isinstance(items, str):
        items = items.split(separator)
    options = get_options(items, includes, excludes, separator)
    results = []
    for permutation in custom_permutate_by_options(items, options):
        results.append(separator.join(permutation).split(separator))
    return results
