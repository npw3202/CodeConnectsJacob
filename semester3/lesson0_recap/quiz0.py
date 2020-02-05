from abc import *
# how would you write a function that continuously takes in user input, add 5 to the number, and print out the result

# def add5(number_input):
#     total = int(number_input) + 5
#     print (total)

# while True:
#     number = input("Pick a number to add 5 to.")
#     add5(number) 

# what is 3/4. How about 3 // 4. How about 3 % 4?


# Explain what the % operator does. Why is it useful


# We want to make a shape class that can calculate the area and perimiter of various shapes

# class Vehicle(ABC):
#     @abstractmethod
#     def go(self):
#         pass

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimiter(self):
        pass

class Square(shape):
    def __init__(self, length, width):
        super(Square, self).__init__()
        self.width = width
        self.length = length
        
    def area(self):
        area = self.length * self.width
        return area

    def perimiter(self):
        perimiter = 2 * self.length + 2 * self.width
        return perimiter

sq = Square(5,5)
print(sq.area())
print(sq.perimiter())
# What is the difference between a list and array. Which one is "easier" to perform random access in
# [,,,,,,,,,,,,,,,,,,,,,,,A,B,,,,,,,,,,1,2,3,4,5,,,,,,,,,,,,]
# 0x05
# 0x05 + 3 = 0x08

# dic = {}
# d['apple'] = 5
# Under the hood, what's one way of implementing a set

# What's the difference between a stack and a queue


# Implement the Ackerman Function
# https://en.wikipedia.org/wiki/Ackermann_function

# 4! = 4 * 3 * 2 * 1
# 4! = 4 * 3!
# 5! = 5 * 4!
# n! = n * (n-1)!
# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n-1)
def ackerman(m,n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackerman(m-1,1)
    else:
        return ackerman(m-1,ackerman(m,n-1))
print(ackerman(0, 0))
print(ackerman(0, 1))
print(ackerman(0, 2))
print(ackerman(0, 3))
print(ackerman(0, 5))
print(ackerman(0, 6))