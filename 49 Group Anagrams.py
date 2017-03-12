class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for str in strs:
            group = ''
            for i in sorted(str):
                group+=i
            if group not in result:
                result[group] = [str]
            else:
                result[group] += [str]
        return result.values()
# This is my initial solution, need to understand the difference between tuple and list, so the tuple can be hashable?!

def groupAnagrams(self, strs):
    groups = collections.defaultdict(list)
    for s in strs:
        groups[tuple(sorted(s))].append(s)
    return map(sorted, groups.values())
