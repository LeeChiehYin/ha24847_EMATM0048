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
from Fish_type import Fish
from Hatchery import Hatchery
hatchery = Hatchery(cash=10000, tech_count = 0, tech_list=[])

for quarter_count in range(1, quarter + 1):
    print('{:=^50s}'.format('STIMULATING QUARTER' + str(quarter_count)))
    print('{:=^50s}'.format(''))
    
    #Technician
    while True:
        try:
            tech_change = int(input('To add enter positive, to remove enter negtive, no change enter 0.\n>>>Please enter number of technicians:'))
            new_tech_count = hatchery.tech_count + tech_change #先建一個new避免規定外呃數值被算入正式tech        
            if new_tech_count < 1:
                print('You need at least 1 technician in this quarter.')
            elif new_tech_count > 5:
                print('Sorry, you cannot hire more than 5 technicians.')
            else:
                hatchery.decide_tech(tech_change)
                hatchery.current_technician(tech_change, tech_list = hatchery.tech_list)
                
                print('Current number of technicains :', hatchery.tech_count)
                print('Current Technician list :', hatchery.tech_list)
                for name in hatchery.tech_list:
                    print('Hired', name, 'weekly rate = 500 in quarter', quarter_count)
                break  # Exit the technician input loop when done
        except ValueError:
            print('Please enter an integer number.')
          
             
    #Fish Demand
    fish_instance =Fish('',0,0,0,0,0,0)
    fish_list = fish_instance.fish_detail()
    
    for fish in fish_list:
        while True:
            try:
                sell = int(input(f"Please enter how many {fish.name} you'd like to sell in the quarter :"))
                resources = fish.fish_resource(sell)
                
                workload_need = resources.get('maintenance', 0) #get maintenance from fish_resource
                enough, xenough = hatchery.check(resources, workload_need)
                if resources: #若返回值有效，退出迴圈
                    print(fish.name, 'Resources needed:', resources) #檢查用 交作業可刪 Insufficient
                    if not enough:
                        print('not enough to sell') #testing
                        for i in xenough:
                            print(i)
                        fish.sell = 0
                        break
                    else: #when enough
                        fish.sell = sell
                        hatchery.remain(resources, workload_need)
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