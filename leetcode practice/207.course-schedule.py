#
# @lc app=leetcode id=207 lang=python
#
# [207] Course Schedule
#

# @lc code=start
from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = dict((i,[] )for i in range(numCourses))
        indegree = [0] * numCourses
    
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
    
        completed = 0
    
        while queue:
            course = queue.popleft()
            completed += 1
        
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
    
        return completed == numCourses


        
        
# @lc code=end

