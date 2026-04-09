# Custom Permutation

> Version 1.0.4

Python implementation for Custom Permutation.

## Setup for repo

1. Clone the repository
2. Create and activate the virtural environment
> `python -m venv .venv`

> `source venv_mysite/bin/activate`

3. Install requirements:
> `pip install -r requirements.txt`

4. Run the app:

> `python src/custom_permutation/app.py --items a,b,c,d -i a,0 -x c,1 -x a,2`

## Args

```sh
--items a,b,c,d -i a,0 -x c,1 -x a,2
```

The permutation will be generated based o the options below:

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