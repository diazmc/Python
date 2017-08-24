class Products(object):

    def __init__(self, price, item, weight, brand, cost, status):

        self.price = price
        self.item = item 
        self.weight = weight 
        self.brand = brand 
        self.cost = cost 
        self.status = 'For sale'
        

    def sell(self):

        if self.status == 'For sale':
            self.status = 'Sold'

        return self

    def addTax(self):

        tax = 0.15
        self.price += self.price * tax

        return self

    def ret(self):

        self.status = 'Defective'
        self.price = 0

        return self

        

    def displayInfo(self):

        print '$' + str(self.price), str(self.item), str(self.weight) + 'lb', str(self.brand), str(self.cost), str(self.status)

        

product1 = Products(10, 'apple', 10, 'costco', 7.99, 'For sale')
product1.sell().addTax().displayInfo()
