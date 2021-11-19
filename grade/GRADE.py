#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
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
            qu = qu.split(' ')
            fil.close()
            for j in qu:
                q1.append(int(j))
            que.append(q1)
            
    p = os.chdir(path+'/'+folder[0])
    
    for i in os.listdir(p):
        t1=[]
        fil = open(i, 'r')
        if i.endswith('.txt'):
            ans1 = fil.read()
            ans1=ans1.split(' ')
            fil.close()
            for j in ans1:
                t1.append(int(j))
            test.append(t1)
    for i in range(len(test)):
        if test[i] == gradingStudents(que[i]):
            print(T_C[i].replace('.txt',':'),"pass")
            count += 1
        else:
            print(T_C[i].replace('.txt',':'),"Fail")
    if count == 7:
        print("\nCongrulation")
    
