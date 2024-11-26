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
        
        
for quarter_count in range(1, quarter + 1):  #下一個quarter從這裡開始
    print('{:=^50s}'.format(''))
    print('{:=^50s}'.format('STIMULATING QUARTER' + str(quarter_count)))
    print('{:=^50s}'.format(''))


    #Technician
    while True:
        try:
            tech_change = int(input('To add enter positive(+), to remove enter negative(-), no change enter 0.\n>>>Please enter number of technicians:'))
            new_tech_count = hatchery.tech_count + tech_change #先建一個new避免規定外呃數值被算入正式tech        
            if new_tech_count < 1: #tech number should be at least 1
                print('Invalid : You need at least 1 technician in this quarter.')
            elif new_tech_count > 5: #maxium tech number is 5 
                print('Invalid : Sorry, you cannot hire more than 5 technicians.')
            else:
                tech_count =hatchery.decide_tech(tech_change)
                s_type =hatchery.current_tech(tech_change, fish_list=fish_list)
                #hatchery.tech_special(new_tech,fish_list)
                print('Current number of technicains :', hatchery.tech_count) #test 交作業時可刪
                print('Current Technician list :', hatchery.tech_list) #test 交作業時可刪
                for tech in hatchery.tech_list:
                    print('Hired', tech['Name'], 'weekly rate = 500 in quarter', quarter_count)
                break  # Exit the technician input loop when done
        except ValueError:
            print('Please enter an integer number.')
                 
    #Fish Demand
    total_usage = {
        'fertilizer': 0,
        'feed': 0,
        'salt': 0
        }
    workload = 0
    sell_input = {} #為了輸出每個魚種user的input
    sold_list={} #被賣掉的魚種跟數量
    result = [] #為了一次性輸出結果，先把結果存起來
    x = False #資源不足的標記
      
    for fish in fish_list:
        while True:
            try:
                sell = int(input(f"Please enter how many {fish.name} you'd like to sell in the quarter (Maxium demand:{fish.limit}): "))
             
                resources = fish.fish_resource(sell)
                if resources is None:
                    continue
                
                if x:  #如果x=True 就是有資源不足，該停下
                    result.append(f"Fish {fish.name}, demand {fish.limit}, sell {sell}: 0")    
                    fish.sell = 0
                    break
                
                
                if resources:  # 如果返回有效資源需求，累加到總需求
                    new_total_usage = total_usage.copy()
                    new_total_usage['fertilizer'] += resources['fertilizer usage']
                    new_total_usage['feed'] += resources['feed usage']
                    new_total_usage['salt'] += resources['salt usage']
                    new_workload = workload + resources['maintenance']
                    
                    enough, x_resource, x_work, tech_work, remainings = hatchery.check(new_total_usage, new_workload, fish)
                    print(f"Type of remainings after check call: {type(remainings)}, Value: {remainings}")
                    if x_work: #人力不足
                       result.append(f"Fish {fish.name}, demand {fish.limit}, sell {sell}: 0")
                       result.append(f"Insufficient labor: required {new_workload-workload} weeks, available {tech_work}")
                       result.append("Insufficient ingredients:")
                       
                       for r in remainings:  # 問題的地方
                           print(f"Iterating over: {r}")
                           need = resources[r + ' usage']
                           result.append(f"  {r} need {need}, storage {remainings[r]+need}")

                       fish.sell = 0
                       x = True
                       break  
                        
                    elif x_resource:#資源不足
                        result.append(f"Fish {fish.name}, demand {fish.limit}, sell {sell}: 0")
                        result.append("Insufficient ingredients:")
                        for r in x_resource:
                            need = resources[r + ' usage']
                            result.append(f"  {r} shortage: need {need}, available {hatchery.supply[r]['origin']-total_usage[r]}")
                        fish.sell = 0 
                        x = True
                        break
                  
                    
                    else: #如果資源夠，就讓加進total usage
                         total_usage =new_total_usage
                         fish.sell =sell
                         workload = new_workload
                         result.append(f"Fish {fish.name}, demand {fish.limit}, sell {sell}: {fish.sell}")
                         print('Resources needed:', total_usage)
                         print('Labor needed:', workload)
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
    print(sold_list)               

    #Showing weekly and quarterly salary
    for name in hatchery.tech_list:
        print('Paid', name, 'weekly rate = 500, amount 6000' )
    print('Paid rent/utilities 1500')
    
    
    
    #Warehouse cost
    usage,remaining,wh_main_c, wh_aux_c,wh_c = hatchery.warehouse_use(total_usage)
    print(usage) #test
    print("Remaing:", remaining)#test
    print(total_usage)#test
    for r, remain in remaining.items():#test
        print(r, 'remaining:', remain)#test
    for r, use in usage.items(): # 輸出每個資源的使用情況#test
        print('Usage of', r, ': Main used:', use['main_use'], ', Aux used:', use['aux_use'])#test
    #for resource, cost in wh_main_c.item():
    for r,cost in wh_main_c.items():
        print('Warehouse Main:',r,'cost',cost ) #四捨五入到小數點第二位
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
  
    tech_cost = hatchery.tech_count * 6000 #一季的薪水
    wh = wh_c #warehouse cost
    wh_r = 0#補滿warehouse的錢
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
            print(s,s,'Technician', name, 'weekly rate=500')
    
        print('END OF QUARTER', quarter_count)
    


    