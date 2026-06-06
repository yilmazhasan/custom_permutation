#!/usr/bin/env python
from typing import Annotated
import typer

from .core import generate as _core_generate

app = typer.Typer()

_SEPARATOR = ','


@app.command()
def generate(
    items: Annotated[str, typer.Option("--items", help="Comma-separated list, e.g. --items a,b,c")] = "",
    includes: Annotated[list[str], typer.Option(
        "--include", "-inc", "-ix", "-i", help="Included constraint, e.g. -i a,1")] = [],
    excludes: Annotated[list[str], typer.Option(
        "--exclude", "-exc", "-ex", "-x", help="Excluded constraint, e.g. -x b,2")] = [],
    out: Annotated[str, typer.Option("--out", "-o", help="Output destination: 'stdout' or a filepath")] = '',
):
    results = _core_generate(items=items, includes=includes, excludes=excludes)

    if out == 'stdout':
        for perm in results:
            print(perm)
    elif out:
        with open(out, 'w') as f:
            f.write('\n'.join([_SEPARATOR.join(perm) for perm in results]))

    return results


if __name__ == "__main__":
    app()
