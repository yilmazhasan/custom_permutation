#!/usr/bin/env python
from typing import Annotated
import typer

from .scripts import custom_permutate_by_options
from .lib import get_options

app = typer.Typer()

@app.command()
def generate(items: Annotated[str, typer.Option("--items", help="Comma-separated list, e.g. a,b,c")] = [], # e.g. "a,b,c"
         includes: Annotated[list[str], typer.Option("--include", "-inc", "-ix", "-i", help="List for the included options, e.g. a,1")] = [], # e.g. "-i a,0"
         excludes: Annotated[list[str], typer.Option("--exclude", "-exc", "-ex", "-x", help="List for the included options, e.g. b,2")] = []): # e.g. "-x "b,1"

    separator = ',' # by default
    items = items.split(separator)
    options = get_options(items, includes, excludes, separator)
    permutation_generator = custom_permutate_by_options(items, options)

    for permutation in permutation_generator:
        print(separator.join(permutation))

if __name__ == "__main__":
  app()
