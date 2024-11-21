# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:29:42 2024

@author: Chieh-Yin
"""
#Lee,Chieh-Yin
#(EMATM0048) Data Science
#Description

#Quarter, Technicains
from Fish_type import Fish
from Hatchery import Hatchery
#from Vendor import Vendor
hatchery = Hatchery(cash=10000, tech_count = 0, tech_list=[])

while True: #quarter can only be a positive integar
    try:
        quarter = int(input('Please enter number of quarters:'))
        if quarter >0:
            break
        else:
            print('Invalid : The number of quarter should be positive!')
    except ValueError: # for non-numeric, tell customer to enter a valid integer float will also be classified here
        print('Invalid : Please enter a positive integer number!')
        
for quarter_count in range(1, quarter + 1):  #下一個quarter從這裡開始
    print('{:=^50s}'.format('STIMULATING QUARTER' + str(quarter_count)))
    print('{:=^50s}'.format(''))
    
    #Technician
    while True:
        try:
            tech_change = int(input('To add enter positive, to remove enter negtive, no change enter 0.\n>>>Please enter number of technicians:'))
            new_tech_count = hatchery.tech_count + tech_change #先建一個new避免規定外呃數值被算入正式tech        
            if new_tech_count < 1:
                print('Invalid : You need at least 1 technician in this quarter.')
            elif new_tech_count > 5:
                print('Invalid : Sorry, you cannot hire more than 5 technicians.')
            else:
                hatchery.decide_tech(tech_change)
                hatchery.current_technician(tech_change, tech_list = hatchery.tech_list)
                
                print('Current number of technicains :', hatchery.tech_count) #test 交作業時可刪
                print('Current Technician list :', hatchery.tech_list) #test 交作業時可刪
                for name in hatchery.tech_list:
                    print('Hired', name, 'weekly rate = 500 in quarter', quarter_count)
                break  # Exit the technician input loop when done
        except ValueError:
            print('Please enter an integer number.')
          
             
    #Fish Demand
    fish_instance =Fish('',0,0,0,0,0,0)
    fish_list = fish_instance.fish_detail()
    total_usage = {
        'total fertilizer usage': 0,
        'total feed usage': 0,
        'total salt usage': 0
        }
    workload = 0
    sell_input = {} #為了輸出每個魚種user的input
    

    for fish in fish_list:
        while True:
            try:
                sell = int(input(f"Please enter how many {fish.name} you'd like to sell in the quarter: "))
                resources = fish.fish_resource(sell)
                
                if resources:  # 如果返回有效資源需求，累加到總需求
                    new_total_usage = total_usage.copy()
                    new_total_usage['total fertilizer usage'] += resources['fertilizer usage']
                    new_total_usage['total feed usage'] += resources['feed usage']
                    new_total_usage['total salt usage'] += resources['salt usage']
                    new_workload = workload + resources['maintenance']
                    
                    enough, xenough, tech_work, remaining = hatchery.check(total_usage, workload)
                    if new_workload > tech_work: #人力不足
                        print('Insufficient labor: required', 'insufficient','weeks, available', tech_work - workload )
                        print('Insufficient ingredients:')
                        #for resource, remain in remaining.items():  # 使用 remaining 输出剩余资源
                            #print(resource, 'need', resources[resource], 'storage', remain)
                        fish.sell = 0   
                        sell_input[fish.name] = sell
                        break   
                    
                    elif enough:#如果資源夠，就讓加進total usage
                         total_usage =new_total_usage
                         fish.sell =sell
                         workload = new_workload
                         sell_input[fish.name] = sell
                         print('Resources needed:', total_usage)
                         print('Labor needed:', workload)
                         break
                    
                    else: #資源不足  
                        fish.sell = 0
                        sell_input[fish.name] = sell
                        for i in xenough:
                            print('You cannot sell more fish because',i)
                        print('Insufficient labour : required', workload,' weeks, available',tech_work-workload)
                        print('Insufficient ingredients:')
                        #for resource, remain in remaining.items():
                            #print(resource, 'need', resources[resource], 'storage', remain)
                        break
 

                    
                else:
                    print('Invalid: Please try again')
            except ValueError:
                print("Invalid : Please enter a valid integer.")
        
    for fish in fish_list:
        print(fish.name, 'demand:', fish.limit, 'sell:', sell_input[fish.name]  ,':', fish.sell)  
    for resource, remain in remaining.items():
        print(resource, 'need', resources[resource], 'storage', remain)   

    
    #Showing weekly and quarterly salary
    for name in hatchery.tech_list:
        print('Paid', name, 'weekly rate = 500, amount 6000' )
    print('Paid rent/utilities 1500')
    
    
    
    #Warehouse cost
    for item,number in hatchery.supply.items():
        print('Warehouse Main :', item, fish.sell*number['warehouse'])
        print('Warehouse Auxilliary :', item, number['warehouse'])
    
    #Choosing Vendors
    print('List of Vendors')
    print('1. Slippery Lakes') #改成vendor name
    print('2. Scaly Wholesaler') #改成vendor name
    vendor = input ('Enter number of vendor to purchase from:')
    print('Hatchery Name: Eastaboga, Cash: 9618.63')
 
    print('Warehouse Main')
    for item, number in hatchery.supply.items():
        print(item.capitalize(), number['main'], '(capacity =', number['main'], ')')
    print('Warehouse Auxilliary')
    for item, number in hatchery.supply.items():
        print(item.capitalize(), number['main'], '(capacity =', number['main'], ')')
    
    print('Technicians')
    for name in hatchery.tech_list:
        print('Technician', name, 'weekly rate=500')
 