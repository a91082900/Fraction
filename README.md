# Fraction
一個分數的基本 Class。可進行四則運算。

## Usage
```Python
from Fraction import Fraction

number1 = Fraction(1, 2) # 1/2
number2 = Fraction(2) # 2
number3 = Fraction(8, 13) # 8/13

number4 = Fraction.fromString('7/8') #string init supported
number5 = Fraction.fromString('8') #string init supported

print(number1 + number2) # 5/2
print(number2 - number1) # 3/2
print(number1 * number3) # 4/13
print(number1 / number3) # 13/16
print(number5 * number4) # 7
```
