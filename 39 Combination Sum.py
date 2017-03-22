class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def findSum(candidates, target, idx, path, res):
            if target < 0:
               return []
            elif target == 0:
                res.append(path)

            for i in range(idx, len(candidates)):
                findSum(candidates, target-candidates[i], i, path + [candidates[i]], res)
        res = []
        if not candidates:
            return []
        else:
            candidates.sort()
            findSum(candidates, target, 0, [], res)
            return res
