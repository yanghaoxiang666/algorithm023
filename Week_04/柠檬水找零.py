class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        a=[0,0,0,0,0]
        for i in bills:
            a[int(i/5)]+=1
            a[int(i/10)]-=1
            a[int(i/20)]-=1
            if a[1]<0 or a[1]+2*a[2]<0:
                return False
        return True

'''
使用贪心算法，可以使得5元的零钱剩下的数量达到最多，如果这样5元零钱都不足，
那就是肯定无法正确找零。由于判断a[1]<0，是在假设有足够10元数量的情况下得到的，
但是实际中10元零钱的数量即a[2]可能是负值，所以这是需要用5元零钱去填补，
所以要保证a[1]+2*a[2]>=0才行，否则无法正确找零
'''