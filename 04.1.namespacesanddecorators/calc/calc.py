import sys
import math
from typing import Any, Optional

PROMPT = '>>> '


def run_calc(context: Optional[dict[str, Any]] = None) -> None:
    """Run interactive calculator session in specified namespace"""
    inp, out = sys.stdin, sys.stdout
    out.write(PROMPT)
    operations = inp.readline()
    while operations != "":
        out.write(str(eval(operations, {"__builtins__": {}}, context)) + "\n")
        out.write(PROMPT)
        operations = inp.readline()
    out.write("\n")


if __name__ == '__main__':
    context = {'math': math}
    run_calc(context)
