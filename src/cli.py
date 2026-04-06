#!/usr/bin/env python
from typing import Annotated
import typer

from scripts import custom_permutate_by_options
from lib import get_options

app = typer.Typer()


@app.command()
def main(items: Annotated[str, typer.Option("--items", "-i")] = [],
         includes: Annotated[list[str], typer.Option("--include", "-inc", "-i")] = [], # e.g. ("a,0")
         excludes: Annotated[list[str], typer.Option("--exclude", "-exc", "-x")] = []): # e.g. ("b,1")

    separator = ',' # by default
    items = items.split(separator)
    options = get_options(items, includes, excludes, separator)
    permutation_generator = custom_permutate_by_options(items, options)

    for permutation in permutation_generator:
        print(separator.join(permutation))

if __name__ == "__main__":
  app()
