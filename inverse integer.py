# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 16:09:26 2017

@author: Administrator
"""

def reverse(x):
        if x < 0:
            x = abs(x)
            b = str(x)
            a = len(b)
            c = ""
            for i in range(a-1,-1,-1):
                c = c + b[i]
            x = int(c)
            x = -x   
            if x < -2147483648:
                return(0)
            else:
                return(x)
        elif x == 0:
            return(x)
        elif x > 0:
            b = str(x)
            a = len(b)
            c = ""
            for i in range(a-1,-1,-1):
                c = c + b[i]
            x = int(c)
            if x > 2147483648:
                return(0)
            else:
                return(x)



