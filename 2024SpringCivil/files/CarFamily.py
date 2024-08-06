# 文件 CarFamily.py

""" 汽车一族 """

class ChinaCar():
    """ 中国汽车 """
    def __init__(self, make, model, year):
        """
        初始化基类属性，再初始化中国汽车特有的属性
        """
        self.make = make
        self.model = model
        self.year = year
        self.country = "China"

    def getDescriptiveName(self):
        longName = str(self.year) + " " + self.make + " " + self.model
        return "中国汽车：" + longName

class AmericanCar():
    """ 美国汽车 """
    def __init__(self, make, model, year):
        """
        初始化基类属性，再初始化美国汽车特有的属性
        """
        self.make = make
        self.model = model
        self.year = year
        self.country = "American"

    def getDescriptiveName(self):
        longName = str(self.year) + " " + self.make + " " + self.model
        return "美国汽车：" + longName

class GermanCar():
    """ 德国汽车 """
    def __init__(self, make, model, year):
        """
        初始化基类属性，再初始化德国汽车特有的属性
        """
        self.make = make
        self.model = model
        self.year = year
        self.country = "German"

    def getDescriptiveName(self):
        longName = str(self.year) + " " + self.make + " " + self.model
        return "德国汽车：" + longName

class JapanCar():
    """ 日本汽车 """
    def __init__(self, make, model, year):
        """
        初始化基类属性，再初始化日本汽车特有的属性
        """
        self.make = make
        self.model = model
        self.year = year
        self.country = "Japan"

    def getDescriptiveName(self):
        longName = str(self.year) + " " + self.make + " " + self.model
        return "日本汽车：" + longName



