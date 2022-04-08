# -*- coding:UTF-8 -*-
'''
给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
在 S 上反复执行重复项删除操作，直到无法继续删除。
在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

示例：

输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。

提示：
    * 1 <= S.length <= 20000
    * S 仅由小写英文字母组成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string
'''

class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        这是通过递归的方法来做，时间复杂度很高  O(n^2)
        """
        length = len(S)
        for i in range(length-1):
            if S[i] == S[i+1]:
                S1 = S.replace('%s%s' % (S[i], S[i+1]), '')
                # print(S1)
                return self.removeDuplicates(S1)
        return S


    def removeDuplicates_1(self, S):
        """
        :type S: str
        :rtype: str
        使用 栈，代码非常简洁，时间复杂度 O(n) ，空间复杂度O(n)
        消除一对相邻重复项可能会导致新的相邻重复项出现，如从字符串 abba中删除 bb 会导致出现新的相邻重复项 aa 出现。
        因此我们需要保存当前还未被删除的字符。一种显而易见的数据结构呼之欲出：栈。
        我们只需要遍历该字符串，如果当前字符和栈顶字符相同，我们就贪心地将其消去，否则就将其入栈即可。
        """
        stack = ['']
        for i in S:
            if i == stack[-1]:
                stack.pop(-1)
            else:
                stack.append(i)
        return ''.join(stack)


    def removeDuplicates_2(self, S):
        """
        :type S: str
        :rtype: str
        使用 双指针 ， 时间复杂度 O(n)，空间复杂度 O(n)
        挨着两个相同的同时消失，可以使用两个指针。
            * 一个right一直往右移动，然后把指向的值递给left指向的值即可。
            * 一个left每次都会比较挨着的两个是否相同，如果相同，他两同时消失
        """
        left = 0
        right = 0
        length = len(S)
        l1 = list(S)
        while (right < length):
            l1[left] = l1[right]
            if (left > 0) and l1[left - 1] == l1[left]:
                left -= 2
            left += 1
            right += 1
        return ''.join(l1[:left])


if __name__ == '__main__':
    s = Solution()
    str1 = "aababaab"
    print(s.removeDuplicates(str1))
    print(s.removeDuplicates_1(str1))
    print(s.removeDuplicates_2(str1))
    str1 = "abbaca"
    print(s.removeDuplicates(str1))
    print(s.removeDuplicates_1(str1))
    print(s.removeDuplicates_2(str1))
