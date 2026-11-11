class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-c for c in counts.values()]
        heapq.heapify(heap)

        queue = deque()
        ans = 0

        while heap or queue:
            ans += 1

            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt != 0:
                    queue.append((cnt, ans + n))

            if queue and queue[0][1] == ans:
                heapq.heappush(heap, queue.popleft()[0])


        return ans


            