import typing as tp


def revert(dct: tp.Mapping[str, str]) -> dict[str, list[str]]:
    """
    :param dct: dictionary to revert in format {key: value}
    :return: reverted dictionary {value: [key1, key2, key3]}
    """
    re_dct: dict[str, list[str]] = {}
    for key in dct.keys():
        if dct[key] in re_dct:
            re_dct[dct[key]].append(key)
        else:
            re_dct[dct[key]] = [key]
    return re_dct
