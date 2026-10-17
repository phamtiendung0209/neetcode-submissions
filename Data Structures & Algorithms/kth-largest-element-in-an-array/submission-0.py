import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Store k largest elements in a heap, then return the heap[0]
        heap = []

        for value in nums:
            if len(heap) < k:
                heapq.heappush(heap, value)
            else:
                heapq.heappushpop(heap, value)

        return heap[0]