# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Author: Yunsheng Liu
# Date: 2021/1/5


"""
在一个由小写字母构成的字符串 s 中，包含由一些连续的相同字符所构成的分组。
例如，在字符串 s = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z"
和 "yy" 这样的一些分组。分组可以用区间 [start, end] 表示，其中 start
和 end 分别表示该分组的起始和终止位置的下标。上例中的 "xxxx" 分组用区间
表示为 [3,6] 。我们称所有包含大于或等于三个连续字符的分组为 较大分组 。
找到每一个 较大分组 的区间，按起始位置下标递增顺序排序后，返回结果。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/positions-of-large-groups
"""

# 方法一：一次遍历
#
# 我们可以遍历该序列，并记录当前分组的长度。如果下一个字符与当前字符不同，
# 或者已经枚举到字符串尾部，就说明当前字符为当前分组的尾部。每次找到当前
# 分组的尾部时，如果该分组长度达到 3，我们就将其加入答案。
#
# 复杂度分析
#
# 时间复杂度：O(n)，其中 n 是字符串的长度。我们只需要遍历一次该数组。
#
# 空间复杂度：O(1)。我们只需要常数的空间来保存若干变量，注意返回值不计入
# 空间复杂度。


class Solution:
    def largeGroupPositions(self, s):
        ret = list()
        n, num = len(s), 1

        for i in range(n):
            if i == n - 1 or s[i] != s[i + 1]:
                if num >= 3:
                    ret.append([i - num + 1, i])
                num = 1
            else:
                num += 1

        return ret
