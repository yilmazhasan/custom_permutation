# Custom Permutation

Python implementation for Custom Permutation.

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