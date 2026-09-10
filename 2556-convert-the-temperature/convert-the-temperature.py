class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        a=[]
        a.append(float(celsius+273.15))
        a.append(float(celsius*1.8+32))
        return a