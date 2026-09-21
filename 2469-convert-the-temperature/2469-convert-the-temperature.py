class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        res=[]
        kelvin=celsius+273.15
        Fahrenheit=celsius*1.80+32.00
        res.append(kelvin)
        res.append(Fahrenheit)
        return res