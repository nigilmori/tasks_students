"""
Simplified VM code which works for some cases.
You need extend/rewrite code to pass all cases.
"""

import builtins
import dis
import operator
import types
import typing as tp


class Frame:
    """
    Frame header in cpython with description
        https://github.com/python/cpython/blob/3.9/Include/frameobject.h#L17

    Text description of frame parameters
        https://docs.python.org/3/library/inspect.html?highlight=frame#types-and-members
    """
    def __init__(self,
                 frame_code: types.CodeType,
                 frame_builtins: dict[str, tp.Any],
                 frame_globals: dict[str, tp.Any],
                 frame_locals: dict[str, tp.Any]) -> None:
        self.code = frame_code
        self.builtins = frame_builtins
        self.globals = frame_globals
        self.locals = frame_locals
        self.lasti = 0
        self.data_stack: tp.Any = []
        self.return_value = None
        self.last_exception = None


    def top(self) -> tp.Any:
        return self.data_stack[-1]

    def pop(self) -> tp.Any:
        return self.data_stack.pop()

    def push(self, *values: tp.Any) -> None:
        self.data_stack.extend(values)

    def popn(self, n: int) -> tp.Any:
        """
        Pop a number of values from the value stack.
        A list of n values is returned, the deepest value first.
        """
        if n > 0:
            returned = self.data_stack[-n:]
            self.data_stack[-n:] = []
            return returned
        else:
            return []

    def peek(self, n):
        return self.data_stack[-n]

    def do_raise(self, exc, cause):
        pass

    def jump(self, jump: int):
        self.lasti = jump

    def run(self) -> tp.Any:
        for instruction in dis.get_instructions(self.code):
            getattr(self, instruction.opname.lower() + "_op")(instruction.argval)
        return self.return_value

    def call_function_op(self, arg: int) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-CALL_FUNCTION

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L3496
        """
        arguments = self.popn(arg)
        f = self.pop()
        self.push(f(*arguments))

    def load_name_op(self, arg: str) -> None:
        """
        Partial realization

        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-LOAD_NAME

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L2416
        """
        if arg in self.locals:
            val = self.locals[arg]
        elif arg in self.builtins:
            val = self.builtins[arg]
        self.push(val)

    def load_global_op(self, arg: str) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-LOAD_GLOBAL

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L2480
        """
        if arg in self.globals:
            val = self.globals[arg]
        elif arg in self.builtins:
            val = self.builtins[arg]
        else:
            raise NameError("global name '%s' is not defined" % arg)
        self.push(val)

    def store_global_op(self, arg: str) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-LOAD_GLOBAL

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L2480
        """
        self.globals[arg] = self.pop()

    def get_iter_op(self, arg: str) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-LOAD_GLOBAL

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L2480
        """
        self.push(iter(self.pop()))

    def for_iter_op(self, arg: int) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-LOAD_GLOBAL

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L2480
        """
        iterobj = self.top()
        try:
            v = next(iterobj)
            self.push(v)
        except StopIteration:
            self.pop()
            self.jump(arg)

    def load_const_op(self, arg: tp.Any) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-LOAD_CONST

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L1346
        """
        self.push(arg)

    def return_value_op(self, arg: tp.Any) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-RETURN_VALUE

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L1911
        """
        self.return_value = self.pop()

    def pop_top_op(self, arg: tp.Any) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-POP_TOP

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L1361
        """
        self.pop()

    def pop_jump_if_false_op(self, arg: int) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-POP_TOP

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L1361
        """
        val = self.pop()
        if not val:
            self.jump(arg)

    def pop_jump_if_true_op(self, arg: int) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-POP_TOP

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L1361
        """
        val = self.pop()
        if val:
            self.jump(arg)

    def load_assertion_error_op(self, arg: int) -> None:
        pass

    def raise_varargs_op(self, arg: int) -> None:
        pass

    def make_function_op(self, arg: int) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-MAKE_FUNCTION

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L3571

        Parse stack:
            https://github.com/python/cpython/blob/3.9/Objects/call.c#L671

        Call function in cpython:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L4950
        """
        name = self.pop()  # the qualified name of the function (at TOS)  # noqa
        code = self.pop()  # the code associated with the function (at TOS1)

        # TODO: use arg to parse function defaults

        def f(*args: tp.Any, **kwargs: tp.Any) -> tp.Any:
            # TODO: parse input arguments using code attributes such as co_argcount

            parsed_args: dict[str, tp.Any] = {}
            f_locals = dict(self.locals)
            f_locals.update(parsed_args)

            frame = Frame(code, self.builtins, self.globals, f_locals)  # Run code in prepared environment
            return frame.run()

        self.push(f)

    def inplace_add_op(self, arg: str) -> None:
        x, y = self.popn(2)
        x += y
        self.push(x)

    def inplace_power_op(self, arg: str) -> None:
        x, y = self.popn(2)
        x **= y
        self.push(x)

    def inplace_multiply_op(self, arg: str) -> None:
        x, y = self.popn(2)
        x *= y
        self.push(x)

    def inplace_modulo_op(self, arg: str) -> None:
        x, y = self.popn(2)
        x %= y
        self.push(x)

    def inplace_subtract_op(self, arg: str) -> None:
        x, y = self.popn(2)
        x -= y
        self.push(x)

    def inplace_true_divide_op(self, arg: str) -> None:
        x, y = self.popn(2)
        x /= y
        self.push(x)

    def inplace_lshift_op(self, arg: str) -> None:
        x, y = self.popn(2)
        x <<= y
        self.push(x)

    def inplace_rshift_op(self, arg: str) -> None:
        x, y = self.popn(2)
        x >>= y
        self.push(x)

    def inplace_and_op(self, arg: str) -> None:
        x, y = self.popn(2)
        x &= y
        self.push(x)

    def inplace_or_op(self, arg: str) -> None:
        x, y = self.popn(2)
        x |= y
        self.push(x)

    def inplace_xor_op(self, arg: str) -> None:
        x, y = self.popn(2)
        x ^= y
        self.push(x)

    def inplace_floor_divide_op(self, arg: str) -> None:
        x, y = self.popn(2)
        x //= y
        self.push(x)

    def build_slice_op(self, count):
        if count == 2:
            x, y = self.popn(2)
            self.push(slice(x, y))
        elif count == 3:
            x, y, z = self.popn(3)
            self.push(slice(x, y, z))

    def binary_subscr_op(self, arg: tp.Any):
        iterble = self.pop()
        slice = (self.pop().indices(len(iterble)))
        self.push(iterble[slice[0]: slice[1] : slice[2]])

    def build_tuple_op(self, arg: int):
        elems = self.popn(arg)
        self.push(tuple(elems))

    def build_list_op(self, arg: int):
        elems = list(self.popn(arg))
        self.push(elems)

    def list_extend_op(self, arg: int):
        val = self.pop()
        the_list = self.peek(arg)
        for item in val:
            the_list.append(item)

    def build_set_op(self, arg: int):
        elems = self.popn(arg)
        self.push(set(elems))

    def set_update_op(self, arg: int):
        pass

    def build_map_op(self, size):
        self.push({})

    def store_map_op(self):
        the_map, val, key = self.popn(3)
        the_map[key] = val
        self.push(the_map)

    def extended_arg_op(self, arg: str) -> None:
        pass

    def compare_op_op(self, arg: tp.Any) -> None:

        x, y = self.popn(2)
        if arg == "==":
            self.push(x == y)

    def binary_add_op(self, arg: str) -> None:

        x, y = self.popn(2)
        x = x + y
        self.push(x)

    def jump_absolute_op(self, arg: int) -> None:

        self.jump(arg)

    def store_name_op(self, arg: str) -> None:

        const = self.pop()
        self.locals[arg] = const

    def unpack_sequence_op(self, arg: str) -> None:

        seq = self.pop()
        for x in reversed(seq):
            self.push(x)




class VirtualMachine:
    def run(self, code_obj: types.CodeType) -> None:
        """
        :param code_obj: code for interpreting
        """
        globals_context: dict[str, tp.Any] = {}
        frame = Frame(code_obj, builtins.globals()['__builtins__'], globals_context, globals_context)
        return frame.run()
