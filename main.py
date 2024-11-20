# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:29:42 2024

@author: Chieh-Yin
"""
#Lee,Chieh-Yin
#(EMATM0048) Data Science
#Description

#Quarter, Technicains
quarter = int(input('Please enter number of quarters:'))
#tech_count = 0
from Fish_type import Fish
from Hatchery import Hatchery
hatchery = Hatchery(cash=10000, tech_list=[])

for quarter_count in range(1, quarter + 1):
    print('{:=^50s}'.format('STIMULATING quarter' + str(quarter_count)))
    print('{:=^50s}'.format(''))
    
    #Technician5
    while True:
        try:
            tech_change = int(input('To add enter positive, to remove enter negtive, no change enter 0.\n>>>Please enter number of technicians:'))
            new_tech_count = hatchery.tech_count + tech_change #先建一個new避免規定外呃數值被算入正式tech        
            if new_tech_count < 1:
                print('You need at least 1 technician in this quarter.')
            elif new_tech_count > 5:
                print('Sorry, you cannot hire more than 5 technicians.')
            else:
                hatchery.decide_tech(tech_change, tech_list = hatchery.tech_list)
                hatchery.current_technicain(tech_change, hatchery.tech_list)
                
                print('Current number of technicains :', hatchery.tech_count)
                print('Current Technician list :', hatchery.tech_list)
                for name in hatchery.tech_list:
                   print('Hired', name, 'weekly rate = 500 in quarter', quarter_count)
                   break
        except ValueError:
            print('Please enter an integer number.')
            """確定後再刪
            while True:
                try:
                    tech = int(input('To add enter positive, to remove enter negtive, no change enter 0.\n>>>Please enter number of technicians:'))
                    
                    new_tech_count = Hatchery.tech_count + Hatchery.tech #先建一個new避免規定外呃數值被算入正式tech           
                    if new_tech_count < 1:
                        print('You need at least 1 technicains in tis quarter.')
                    elif new_tech_count > 5:
                        print('Sorry, you cannot hire more than 5 technicians.')
                    else:
                        if Hatchery.tech > 0: # 當新增的tech為正數，詢問新進tech name
                            for i in range(Hatchery.tech):
                                name_add = input('Please enter name of new technician.')
                                tech_list.append(name_add)
                                
                                
                        elif tech < 0: #當新增的tech為負數，詢問要移除的tech_name
                           for i in range(abs(Hatchery.tech)): #abs=絕對值，表示要叫出tech_list的次數
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
                            print('Hired',name,'weekly rate = 500 in quarter' + str(quarter_count))
                        break"""
          
             
    #Fish Demand
    fish_instance =Fish('',0,0,0,0,0,0)
    fish_list = fish_instance.fish_detail()
    
    for fish in fish_list:
        while True:
            try:
                sell = int(input(f"Please enter how many {fish.name} you'd like to sell in the quarter :"))
                resources = fish.fish_resource(sell)
                if resources: #若返回值有效，退出迴圈
                    print(fish.name, 'Resources needed:', resources) #檢查用 交作業可刪 Insufficient
                    break
            except ValueError:
                print("Invalid : Please enter a valid integer.")
            
    for fish in fish_list:
        print(fish.name, 'demand:', fish.limit, 'sell:', fish.sell)  

    
          
    
    #Insufficient Calculation
    #or fish in fish_list:
        #f fish.maintenance , fish.fertilizer , fish.feed , fish.salt
    #Showing weekly and quarterly salary
    
    #Showing Paid rent/utilities 1500
    #print('Paid rent/utilities 1500')