import typing as tp


def convert_to_common_type(data: list[tp.Any]) -> list[tp.Any]:
    """
    Takes list of multiple types' elements and convert each element to common type according to given rules
    :param data: list of multiple types' elements
    :return: list with elements converted to common type
    """
    non_false_types = {type(i) for i in data if bool(i) is not False}
    types = {type(i) for i in data}
    otv = []
    if list in non_false_types or tuple in non_false_types:
        for item in data:
            if bool(item) is False or item is None:
                item = []
            elif type(item) == str:
                item = [item]
            elif hasattr(item, "__iter__"):
                item = list(item)
            else:
                item = [item]
            otv.append(item)
    elif str in non_false_types:
        for item in data:
            if bool(item) is False or item is None:
                item = ""
            else:
                item = str(item)
            otv.append(item)
    elif float in non_false_types:
        for item in data:
            if bool(item) is False or item is None:
                item = 0.0
            else:
                item = float(item)
            otv.append(item)
    elif int in non_false_types:
        flag = 0
        for item in data:
            if type(item) == int and item != 1:
                flag = 1
        if flag == 0:
            for item in data:
                if bool(item) is False or item is None:
                    item = False
                else:
                    item = bool(item)
                otv.append(item)
        else:
            for item in data:
                if bool(item) is False or item is None:
                    item = 0
                else:
                    item = int(item)
                otv.append(item)
    elif bool in non_false_types:
        for item in data:
            if bool(item) is False or item is None:
                item = False
            else:
                item = bool(item)
            otv.append(item)
    elif len(non_false_types) == 0:
        if list in types or tuple in types:
            for item in data:
                if bool(item) is False or item is None:
                    item = []
                elif type(item) == str:
                    item = [item]
                elif hasattr(item, "__iter__"):
                    item = list(item)
                else:
                    item = [item]
                otv.append(item)
        elif int in types:
            flag = 0
            for item in data:
                if type(item) == int and item != 1:
                    flag = 1
            if flag == 0:
                for item in data:
                    if bool(item) is False or item is None:
                        item = False
                    else:
                        item = bool(item)
                    otv.append(item)
            else:
                for item in data:
                    if bool(item) is False or item is None:
                        item = 0
                    else:
                        item = int(item)
                    otv.append(item)
        elif str in types:
            for item in data:
                if bool(item) is False or item is None:
                    item = ""
                else:
                    item = str(item)
                otv.append(item)
        elif float in non_false_types:
            for item in data:
                if bool(item) is False or item is None:
                    item = 0.0
                else:
                    item = float(item)
                otv.append(item)
        elif bool in types:
            for item in data:
                if bool(item) is False or item is None:
                    item = False
                else:
                    item = bool(item)
                otv.append(item)
        elif set(types) == {type(None)}:
            for item in data:
                otv.append('')
    return otv
