# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:29:42 2024

@author: Chieh-Yin
"""
#Lee,Chieh-Yin
#(EMATM0048) Data Science
#Description :A simulation of a fish hatchery which breeds and sells differnet fish species. 
#Each quarter, user need to choose whether to hire/fire technicains and decide the amount of fish to sell, 
#also user should select vendors to refill warehouses in the end of the quarter.
#This program will calculate the cash balance of this quarter to see if it's bankrupt.

#Quarter, Technicains
from Fish_type import Fish
from Hatchery import Hatchery
from Vendor import Vendor
hatchery = Hatchery(cash=10000, tech_count = 0, tech_list=[])
h_name = Hatchery.hatchery_name()
default = 8

fish_instance =Fish('',0,0,0,0,0,0)
fish_list = fish_instance.fish_detail()

while True: #quarter can only be a positive integar
    try:
        q_input = input('Please enter number of quarters (press enter = default[8]):')
        if not q_input:
            quarter = default
            break
        else:
            quarter = int(q_input)
            if quarter >0:
                break
            else:
                print('Invalid : The number of quarter should be positive!')
    except ValueError: # for non-numeric, tell customer to enter a valid integer float will also be classified here
        print('Invalid : Please enter a positive integer number!')
        
        
for quarter_count in range(1, quarter + 1): 
    print('{:=^50s}'.format(''))
    print('{:=^50s}'.format('STIMULATING QUARTER' + str(quarter_count)))
    print('{:=^50s}'.format(''))


    #Technician
    while True:
        try:
            tech_change = int(input('To add enter positive(+), to remove enter negative(-), no change enter 0.\n>>>Please enter number of technicians:'))
            new_tech_count = hatchery.tech_count + tech_change        
            if new_tech_count < 1:
                print('Invalid : You need at least 1 technician in this quarter.')
            elif new_tech_count > 5: 
                print('Invalid : Sorry, you cannot hire more than 5 technicians.')
            else:
                tech_count =hatchery.decide_tech(tech_change)
                s_type =hatchery.current_tech(tech_change, fish_list=fish_list)
 
                for tech in hatchery.tech_list:
                    print('Hired', tech['Name'], ', weekly rate = 500 in quarter', quarter_count)
                break  
        except ValueError:
            print('Please enter an integer number.')
                 
    #Fish Demand
    total_usage = {
        'fertilizer': 0,
        'feed': 0,
        'salt': 0
        }
    workload = 0
    sell_input = {} 
    sold_list={} 
    result = [] 
    x = False 

    for fish in fish_list:
        while True:
            try:
                sell = int(input(f"Please enter how many {fish.name} you'd like to sell in the quarter (Maxium demand:{fish.limit}): "))
             
                resources = fish.fish_resource(sell)
                if resources is None:
                    continue
                
                if x:  
                    result.append(f"Fish {fish.name}, demand {fish.limit}, sell {sell}: 0")    
                    fish.sell = 0
                    break
                
                
                if resources: 
                    new_total_usage = total_usage.copy()
                    new_total_usage['fertilizer'] += resources['fertilizer usage']
                    new_total_usage['feed'] += resources['feed usage']
                    new_total_usage['salt'] += resources['salt usage']
                    new_workload = workload + resources['maintenance']
                    
                    enough, x_resource, x_work, tech_work, remainings = hatchery.check(new_total_usage, new_workload, fish)
        
                    if x_work: 
                       result.append(f"Fish {fish.name}, demand {fish.limit}, sell {sell}: 0")
                       result.append(f"Insufficient labor: required {new_workload-workload} weeks, available {tech_work}")
                       result.append("Insufficient ingredients:")
                       
                       for r in remainings:  
        
                           need = resources[r + ' usage']
                           result.append(f"  {r} need {need}, storage {remainings[r]+need}")

                       fish.sell = 0
                       x = True
                       break  
                        
                    elif x_resource:
                        result.append(f"Fish {fish.name}, demand {fish.limit}, sell {sell}: 0")
                        result.append("Insufficient ingredients:")
                        for r in x_resource:
                            need = resources[r + ' usage']
                            result.append(f"  {r} shortage: need {need}, available {hatchery.supply[r]['origin']-total_usage[r]}")
                        fish.sell = 0 
                        x = True
                        break
                  
                    
                    else: 
                         total_usage =new_total_usage
                         fish.sell =sell
                         workload = new_workload
                         result.append(f"Fish {fish.name}, demand {fish.limit}, sell {sell}: {fish.sell}")
                    
                         if fish.name in sold_list:
                            sold_list[fish.name] += sell
                         else:
                            sold_list[fish.name] = sell
                         break
                     
                else:
                     result.append(f"Fish {fish.name}, demand {fish.limit}, sell {sell}: 0")   
                     fish.sell=0
                     break
                
            except ValueError:
                print("Invalid input: Please enter a valid integer.")
                continue     
        
    for i in result:
        print(i)          

   
    for name in hatchery.tech_list:
        print('Paid', name['Name'], 'weekly rate = 500, amount 6000' )
    print('Paid rent/utilities 1500')
    
    
    
    #Warehouse cost
    usage,remaining,wh_main_c, wh_aux_c,wh_c = hatchery.warehouse_use(total_usage)

    for r,cost in wh_main_c.items():
        print('Warehouse Main:',r,'cost',cost ) 
    for r,cost in wh_aux_c.items():
        print('Warehouse Auxilliary:',r,'cost',cost )
         
    #Choosing Vendors 
    vendor_instance = Vendor('', 0, 0, 0)
    select = vendor_instance.vendor_detail()
    print('Select:', select.name)
    payment = select.buy(remaining)
    
    #Hatchery name cash balance  
    earning = 0
    for fish in fish_list:
        if fish.name in sold_list:  
            earning += fish.price * sold_list[fish.name]
  
    tech_cost = hatchery.tech_count * 6000 
    wh = wh_c #warehouse cost
    wh_r = 0 
    for r in payment:
        wh_r+=payment[r]['main']+payment[r]['aux']
        
    change = earning - (1500 +tech_cost + wh_c+ wh_r)
    hatchery.cash += change
    
    s = ' '*4
    d,remained = hatchery.depreciation(remaining)
    
    if hatchery.cash<0: #went bankrupt
        n=hatchery.bankrupt_count(payment, wh_r) 
        hatchery.bankrupt(h_name, n, remained)
        print('END OF QUARTER', quarter_count)
        print('{:=^50s}'.format('FINAL STATE QUARTER' + str(quarter_count+1)))
        hatchery.bankrupt(h_name,n,remained)
        print('~ THE END of STIMULATION ~')
        break

    else: #still own positive cash balance
        print('Hatchery Name:',h_name, 'Cash Balance :', round(hatchery.cash,2)) 
        #warehose refill
        print(s,'Warehouse Main') 
        for item, number in hatchery.supply.items():
                print(s,s,item.capitalize(), number['main'] , '(capacity =', number['main'], ')')
        print(s,'Warehouse Auxilliary')
        for item, number in hatchery.supply.items():
            print(s,s,item.capitalize(), number['main'], '(capacity =', number['main'], ')')
    
        print(s,'Technicians')
        for name in hatchery.tech_list:
            print(s,s,'Technician', name['Name'], 'weekly rate = 500')
    
        print('END OF QUARTER', quarter_count)
    


    