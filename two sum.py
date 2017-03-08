# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 00:43:16 2017

@author: Administrator
"""
target=8
nums = [3,5,6,8]
def twoSum(nums,target):
    for i in range(0,len(nums),1):
        for j in range(i+1,len(nums),1):
            if nums[i] + nums[j] == target:
                print(i,j)
twoSum([2,4,5,7],7)

a = 124
b = a%100
print(b)

s = "Bill"
print(s[0],s[len(s) - 1])

for i in range(0, 10) :

   print("Loop Execution")
   
   counter = 1

for i in range(1, 100) :

   counter = counter + 1

print(counter)


val1 = True

val2 = False

while val1 :

      print("Hello")
      break
  
nums = (0,120,420)
print(nums[0])