class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        nums = [i for i in range(1, n+1)]
        head, tail = 0, n-1
        res = [0]*n
        for i in range(n):
            if k == 0:
                res[i:] = nums[head:tail+1] if i%2==1 else nums[tail:head-1:-1]
                break
            if i % 2 == 0:
                res[i] = nums[head]
                head +=1
                k -= 1
            else:
                res[i] = nums[tail]
                tail -= 1
                k -= 1
        return res
        
# for this kind of problem, i shouldn't focus on the coding or algorithm, i should find a pattern within the numbers,
# and the hard part is to optimize the solution.
