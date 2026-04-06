from src.custom_permutation.scripts import custom_permutate_by_options
from src.custom_permutation.lib import get_options

def get_permutation_count(permutation_generator):
    result = set()
    for permutation in permutation_generator:
        result.add(','.join(permutation))
    return len(result)

def test_app_with_inc_and_exc():
    separator = ','
    items = ['b', 'b', 'b', 'c']
    options = get_options(items=items, includes=['b,0'], excludes=[], separator=separator)
    permutation_generator = custom_permutate_by_options(items, options)
    count = get_permutation_count(permutation_generator)
    assert count == 3

def test_app_with_inc_and_exc_2():
    separator = ','
    items = ['b', 'b', 'b', 'c', 'a']
    options = get_options(items=items, includes=['b,0'], excludes=['a,0', 'a,1', 'a,2', 'a,3'], separator=separator)
    permutation_generator = custom_permutate_by_options(items, options)

    count = get_permutation_count(permutation_generator)
    assert count == 3

def test_app_with_predefined_options():
    items = ['b', 'b', 'b', 'c']
    options = [['b'], ['b', 'c'], ['b', 'c'], ['b', 'c']]
    permutation_generator = custom_permutate_by_options(items, options)
    count = get_permutation_count(permutation_generator)
    assert count == 3

def test_app_with_predefined_options():
    items = ['b', 'b', 'b', 'c', 'a']
    options = [['b'], ['b', 'c'], ['b', 'c'], ['b', 'c'], ['a', 'b', 'c']]
    permutation_generator = custom_permutate_by_options(items, options)

    count = get_permutation_count(permutation_generator)
    assert count == 3
