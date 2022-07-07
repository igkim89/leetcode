class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.data_list = []

    def next(self, val: int) -> float:
        size = self.size
        data_list = self.data_list
        data_list.append(val)
        data_sum = sum(data_list[-size:])
        data_avg = data_sum / (size if size < len(data_list) else len(data_list))
        
        return data_avg


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)