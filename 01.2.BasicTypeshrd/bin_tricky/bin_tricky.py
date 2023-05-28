import typing as tp


def find_median(nums1: tp.Sequence[int], nums2: tp.Sequence[int]) -> float:
    """
    Find median of two sorted sequences. At least one of sequences should be not empty.
    :param nums1: sorted sequence of integers
    :param nums2: sorted sequence of integers
    :return: middle value if sum of sequences' lengths is odd
             average of two middle values if sum of sequences' lengths is even
    """
    n = len(nums1)
    m = len(nums2)
    if n > m:
        return find_median(nums2, nums1)

    start = 0
    end = n
    real = (n + m + 1) // 2

    while start <= end:
        mid = (start + end) // 2
        left1size = mid
        left2size = real - mid

        left1 = nums1[left1size - 1] if (left1size > 0) else float('-inf')
        left2 = nums2[left2size - 1] if (left2size > 0) else float('-inf')
        right1 = nums1[left1size] if (left1size < n) else float('inf')
        right2 = nums2[left2size] if (left2size < m) else float('inf')

        if left1 <= right2 and left2 <= right1:
            if (m + n) % 2 == 0:
                return (max(left1, left2) + min(right1, right2)) / 2
            return float(max(left1, left2))

        elif left1 > right2:
            end = mid - 1
        else:
            start = mid + 1
    assert False, "Not reachable"
