from src.custom_permutation.lib import increment_by_custom_base

def test_increment_by_custom_base():
    res = increment_by_custom_base(the_input_number=[0, 0, 0, 0], the_base_limit=[1, 2, 2, 2])
    assert res ==  [0, 0, 0, 1]

    res = increment_by_custom_base(the_input_number=[1, 1, 2, 2], the_base_limit=[2, 3, 3, 3]) 
    assert res ==  [1, 2, 0, 0]

    res = increment_by_custom_base(the_input_number=[1, 2, 2, 2], the_base_limit=[2, 3, 3, 3]) 
    assert res ==  [0, 0, 0, 0]
