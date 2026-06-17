class StockSpanner:

    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        self.stock.append(price)
        n = len(self.stock)
        span = 0

        for i in range(n - 1, -1, -1):
            if self.stock[i] > price:
                break
            
            span += 1
        
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)