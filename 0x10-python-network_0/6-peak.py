#!/usr/bin/python3
"""Module to find the peak in a list of integers"""


def find_peak(nums):
    """find_peak function definition"""
    size = len(nums)
    if (size == 0):
        return
    mid_index = size // 2
    if (mid_index == size - 1 or nums[mid_index] >= nums[mid_index + 1]) \
            and (nums[mid_index] >= nums[mid_index - 1] or mid_index == 0):
        return nums[mid_index]
    if (mid_index != size - 1) and nums[mid_index + 1] > nums[mid_index]:
        return find_peak(nums[mid_index+1:])
    else:
        return find_peak(nums[:mid_index])
