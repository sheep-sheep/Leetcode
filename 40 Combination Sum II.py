class Solution(object):
    def combinationSum2(self, candidates, target):
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
                if i > idx and candidates[i] == candidates[i-1]: #This line is the KEY!!!
                    continue
                findSum(candidates, target-candidates[i], i+1, path + [candidates[i]], res)
        res = []
        if not candidates:
            return []
        else:
            candidates = sorted(candidates)
            findSum(candidates, target, 0, [], res)
            return res
