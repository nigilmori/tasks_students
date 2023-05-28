def get_common_type(type1: type, type2: type) -> type:
    """
    Calculate common type according to rule, that it must have the most adequate interpretation after conversion.
    Look in tests for adequacy calibration.
    :param type1: one of [bool, int, float, complex, list, range, tuple, str] types
    :param type2: one of [bool, int, float, complex, list, range, tuple, str] types
    :return: the most concrete common type, which can be used to convert both input values
    """
    if type1 == type2 == range:
        return tuple
    elif type1 == type2:
        return type1
    elif type1 == str or type2 == str:
        return str
    elif type1 == list or type2 == list:
        if type1 in [tuple, range] or type2 in [tuple, range]:
            return list
        else:
            return str
    elif type1 == tuple or type2 == tuple:
        if type1 == range or type2 == range:
            return tuple
        else:
            return str
    elif type1 == range or type2 == range:
        return str
    elif type1 == float or type2 == float:
        if type1 == complex or type2 == complex:
            return complex
        else:
            return float
    elif type1 == int or type2 == int:
        if type1 == complex or type2 == complex:
            return complex
        else:
            return int
    elif type1 == bool or type2 == bool:
        return complex
    return bool
