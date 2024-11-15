# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:29:42 2024

@author: Chieh-Yin
"""
#Lee,Chieh-Yin
#(EMATM0048) Data Science
#Description

#Quarter, Technicains
quarter = int(input('Please entr number of quarters:'))
tech_count = 0

for quarter_count in range(1, quarter + 1):
    print('{:=^50s}'.format('STIMULATING quarter'+str(quarter_count)))
    print('{:=^50s}'.format(''))
    
    #Technician
    while True:
        try:
            tech = int(input('To add enter positive, to remove enter negtive, no change enter 0.\n>>>Please enter number of technicians:')
            if 1<= tech_count+tech <=5:
                tech_count +=tech_count
        
            print('Number of technicains', tech_count)
            if tech_count < 1:
                print('You need tat least 1 technicains in tis quarter.')
            elif tech_count > 5:
                print('Sorry, you cannot hire more than 5 technicians.')
            else:
                break
         except ValueError:
             print('Please enter an integer number.')
             
print(tech_count)
      
            