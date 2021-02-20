'''
 解题思路：
若 n = 2^x且n = 2为自然数（即 n为2的幂），则一定满足以下条件：
1.恒有 n & (n - 1) == 0，这是因为：
n二进制最高位为 1，其余所有位为 0；
n−1二进制最高位为 0，其余所有位为 1；
2.一定满足 n > 0。
因此，通过 n > 0 且 n & (n - 1) == 0 即可判定是否满足 n = 2^x

'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0

