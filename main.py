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
from Fish_type import Fish
from Hatchery import Hatchery
hatchery = Hatchery(cash=10000,tech_count=0)

for quarter_count in range(1, quarter + 1):
    print('{:=^50s}'.format('STIMULATING quarter'+str(quarter_count)))
    print('{:=^50s}'.format(''))
    
    #Technician5
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
             
    #Fish Demand
    fish_list = Fish.fish_detail()
    for fish in fish_list:
        while True:
            try:
                sell = int(input("Please enter how much", fish.name, "you'd like to sell in the quarter"))
                if sell < 0:
                    print('Invalid : The number of fish you sell should be 0 or positive integer!')
                elif sell > fish.limit:
                    print('Exceeds the limit for', fish.name)
                else:
                    fish.sell = sell
            except ValueError:
                print("Invalid : Please enter a valid integer.")
            
            
            #cf_sell = int(input("Please enter how much 'Clef Fins' you'd like to sell in the quarter"))
            #ts_sell = int(input("Please enter how much 'Timpani Snapper' you'd like to sell in the quarter"))
            #ab_sell = int(input("Please enter how much 'Andalusian Brim' you'd like to sell in the quarter"))
            #pc_sell = int(input("Please enter how much 'Plagal Cod' you'd like to sell in the quarter"))
            #ff_sell = int(input("Please enter how much 'Fugue Flounder' you'd like to sell in the quarter"))
            #mb_sell = int(input("Please enter how much 'Modal Bass' you'd like to sell in the quarter"))  
    for fish in fish_list:
        print(fish.name, 'demand :', fish.limit, 'sell :', fish.sell, ';', fish,sell)  

    
           # for fish in fish_list:
                #print('Fish', fish.name, ', demand', fish.limit, ', sell', fish.sell, ':',  fish.limit)
    
    #Insufficient Calculation
    
    #Showing weekly and quarterly salary
    
    #Showing Paid rent/utilities 1500
    #print('Paid rent/utilities 1500')