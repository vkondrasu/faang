# https://leetcode.com/problems/task-scheduler-ii/description/ 
# 2365. Task Scheduler II

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        time = c = 0
        n = len(tasks)
        executionTime = {}
        for c in range(n):

            if tasks[c] in executionTime:
                # we executed this task earlier but current time (time+1) is minimum space away from last execution time
                if time - executionTime[tasks[c]] >= space:
                    time += 1
                # we executed this task earlier but current time (time+1) is NOT minimum space away from last execution time
                # we have wait till time is last execution time + space away; executionTime[tasks[c]] + space + 1
                else:
                    time = executionTime[tasks[c]] + space + 1
                executionTime[tasks[c]] = time
            # we are executing this task for the first time - execute now at (time+1)
            else:
                time += 1
                executionTime[tasks[c]] = time
                

        return time
