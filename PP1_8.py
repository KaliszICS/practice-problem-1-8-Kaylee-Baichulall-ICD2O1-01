'''
Lesson: Boolean Logic
Author: Kaylee Baichulall
Date Created: Sept 26 2024
Date Last Edited: Sept 26 2024
'''

def q1():
  bool1 = True
  bool2 = False
  print(bool1 and bool2)
  print(bool1 or bool2)

def q2():
  userInt = input("Enter an integer: ")
  userInt = int(userInt)
  bool1 = userInt != 0
  print(bool1)

def q3():
  userInt = input("Enter a number: ")
  userInt = float(userInt)
  bool1 = userInt >= 0 and userInt <= 10
  print(bool1)

def q4():
  userFood = input("Input food: ")
  userDrink = input("Input drink: ")
  bool1 = userFood != "pizza" or userDrink != "pop"
  print(bool1)

def q5():
  userInt = input("Enter an integer: ")
  userInt = int(userInt)
  num = userInt % 2
  bool1 = num == 0
  print(f"The integer {userInt} is {bool1}.")

#Do not edit code after this
#Comment out the followwing code when running tests
'''
q1()
q2()
q3()
q4()
q5()
'''
