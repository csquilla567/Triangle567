# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
        
    def testNotTriangle1(self): 
        self.assertEqual(classifyTriangle(10, 15, 30), 'NotATriangle', '10,15,30 is Invalid')
       
    def testNotTriangle2(self): 
        self.assertEqual(classifyTriangle(8, 8, 16), 'NotATriangle', '8,8,16 is Invalid')
        
    def testNotTriangle3(self): 
        self.assertEqual(classifyTriangle(6, 13, 6), 'NotATriangle', '6,13,6 is Invalid')
        
    def testNotTriangle4(self): 
        self.assertEqual(classifyTriangle(7, 20, 7), 'NotATriangle', '7,20,7 is Invalid')
        
    def testNotTriangle5(self): 
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1,2,3 is Invalid')
        
    def testNotTriangle6(self): 
        self.assertEqual(classifyTriangle(1, 3, 2), 'NotATriangle', '1,3,2 is Invalid')
        
    def testNotTriangle7(self): 
        self.assertEqual(classifyTriangle(2, 1, 3), 'NotATriangle', '2,1,3 is Invalid')
        
    def testNotTriangle8(self): 
        self.assertEqual(classifyTriangle(2, 3, 1), 'NotATriangle', '2,3,1 is Invalid')
        
    def testNotTriangle9(self): 
        self.assertEqual(classifyTriangle(3, 1, 2), 'NotATriangle', '3,1,2 is Invalid')
        
    def testNotTriangle10(self): 
        self.assertEqual(classifyTriangle(3, 2, 1), 'NotATriangle', '3,2,1 is Invalid')
        
    
    def testEquilateral1(self): 
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 is Equilateral')
    
    def testEquilateral2(self):
        self.assertEqual(classifyTriangle(2, 2, 2), 'Equilateral', '2,2,2 is Equilateral')
    
    def testEquilateral3(self):
        self.assertEqual(classifyTriangle(100, 100, 100), 'Equilateral', '100,100,100 is Equilateral')
    
    def testEquilateral4(self):
        self.assertEqual(classifyTriangle(13, 13, 13), 'Equilateral', '13,13,13 is Equilateral')
    
    def testEquilateral5(self):
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral', '10,10,10 is Equilateral')
    
    
    def testIsosceles1(self): 
        self.assertEqual(classifyTriangle(10, 15, 15), 'Isosceles', '10,15,15 is Isosceles')
        
    def testIsosceles2(self):    
        self.assertEqual(classifyTriangle(20, 15, 20), 'Isosceles', '20,15,20 is Isosceles')
        
    def testIsosceles3(self):    
        self.assertEqual(classifyTriangle(5, 5, 3), 'Isosceles', '5,5,3 is Isosceles')
        
    def testIsosceles4(self):    
        self.assertEqual(classifyTriangle(5, 3, 5), 'Isosceles', '5,3,5 is Isosceles')
        
    def testIsosceles5(self):    
        self.assertEqual(classifyTriangle(3, 5, 5), 'Isosceles', '3,5,5 is Isosceles')
    
    
    def testRight1(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')
        
    def testRight2(self):
        self.assertEqual(classifyTriangle(3, 5, 4), 'Right', '3,5,4 is a Right triangle')
        
    def testRight3(self):
        self.assertEqual(classifyTriangle(5, 4, 3), 'Right', '5,4,3 is a Right triangle')
        
    def testRight4(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')
        
    def testRight5(self):
        self.assertEqual(classifyTriangle(4, 3, 5), 'Right', '4,3,5 is a Right triangle')
        
    def testRight6(self):
        self.assertEqual(classifyTriangle(4, 5, 3), 'Right', '4,5,3 is a Right triangle')
        
    def testRight7(self):
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right', '5,12,13 is a Right triangle')
        
    def testRight8(self):
        self.assertEqual(classifyTriangle(10, 8, 6), 'Right', '10,8,6 is a Right triangle')
    
    
    def testScalene1(self):
        self.assertEqual(classifyTriangle(10, 15, 14), 'Scalene', '10,15,14 is Scalene')
        
    def testScalene2(self):
        self.assertEqual(classifyTriangle(2, 4, 5), 'Scalene', '2,4,5 is Scalene')
          
    def testScalene3(self):
        self.assertEqual(classifyTriangle(7, 6, 5), 'Scalene', '7,6,5 is Scalene')
        
    def testScalene4(self):
        self.assertEqual(classifyTriangle(4, 7, 6), 'Scalene', '4,7,6 is Scalene')
    
    def testScalene5(self):    
        self.assertEqual(classifyTriangle(20, 30, 15), 'Scalene', '20,30,15 is Invalid')
      
        
    def testInvalid1(self):    
        self.assertEqual(classifyTriangle(-1, 12, 14), 'InvalidInput', 'Invalid input')
    
    def testInvalid2(self):    
        self.assertEqual(classifyTriangle(200, 200, 201), 'InvalidInput', 'Invalid input')
    
    def testInvalid3(self):    
        self.assertEqual(classifyTriangle(86, 201, 150), 'InvalidInput', 'Invalid input')
    
    def testInvalid4(self):    
        self.assertEqual(classifyTriangle(250, 175, 100), 'InvalidInput', 'Invalid input')
    
    def testInvalid5(self):    
        self.assertEqual(classifyTriangle('t', 30, 15), 'InvalidInput', 'Invalid input')
    
    def testInvalid6(self):    
        self.assertEqual(classifyTriangle(20, 'p', 15), 'InvalidInput', 'Invalid input')
    
    def testInvalid7(self):    
        self.assertEqual(classifyTriangle(20, 30, 'q'), 'InvalidInput', 'Invalid input')
    
    def testInvalid8(self):    
        self.assertEqual(classifyTriangle('t','k', 'e'), 'InvalidInput', 'Invalid input')
    
    def testInvalid9(self):    
        self.assertEqual(classifyTriangle(0, 12, 14), 'InvalidInput', 'Invalid input')
    
    def testInvalid10(self):    
        self.assertEqual(classifyTriangle(5, 2, -14), 'InvalidInput', 'Invalid input')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

