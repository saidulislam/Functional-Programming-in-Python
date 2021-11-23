class ListOperations():
    def __init__(self, any_list):
        self.any_list = any_list

    def add_values(self):
        self.sum = sum(self.any_list)


my_list = [1,2,3,4]
sum_values = ListOperations(my_list)
sum_values.add_values()

print(sum_values.sum)