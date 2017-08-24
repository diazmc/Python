class Car(object):

    def __init__(self, price, speed, fuel, mileage):

        self.price = price 
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0

    def displayInfo(self):

        print "Price: " + str(self.price)
        print "Speed: " + str(self.speed) + "mph"
        print "Fuel: " + str(self.fuel) 
        print "Mileage: " + str(self.mileage) + "mpg"
  
        if self.price > 10000:
            print "Tax: 0.15"

        else:
            print "Tax: 0.12"
    
        

car1 = Car(20000,35,'full', 15)
car1.displayInfo()

car2 = Car(2000,5,'Not Full', 105)
car2.displayInfo()

car3 = Car(2000,15,'Kind of Full',95)
car3.displayInfo()

car4 = Car(2000,25,'Full', 25)
car4.displayInfo()

car5 = Car(2000,45,'Empty',25)
car5.displayInfo()

car6 = Car(2000000,35,'Empty',15)
car6.displayInfo()