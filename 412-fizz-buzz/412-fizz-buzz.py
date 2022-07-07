class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        data_list = []
        for i in range(1, n+1):
            if i%15 == 0:
                data_list.append("FizzBuzz")
            elif i%3 == 0:
                data_list.append("Fizz")
            elif i%5 == 0:
                data_list.append("Buzz")
            else:
                data_list.append(str(i))
        
        return data_list  