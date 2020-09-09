import unittest

class ClassifyTriangleTestcase(unittest.TestCase):
    def testClassifyIsosceles(self):
        self.assertEquals((int(a) == int(b)), isosceles)
        self.assertEquals((int(b) == int(c)), isosceles)
        self.assertEquals((int(a) == int(c)), isosceles)
    def testClassifyEquilateral(self):
        self.assertEquals((int(a) == int(b) == int (c)), equilateral)
    def testClassifyScalene(self):
        self.assertEquals((int(a) != int(b) != int (c)), equilateral)   

print("Enter the lenghts of the triangle sides: ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a == b == c:
    print("This is an equilateral triangle!")
elif a == b or b == c or c == a:
    print("It is an isosceles triangle!")
else:
    print("It is a scalene triangle!")
