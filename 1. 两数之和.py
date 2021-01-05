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

"""


# 方法一：暴力枚举
#
# 最容易想到的方法是枚举数组中的每一个数 x，寻找数组中是否存在 target - x。
# 当我们使用遍历整个数组的方式寻找 target - x 时，需要注意到每一个位于 x
# 之前的元素都已经和 x 匹配过，因此不需要再进行匹配。而每一个元素不能被使用
# 两次，所以我们只需要在 x 后面的元素中寻找 target - x。

# 复杂度分析
#
# 时间复杂度：O(N^2)，其中 N 是数组中的元素数量。最坏情况下数组中任意两个数
# 都要被匹配一次。
#
# 空间复杂度：O(1)。


class Solution1:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# 方法二：哈希表
#
# 注意到方法一的时间复杂度较高的原因是寻找 target - x 的时间复杂度过高。因此，
# 我们需要一种更优秀的方法，能够快速寻找数组中是否存在目标元素。如果存在，我们
# 需要找出它的索引。
#
# 使用哈希表，可以将寻找 target - x 的时间复杂度降低到从 O(N) 降低到 O(1)O(1)。
# 这样我们创建一个哈希表，对于每一个 x，我们首先查询哈希表中是否存在 target - x，
# 然后将 x 插入到哈希表中，即可保证不会让 x 和自己匹配。

# 复杂度分析
# 
# 时间复杂度：O(N)，其中 N 是数组中的元素数量。对于每一个元素 x，我们可以 O(1)地
# 寻找 target - x。
#
# 空间复杂度：O(N)，其中 N 是数组中的元素数量。主要为哈希表的开销。


class Solution2:
    def twoSum(self, nums, target):
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
