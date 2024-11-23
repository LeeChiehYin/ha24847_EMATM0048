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
from Vendor import Vendor
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
    if hatchery.cash>0:
        print('{:=^50s}'.format(''))
        print('{:=^50s}'.format('STIMULATING QUARTER' + str(quarter_count)))
        print('{:=^50s}'.format(''))
    else:
        print('{:=^50s}'.format('FINAL STATE QUARTER' + str(quarter_count)))
    
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
                hatchery.current_tech(tech_change, tech_list = hatchery.tech_list)
                
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
        'fertilizer': 0,
        'feed': 0,
        'salt': 0
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
                    new_total_usage['fertilizer'] += resources['fertilizer usage']
                    new_total_usage['feed'] += resources['feed usage']
                    new_total_usage['salt'] += resources['salt usage']
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
    #for resource, remain in remaining.items():
        #print(resource, 'need', [resource], 'storage', remain) not work

    
    #Showing weekly and quarterly salary
    for name in hatchery.tech_list:
        print('Paid', name, 'weekly rate = 500, amount 6000' )
    print('Paid rent/utilities 1500')
    
    
    
    #Warehouse cost
    #hatchery = Hatchery()
    usage,remaining,wh_main_c, wh_aux_c = hatchery.warehouse_use(total_usage)
    print(usage) #test
    print("Remaing:", remaining)#test
    print(total_usage)#test
    for resource, remain in remaining.items():#test
        print(resource, 'remaining:', remain)#test
    for resource, use in usage.items(): # 輸出每個資源的使用情況#test
        print('Usage of', resource, ': Main used:', use['main_use'], ', Aux used:', use['aux_use'])#test
    #for resource, cost in wh_main_c.item():
    print('Warehouse Main cost:', wh_main_c) #四捨五入到小數點第二位
    print('Warehouse Auxilliary cost:', wh_aux_c)
            
    #Choosing Vendors 
    vendor_instance = Vendor('', 0, 0, 0)
    select = vendor_instance.vendor_detail()
    print('Select:', select.name)
    payment = select.buy(remaining)
    print("payment:", payment) #test
    #Hatchery name
    new_balance = hatchery.balance()
    h_name = Hatchery.hatchery_name()
    print('Hatchery Name:',h_name, 'Cash Balance :', hatchery.cash) 
    
    #warehose refill
    print('Warehouse Main') 
    for item, number in hatchery.supply.items():
            print(item.capitalize(), number['main'] , '(capacity =', number['main'], ')')
    print('Warehouse Auxilliary')
    for item, number in hatchery.supply.items():
        print(item.capitalize(), number['main'], '(capacity =', number['main'], ')')

    print('Technicians')
    for name in hatchery.tech_list:
        print('Technician', name, 'weekly rate=500')

    print('END OF QUARTER', quarter_count)


    