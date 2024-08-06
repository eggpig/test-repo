# 文件 car2.py


""" 一个可用于表示汽车的类 """
""" 一组用于表示燃油汽车和电动汽车的类 """

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

    def incrementOdometer(self, miles):
        """ 将里程表读数增加指定的量 """
        self.odometerReading += miles

class Battery():
    """ 一次模拟电动汽车电瓶的简单尝试 """
    def __init__(self, batterySize=70):
        """ 初始化电瓶属性 """
        self.batterySize = batterySize

    def describeBattery(self):
        """ 打印一条描述电瓶容量信息 """
        print("This car has a " + str(self.batterySize) + "-kwh battery.")

    def getRange(self):
        """ 打印一条描述电瓶续航里程的消息 """
        if self.batterySize == 70:
            range = 240
        elif self.batterySize == 85:
            range = 270

        message = "This car can go approximately " + str(range) + " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """ 模拟电动汽车的独特之处 """
    def __init__(self, make, model, year):
        """
        初始化基类属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()