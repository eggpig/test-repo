# �ļ� car2.py


""" һ�������ڱ�ʾ�������� """
""" һ�����ڱ�ʾȼ�������͵綯�������� """

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
        """ ��ӡһ����Ϣ��ָ����������� """
        print("This car has " + str(self.odometerReading) + " miles on it.")

    def updateOdometer(self, mileage):
        """
        ����̱��������Ϊָ����ֵ
        �ܾ�����̱����ص�
        """
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print("You can't roll back an odometer!")

    def incrementOdometer(self, miles):
        """ ����̱��������ָ������ """
        self.odometerReading += miles

class Battery():
    """ һ��ģ��綯������ƿ�ļ򵥳��� """
    def __init__(self, batterySize=70):
        """ ��ʼ����ƿ���� """
        self.batterySize = batterySize

    def describeBattery(self):
        """ ��ӡһ��������ƿ������Ϣ """
        print("This car has a " + str(self.batterySize) + "-kwh battery.")

    def getRange(self):
        """ ��ӡһ��������ƿ������̵���Ϣ """
        if self.batterySize == 70:
            range = 240
        elif self.batterySize == 85:
            range = 270

        message = "This car can go approximately " + str(range) + " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """ ģ��綯�����Ķ���֮�� """
    def __init__(self, make, model, year):
        """
        ��ʼ���������ԣ��ٳ�ʼ���綯�������е�����
        """
        super().__init__(make, model, year)
        self.battery = Battery()