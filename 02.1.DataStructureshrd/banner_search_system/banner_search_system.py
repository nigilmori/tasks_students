import heapq
import typing as tp
from collections import Counter


def normalize(
        text: str
        ) -> str:
    """
    Removes punctuation and digits and convert to lower case
    :param text: text to normalize
    :return: normalized query
    """
    text = text.lower()
    del_symbols = "0123456789?#@*&%,.!/-"
    for symbol in del_symbols:
        text = text.replace(symbol, "")
    return text


def get_words(
        query: str
        ) -> list[str]:
    """
    Split by words and leave only words with letters greater than 3
    :param query: query to split
    :return: filtered and split query by words
    """
    return [word for word in query.split() if len(word) > 3]


def build_index(
        banners: list[str]
        ) -> dict[str, list[int]]:
    """
    Create index from words to banners ids with preserving order and without repetitions
    :param banners: list of banners for indexation
    :return: mapping from word to banners ids
    """
    indexes: dict[str, list[int]] = {}
    banners = [normalize(banner) for banner in banners]
    for banner in banners:
        for word in get_words(banner):
            indexes.setdefault(word, [index for index in range(len(banners)) if word in get_words(banners[index])])
    return indexes


def merge(seq: tp.Sequence[tp.Sequence[int]]) -> list[int]:
    """
    :param seq: sequence of sorted sequences
    :return: merged sorted list
    """
    mins = [[seq[i][0], i, 0] for i in range(len(seq)) if len(seq[i]) > 0]
    heapq.heapify(mins)
    otv = []
    while len(mins) > 0:
        mini = heapq.heappop(mins)
        otv.append(mini[0])
        if mini[2] < len(seq[mini[1]]) - 1:
            heapq.heappush(mins, [seq[mini[1]][mini[2]+1], mini[1], mini[2]+1])
    return otv


def get_banner_indices_by_query(
        query: str,
        index: dict[str, list[int]]
        ) -> list[int]:
    """
    Extract banners indices from index, if all words from query contains in indexed banner
    :param query: query to find banners
    :param index: index to search banners
    :return: list of indices of suitable banners
    """
    query = normalize(query)
    words_query = get_words(query)
    indexes_words_query = []
    for word in words_query:
        if word in index.keys():
            indexes_words_query.append(index[word])
    counter = Counter(merge(indexes_words_query))
    return [i for i in counter.keys() if counter[i] == len(words_query)]


#########################
# Don't change this code
#########################

def get_banners(
        query: str,
        index: dict[str, list[int]],
        banners: list[str]
        ) -> list[str]:
    """
    Extract banners matched to queries
    :param query: query to match
    :param index: word-banner_ids index
    :param banners: list of banners
    :return: list of matched banners
    """
    indices = get_banner_indices_by_query(query, index)
    return [banners[i] for i in indices]

#########################
