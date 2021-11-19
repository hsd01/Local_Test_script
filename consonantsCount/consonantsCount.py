#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'consonantsCount' function below.
#
# The function is expected to return total number integer of consonants present in string.
# The function accepts string, string as parameter.
# function should return total count of consonants in int
#

def consonantsCount(string):
    # Write your code here
    
    
# donot make any change below if __name__ == '__main__': 
if __name__ == '__main__':
    count = 0
    folder = []
    for i in os.listdir():
        if i.endswith('.py') or i.endswith('.txt') or i.endswith('.pdf'):
            pass
        else:
            folder.append(i)
    path = os.getcwd()
    os.chdir(folder[1])
    test = []
    que = []
    T_C = []
    for i in os.listdir():
        q1=[]
        fil = open(i, 'r')
        if i.endswith('.txt'):
            T_C.append(i)
            qu = fil.read()
            que.append(qu)           
    p = os.chdir(path+'/'+folder[0])
    
    for i in os.listdir(p):
        t1=[]
        fil = open(i, 'r')
        if i.endswith('.txt'):
            ans1 = fil.read()
            fil.close()
            test.append(int(ans1))
    
    for i in range(len(test)):
        if test[i] == consonantsCount(que[i]):
            print(T_C[i].replace('.txt',':'),"pass")
            count += 1
        else:
            print(T_C[i].replace('.txt',':'),"Fail  X")
    if count == 12:
        print("\nCongrulation")
   
