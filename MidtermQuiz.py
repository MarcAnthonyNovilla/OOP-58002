class TempConversion:
    def __init__(self, temp):
        self.__temp = temp
    def FTOC(self):
        return (self.__temp-32)*5/9
    def KTOC(self):
        return self.__temp-273.15
    def CTOF(self):
        return (self.__temp*9/5)+32
    def KTOF(self):
        return (1.8*self.__temp)-459.67
    def CTOK(self):
        return self.__temp+273.15
    def FTOK(self):
        return (self.__temp+459.67)/1.8
    def display(self):
        print(f"Your Fahrenheit to Celsius is: {self.FTOC()}")
        print(f"Your Kelvin to Celsius is: {self.KTOC()}")
        print(f"Your Celsius to Fahrenheit is: {self.CTOF()}")
        print(f"Your Kelvin to Fahrenheit is: {self.KTOF()}")
        print(f"Your Celsius to Kelvin is: {self.CTOK()}")
        print(f"Your Fahrenheit to Kelvin is: {self.FTOK()}")
Temp = TempConversion(float(input("Input a Temperature:")))
Temp.display()