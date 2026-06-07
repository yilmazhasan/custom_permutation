# Custom Permutation

> Version 1.0.8

Python implementation for Custom Permutation.

## Usage

### Programmatic usage

```py
from custom_permutation import CustomPermutation

CustomPermutation.generate(items=["a", "b", "c", "d"], includes=["a,1"], excludes=["c,2"])
```

Output:

```sh
[
    ['b', 'a', 'd', 'c'],
    ['c', 'a', 'b', 'd'],
    ['c', 'a', 'd', 'b'],
    ['d', 'a', 'b', 'c']
]
```

### CLI usage

```sh
custom_permutation --items "a,b,c,d" -i "a,1" -x "c,2"
```

Output:

```sh
['b', 'a', 'd', 'c']
['c', 'a', 'b', 'd']
['c', 'a', 'd', 'b']
['d', 'a', 'b', 'c']
```

## Installation

`pip install custom_permutation`

## Set up locally for development

1. Clone the repository
2. Create and activate the virtural environment

   > `python -m venv .venv`

   > `source venv_mysite/bin/activate`

3. Install requirements:

   > `pip install -r requirements.txt`

4. Run the app:

   > `python src/custom_permutation/app.py --items a,b,c,d -i a,0 -x c,1 -x a,2`

## Args Explained

```sh
--items a,b,c,d -i a,0 -x c,1 -x a,2
```

This indicates that:

- We have four items `['a', 'b', 'c', 'd']`.
- We want `a` to be set at index `0`.
- We want neither `c` to be at index `1` nor `a` index `2`.
- Thus, the permutation will be generated based on the options below for each indexes:

```sh
[['a'], ['a', 'b', 'd'], ['a', 'b', 'd'], ['a', 'b', 'c', 'd']]
```

**idx `n` must be a member in `list` such as:**

- idx `0` $\in$ `['a']`
- idx `1` $\in$ `['a', 'b', 'd']`
- idx `2` $\in$ `['a', 'b', 'd']`
- idx `3` $\in$ `['a', 'b', 'c', 'd']`

The result would be four lists:

```
a,b,c,d
a,b,d,c
a,d,b,c
a,d,c,b
```
