'''
    动态规划的思想优点是比较好想，缺点也很明显，空间复杂度比较高，那么回顾一下，我们只是需要得到同中心的回文子串数目，显然只要我们找到子串的中心，然后使用两个指针不断向两端延伸即可，也就是中心扩展法，这样空间复杂度就降到O(1)了。找中心很简单，字符串中的元素逐一遍历即可，但是要注意是奇数还是偶数回文串，奇数回文串中心只有一个，而偶数回文串中心有两个，我们事先不知道奇偶，解决办法可以参考官方题解的，也可以都计算一遍，这样比较好想。

'''



class Solution:
        def countSubstrings(self, s: str) -> int:
            n = len(s)
            self.res = 0
            def helper(i,j):
                while i >= 0 and j < n and s[i] == s[j]:
                    i -= 1
                    j += 1
                    self.res += 1
            for i in range(n):
                helper(i,i)
                helper(i,i+1)
            return self.res
