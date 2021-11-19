#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'vowels' function below.
#
# The function is expected to return string of vowels present in string.
# The function accepts string, string as parameter.
#

def vowels(string):
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
            test.append(ans1)
    
    for i in range(len(test)):
        if test[i] == vowels(que[i]):
            print(T_C[i].replace('.txt',':'),"pass")
            count += 1
        else:
            print(T_C[i].replace('.txt',':'),"Fail")
    if count == 10:
        print("\nCongrulation")
   
