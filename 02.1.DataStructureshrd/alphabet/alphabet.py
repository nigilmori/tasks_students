import enum


class Status(enum.Enum):
    NEW = 0
    EXTRACTED = 1
    FINISHED = 2


def topological_sort(graph: dict[str, set[str]],
                     letter: str,
                     visited: dict[str, bool],
                     stack: list[str]) -> None:
    visited[letter] = True
    for letter2 in graph[letter]:
        if visited[letter2] is False:
            topological_sort(graph, letter2, visited, stack)
    stack.insert(0, letter)


def extract_alphabet(
        graph: dict[str, set[str]]
        ) -> list[str]:
    """
    Extract alphabet from graph
    :param graph: graph with partial order
    :return: alphabet
    """
    otv: list[str] = []
    visited = {letter: False for letter in graph.keys()}
    for letter in graph.keys():
        if not visited[letter]:
            topological_sort(graph, letter, visited, otv)
    return otv


def build_graph(
        words: list[str]
        ) -> dict[str, set[str]]:
    """
    Build graph from ordered words. Graph should contain all letters from words
    :param words: ordered words
    :return: graph
    """
    all_letters: set[str] = set()
    for word in words:
        for i in word:
            all_letters.add(i)
    graph: dict[str, set[str]] = {letter: set() for letter in all_letters}

    for iter in range(len(words) - 1):
        compare_words = list(zip(words[iter], words[iter + 1]))
        for letters_pair in compare_words:
            if letters_pair[0] != letters_pair[1]:
                graph[letters_pair[0]].add(letters_pair[1])
                break
    return graph


#########################
# Don't change this code
#########################

def get_alphabet(
        words: list[str]
        ) -> list[str]:
    """
    Extract alphabet from sorted words
    :param words: sorted words
    :return: alphabet
    """
    graph = build_graph(words)
    return extract_alphabet(graph)

#########################
