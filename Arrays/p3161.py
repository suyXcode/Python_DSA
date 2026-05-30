
#3161. Block Placement Queries
from bisect import bisect_left, insort

class Solution:
    def getResults(self, queries):
        maxX = 0

        for q in queries:
            maxX = max(maxX, q[1])

        obstacles = [0, maxX]

        for q in queries:
            if q[0] == 1:
                insort(obstacles, q[1])

        n = maxX + 2
        bit = [0] * n

        def update(i, val):
            i += 1
            while i < n:
                bit[i] = max(bit[i], val)
                i += i & -i

        def query(i):
            i += 1
            res = 0
            while i > 0:
                res = max(res, bit[i])
                i -= i & -i
            return res

        for i in range(1, len(obstacles)):
            update(obstacles[i], obstacles[i] - obstacles[i - 1])

        ans = []

        for q in reversed(queries):

            if q[0] == 2:
                x = q[1]
                sz = q[2]

                idx = bisect_left(obstacles, x)

                left = obstacles[idx - 1] if idx > 0 else 0

                best = query(left)
                best = max(best, x - left)

                ans.append(best >= sz)

            else:
                x = q[1]

                idx = bisect_left(obstacles, x)

                left = obstacles[idx - 1]
                right = obstacles[idx + 1]

                obstacles.pop(idx)

                update(right, right - left)

        ans.reverse()
        return ans
