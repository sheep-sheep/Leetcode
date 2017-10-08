class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        helper = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = 0
                queue = []
                if grid[i][j] and not helper[i][j]:
                    helper[i][j] = True
                    queue.append((i, j))
                while queue:
                    n = len(queue)
                    area += n
                    while n:
                        tmp_i, tmp_j = queue.pop(0)
                        n -= 1
                        if tmp_i-1 >= 0 and grid[tmp_i-1][tmp_j] and not helper[tmp_i-1][tmp_j]:
                            helper[tmp_i - 1][tmp_j] = True
                            queue.append((tmp_i - 1, tmp_j))

                        if tmp_i+1 < len(grid) and grid[tmp_i+1][tmp_j] and not helper[tmp_i+1][tmp_j]:
                            helper[tmp_i + 1][tmp_j] = True
                            queue.append((tmp_i + 1, tmp_j))

                        if tmp_j-1 >= 0 and grid[tmp_i][tmp_j-1] and not helper[tmp_i][tmp_j-1]:
                            helper[tmp_i][tmp_j-1] = True
                            queue.append((tmp_i, tmp_j-1))

                        if tmp_j+1 < len(grid[0]) and grid[tmp_i][tmp_j+1] and not helper[tmp_i][tmp_j+1]:
                            helper[tmp_i][tmp_j+1] = True
                            queue.append((tmp_i, tmp_j+1))

                maxArea = max(area, maxArea)

        return maxArea
