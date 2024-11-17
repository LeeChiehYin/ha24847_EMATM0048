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
tech_list = []
#import Hatchery from Hatchery.py
#hatchery = Hatchery(cash=10000,tech_count=0)

for quarter_count in range(1, quarter + 1):
    print('{:=^50s}'.format('STIMULATING quarter'+str(quarter_count)))
    print('{:=^50s}'.format(''))
    
    #Technician
    while True:
        try:
            tech = int(input('To add enter positive, to remove enter negtive, no change enter 0.\n>>>Please enter number of technicians:'))
            
            new_tech_count = tech_count + tech #先建一個new避免規定外呃數值被算入正式tech           
            if new_tech_count < 1:
                print('You need at least 1 technicains in tis quarter.')
            elif new_tech_count > 5:
                print('Sorry, you cannot hire more than 5 technicians.')
            else:
                if tech > 0: # 當新增的tech為正數，詢問新進tech name
                    for i in range(tech):
                        name_add = input('Please enter name of new technician.')
                        tech_list.append(name_add)
                        
                        
                elif tech < 0: #當新增的tech為負數，詢問要移除的tech_name
                   for i in range(abs(tech)): #abs=絕對值，表示要叫出tech_list的次數
                       if tech_list:
                           #while True:
                           name_remove = input("Please enter the name of the technicians you'd like to remove :")
                           if name_remove in tech_list:
                               tech_list.remove(name_remove)
                              
                           else: #如果name_remove不在list
                               print('Technician',name_remove,'is not in the Technician list. Please check the name again!')
                               print('Here are the technicians in last quarter:',tech_list)
                                   #except ValueError:
                                   #3print('Please enter a name on the technician list.',tech_list)
                       else: #如果list是空的
                           print('The Technician list is empty!')
                           break
                       
                tech_count = new_tech_count
                #print('Current number of technicians:', tech_count)
                #print('Current Technicain list:', tech_list)
                for name in tech_list:
                    print('Hired',name,'weekly rate = 500 in quarter', quarter_count)
                break
           
        except ValueError:
             print('Please enter an integer number.')
             
      
            