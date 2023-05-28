import typing as tp


def count_util(text: str, flags: tp.Optional[str] = None) -> dict[str, int]:
    """
    :param text: text to count entities
    :param flags: flags in command-like format - can be:
        * -m stands for counting characters
        * -l stands for counting lines
        * -L stands for getting length of the longest line
        * -w stands for counting words
    More than one flag can be passed at the same time, for example:
        * "-l -m"
        * "-lLw"
    Ommiting flags or passing empty string is equivalent to "-mlLw"
    :return: mapping from string keys to corresponding counter, where
    keys are selected according to the received flags:
        * "chars" - amount of characters
        * "lines" - amount of lines
        * "longest_line" - the longest line length
        * "words" - amount of words
    """
    if flags is None:
        flags = ""
    flags = flags.replace("-", "")
    flags = flags.replace(" ", "")
    set_flags = set(list(flags))
    if (set_flags == set()):
        set_flags = {"m", "l", "L", "w"}
    otv: dict[str, int] = {}
    if "m" in set_flags:
        otv.setdefault("chars", len(text))
    if "l" in set_flags:
        otv.setdefault("lines", text.count("\n"))
    if "L" in set_flags:
        may_long_lines = [len(line) for line in text.splitlines()]
        if len(may_long_lines) > 0:
            otv.setdefault("longest_line", max(may_long_lines))
        else:
            otv.setdefault("longest_line", 0)
    if "w" in set_flags:
        lines = text.split("\n")
        count_words = 0
        for line in lines:
            words_in_line = [word for word in line.split() if bool(word) is not False]
            count_words += len(words_in_line)
        otv.setdefault("words", count_words)

    return otv
