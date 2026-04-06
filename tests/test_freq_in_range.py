from src.custom_permutation.lib import freq_in_range

def test_freq_in_range():
    assert freq_in_range({1: 1, 2: 1, 3: 1}, {1: 1, 2: 1, 3: 1})
    assert not freq_in_range({1: 2, 2: 1, 3: 1}, {1: 1, 2: 1, 3: 1})
    assert freq_in_range({1: 1, 2: 1, 3: 1}, {1: 2, 2: 1, 3: 1})
    assert freq_in_range({-1: 3, 2: 1, 3: 1}, {1: 2, 2: 2, 3: 1})
    assert freq_in_range({0: 2, 1: 1, 2: 1}, {0: 3, 1: 1}) == False
