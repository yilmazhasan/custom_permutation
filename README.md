# Custom Permutation

> Version 1.0.6

Python implementation for Custom Permutation.


## Usage

### Programmatic usage

```py
from custom_permutation import cli

cli.generate(items=["a", "b", "c", "d"], includes=["a,1"], excludes=["c,2"])
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
custom_permutation --items "a,b,c,d" -i "a,1" -x "c,2" -o stdout
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

This indicates:

- we have four items `['a', 'b', 'c', 'd']`.
- We want to have `a` to be at index `0`.
- We want not to have `c` at index `1` and `a` index `2`.
- Thus, the permutation will be generated based o the options below:

```sh
[
    ['a'],
    ['a', 'b', 'd'],
    ['a', 'b', 'd'],
    ['a', 'b', 'c', 'd']
]
```

The result would be four lists:

```
a,b,c,d
a,b,d,c
a,d,b,c
a,d,c,b
```