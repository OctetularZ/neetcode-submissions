class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        if len(stones) == 1:
            return stones[0]

        heap = [-x for x in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            rock_1 = heapq.heappop(heap)
            rock_2 = heapq.heappop(heap)

            new_rock = (-rock_1) - (-rock_2)
            if new_rock == 0:
                continue
            else:
                heapq.heappush(heap, -new_rock)
        
        return -heapq.heappop(heap) if len(heap) == 1 else 0
