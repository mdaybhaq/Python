#using mymodule.py file
import mymodule
mymodule.say_hello('Ayub')
mymodule.say_bye('Ehsan')

#import/use specific part of code
from mymodule import person1
print(person1['age'])

#package: collection module/py files +__init__.py

#library : collection of modules and packages

#inbuilt lib
import math
A= 16
print(math.sqrt(A))

#import specific function from lib
from math import factorial
B=4 
print(factorial(B))

#import pandas as pd
import 
