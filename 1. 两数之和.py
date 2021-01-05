# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Author: Yunsheng Liu
# Date: 2021/1/5

"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出
和为目标值的那两个整数，并返回它们的数组下标。你可以假设每种输入只会
对应一个答案。但是，数组中同一个元素不能使用两遍。你可以按任意顺序返
回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum


输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def twoSum(self, nums, target):
        """

        :param nums: list, 整数数组。
        :param target: int, 整数目标值
        :return:list
        """
        temp = {}
        for i, value in enumerate(nums):
            if target - value in temp:
                return [temp[target - value], i]
            temp[value] = i
        return []
