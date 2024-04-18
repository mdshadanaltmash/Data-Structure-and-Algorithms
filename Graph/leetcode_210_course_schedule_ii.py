class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj_list = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)

        visit_set, cycle = set(), set()
        topological_sort = []

        def dfs(course):
            if course in cycle:
                return False
            if course in visit_set:
                return True
            cycle.add(course)
            for pres in adj_list[course]:
                if not dfs(pres):
                    return False
            visit_set.add(course)
            cycle.remove(course)
            topological_sort.append(course)
            return True

        for crs in adj_list.keys():
            if crs not in visit_set:
                if not dfs(crs):
                    return []
        return topological_sort


if __name__ == '__main__':
    num_courses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    obj = Solution()
    print(obj.findOrder(num_courses, prerequisites))
