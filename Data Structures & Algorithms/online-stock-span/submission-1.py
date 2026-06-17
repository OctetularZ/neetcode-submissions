class StockSpanner:

    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        span = 1
        new_stock = [price, span]
        n = len(self.stock)
        
        while self.stock and self.stock[-1][0] <= new_stock[0]:
            top = self.stock.pop()
            new_stock[1] += top[1]
        
        self.stock.append(new_stock)
        
        
        return new_stock[1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# Current solution too slow
# To make faster, I could use a hashmap to store the index of 