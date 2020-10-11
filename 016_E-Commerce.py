class ECommerce:
    def __init__(self):
        self.log = []
    
    def print_log(self):
        print("Current log: {}".format(self.log))

    def record(self, order_id):
        self.log.append(order_id)
        print("Added id of value {} to log.".format(order_id))
    
    def get_last(self, i): # 1 <= i <= len(self.log)
        print("Element {} from the end of the list: {}".format(i, self.log[len(self.log)-i]))

#Driver code
from random import randint

ecommerce = ECommerce()
for i in range(1, 11):
    ecommerce.record(i)
    ecommerce.print_log()
    if not i % 2:
        ecommerce.get_last(randint(1, i-1))
    