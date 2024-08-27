class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        start_day = {task: 0 for task in tasks}
        day = 0
        for task in tasks:
            day += 1

            # if the current day is too early to complete the task,
            # fast forward the day to the earliest day you can.
            if day < start_day[task]:
                day = start_day[task]

                # update the earliest day you can complete the task.
            start_day[task] = day + space + 1

        return day
