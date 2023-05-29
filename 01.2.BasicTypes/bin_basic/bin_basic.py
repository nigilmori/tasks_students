import typing as tp


def find_value(nums: tp.Union[list[int], range], value: int) -> bool:
    if isinstance(nums, list):
        fi = 0
        la = len(nums)-1
        otv = -1
        while (fi <= la) and (otv == -1):
            m = (fi+la)//2
            if nums[m] == value:
                otv = m
            else:
                if value < nums[m]:
                    la = m - 1
                else:
                    fi = m + 1
        return otv != -1
    else:
        return nums.step*nums.start <= nums.step*value < nums.step*nums.stop and (value-nums.start) % nums.step == 0
