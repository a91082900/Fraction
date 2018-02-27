from math import gcd

class Fraction:
    def __init__(self, numerator, denominator=1):
        if isinstance(numerator, float): # process with float
            while not numerator.is_integer():
                numerator *= 10
                denominator *= 10
            numerator = int(numerator)
            
        f_gcd = gcd(numerator, denominator)
        if denominator == 0:
            raise ValueError("demoninator can't be 0")
        if (numerator < 0) ^ (denominator < 0):
            numerator = abs(numerator)
            denominator = -1*abs(denominator)
        else:
            numerator = abs(numerator)
            denominator = abs(denominator)
        self.n = numerator // f_gcd
        self.d = denominator // f_gcd
        
    def toFraction(self, obj):
        if isinstance(obj, float) or isinstance(obj, int):
            obj = Fraction(obj)
        return obj

    def __str__(self):
        return "{}/{}".format(self.n, self.d)
    
    def __repr__(self):
        return "Fraction({}, {})".format(self.n, self.d)
    
    def __add__(self, other): # + operator
        other = self.toFraction(other)
        d = self.d * other.d // gcd(self.d, other.d) # lcm
        
        return Fraction(self.n*(d//self.d) + other.n*(d//other.d), d)
    def __sub__(self, other): # - operator
        other = self.toFraction(other)
        return self + Fraction(other.n, -1*other.d) # 加相反數

    def __mul__(self, other): # * operator
        other = self.toFraction(other)
        return Fraction(self.n*other.n, self.d*other.d)
    
    def __truediv__(self, other): # / operator
        other = self.toFraction(other)
        return self * Fraction(other.d, other.n) # 乘倒數
    
    def __pow__(self, y): # ** operator
        return Fraction(self.n**y, self.d**y)
