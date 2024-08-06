class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometerReading = 0

    def getDescriptiveName(self):
        longName = str(self.year) + " " + self.make + " " + self.model
        return longName

    def readOdometer(self):
        """ 打印一条消息，指出汽车的里程 """
        print("This car has " + str(self.odometerReading) + " miles on it.")

    def updateOdometer(self, mileage):
        """
        将里程表读数设置为指定的值
        拒绝将里程表往回调
        """
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print("You can't roll back an odometer!")