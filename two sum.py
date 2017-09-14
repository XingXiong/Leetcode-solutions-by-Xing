# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 00:43:16 2017

@author: Administrator
"""
# Create a dictionary to hold the difference between the target and every element in the list we went through.
# Once we find an number which equals to this difference,then return their indices.
def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic1 = {}
        for i in range(len(nums)):
            if nums[i] in dic1:
                return([i,dic1[nums[i]]]) 
            dic1[target - nums[i]] = i
