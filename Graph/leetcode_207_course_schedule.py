class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)

        visit_set = set()

        def dfs(course):
            if course in visit_set:
                return False
            if not adj_list[course]:
                return True
            visit_set.add(course)
            for pres in adj_list[course]:
                if not dfs(pres):
                    return False
                adj_list[course].pop(0)
            visit_set.remove(course)
            return True

        for crs in adj_list.keys():
            if not dfs(crs):
                return False
        return True


if __name__ == '__main__':
    num_courses = 3
    prerequisites = [[1, 0], [1, 2], [0, 1]]
    obj = Solution()
    print(obj.canFinish(num_courses, prerequisites))
