#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:56:04 2020

@author: usuario
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 10:04:14 2020

@author: usuario
"""
import random

import time
import  numpy
from  mpi4py  import  MPI 
 

 

def how_many_max_values_sequential(ar):

    #find max value of the list

    maxValue = 0

    for i in range(len(ar)):

        if i == 0:

            maxValue = ar[i]

        else:

            if ar[i] > maxValue:

                maxValue = ar[i]

    #find how many max values are in the list

    contValue = 0

    for i in range(len(ar)):

        if ar[i] == maxValue:

            contValue += 1

 

    return contValue

 

# Complete the how_many_max_values_parallel function below.

def how_many_max_values_parallel(ar):
    comm = MPI.COMM_WORLD

    rank = comm.Get_rank()

 

    if rank == 0:

        data = ar

        comm.send(data, dest=1, tag=11)

    elif rank == 1:

        data = comm.recv(source=0, tag=11)
        
        maxValue = 0
        print(ar)
        for i in range(len(ar)):
             if i == 0:

            
                 maxValue = ar[i]
             else:
                 if ar[i] > maxValue:
                     maxValue = ar[i]
        contValue = 0

        for i in range(len(ar)):
            if ar[i] == maxValue:
                contValue += 1
       
        print(contValue)
    return 0

 

if __name__ == '__main__':

   

   

    ar_count = 50

   

    #Generate ar_count random numbers between 1 and 30

    ar = [random.randrange(1,30) for i in range(ar_count)]

    inicioSec = time.time()

    resultSec = how_many_max_values_sequential(ar)

    finSec =  time.time()

   

    inicioPar = time.time()   

    resultPar = how_many_max_values_parallel(ar)

    finPar = time.time()   

   

    #print('Results are correct!\n' if resultSec == resultPar else 'Results are incorrect!\n')

    print('Sequential Process took %.3f ms with %d items\n' % ((finSec - inicioSec)*1000, ar_count))

    print('Parallel Process took %.3f ms with %d items\n' % ((finPar - inicioPar)*1000, ar_count))