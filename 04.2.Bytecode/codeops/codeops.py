import dis
import types
from collections import Counter


def count_operations(source_code: types.CodeType) -> dict[str, int]:
    """Count byte code operations in given source code.

    :param source_code: the bytecode operation names to be extracted from
    :return: operation counts
    """
    arr = list(dis.get_instructions(source_code))
    iter = 0
    while iter < len(arr):
        if isinstance(arr[iter].argval, types.CodeType):
            arr1 = list(dis.get_instructions(arr[iter].argval))
            for instr in arr1:
                arr.append(instr)
        iter += 1
    return Counter([instruction.opname for instruction in arr])
