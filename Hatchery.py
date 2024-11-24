# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:20:26 2024

@author: Chieh-Yin
"""
#Hatchery class (supplies, cash ,technicians):
import math #為了無條件進位depreciation
#from Fish_type import Fish

class Hatchery:
    def __init__(self, cash, tech_count, tech_list = None):
        self.supply = {'fertilizer' : {'origin':30, 'main':20, 'aux':10, 'depre':0.4, 'warehouse':0.1},
                       'feed' : {'origin':600, 'main':400,'aux':200, 'depre':0.1,'warehouse': 1},
                       'salt' : {'origin':300, 'main':200,'aux':100, 'depre':0,'warehouse': 1}
                       }
        self.cash = cash #cash balance
        self.tech_count = tech_count #the number of current technicians
        if tech_list :
            self.tech_list = tech_list
        else:
            self.tech_list = []                     

    def hatchery_name():
        while True:
            h_name = input('Please enter your Hatchery name :').strip()
            if not h_name: #無效輸入
                print('Invaild: Please enter a name for your Hatchery!')
            else:
                h_name = h_name[0].upper() + h_name[1:]
                return h_name

    #Technician
    def decide_tech(self, tech_change):
        self.tech_count += tech_change
        return self.tech_count
    
    """def tech_special(self):
        #是否要有specialize技能
        decide = input('Would you like to add specialized skill on this worker? (1=Yes, 2=No)')
        #要怎樣的技能(maintenance*2/3)
         while True:
             if decide = 1: #如果同意專精
                 print('Please choose a fish type to specialize.')
                 s_type = input()
                 if s_type in fish_list:
                     maintenance"""
    
    def current_tech(self, tech_change, tech_list):
        """
        tech_change : the number of technicians who are hired or fired in this quarter(+/-)
        tech_list :the list which contains names of all technicians (updated every quarter)
        """
        if tech_change > 0:
            for i in range(tech_change):
                name_add = input('Please enter name of new technician.').strip().capitalize() #縮排，首字大寫
                self.tech_list.append(name_add)
        elif tech_change < 0:
            for i in range(abs(tech_change)):
                if self.tech_list:
                    while True:
                        name_remove = input("Please enter the name of the technicians you'd like to remove :").strip().capitalize()
                        if name_remove in tech_list:
                            print('Let go', name_remove,', weekly rate=500 in this quarter')
                            self.tech_list.remove(name_remove)
                            break
                        else: #如果name_remove不在list
                            print('Technician',name_remove,'is not in the Technician list. Please check the name again!')
                            print('Here are the technicians in last quarter:',tech_list)
                                #except ValueError:
                                #print('Please enter a name on the technician list.',tech_list)
                else: #如果list是空的
                    print('The Technician list is empty!')
                    break

    #check work and resource
    def check(self,total_usage,workload):
        x_resource = [] #make a list of insufficient resource
        remainings ={}
        tech_work = self.tech_count * 9
        x_work = False #人力是否不足
        
        #resource check
        for r, need in total_usage.items(): #能用的資源跟需要的
            if r in self.supply:
                remaining =self.supply[r]['origin'] - need
                remainings[r] = remaining
                if remaining<0: #資源不足
                    x_resource.append(r)
       
        #work check
        if workload > tech_work: #如果工作量大於tech工作
            x_work= True
            
        enough = not x_resource and not x_work
        return enough,x_resource,x_work,tech_work,remainings
       
        
    #warehouse cost    
    def  warehouse_use(self, total_usage):
       usage = {
            'fertilizer': {'main_use': 0, 'aux_use': 0},
            'feed': {'main_use': 0, 'aux_use': 0},
            'salt': {'main_use': 0, 'aux_use': 0}
            }
       remaining ={
            'fertilizer':{'main':20,'aux':10},
            'feed':{'main':400,'aux':200},
            'salt':{'main':200,'aux':100}
            }
       
    
       
       for resource in total_usage: #從total_usage找資料
           if resource in remaining: #如果remaining裡有這類資料
               amount = total_usage[resource]
        
               if amount > remaining[resource]['main']: #如果總量大於main庫存
                   usage[resource]['main_use'] = remaining[resource]['main'] #main全部用完
                   remaining[resource]['main'] = 0 #用完了

                   r_amount = amount - usage[resource]['main_use'] #剩下的(r_amount)為總量-main庫存
                   if r_amount <= remaining[resource]['aux']: #如果剩下的量小於等於aux庫存(絕對的)
                       usage[resource]['aux_use'] = r_amount #aux的用量就是剩下的量
                       remaining[resource]['aux'] -= r_amount #aux剩下的量為扣掉剩下的總量後的值
                   else:  # 如果辅助库存不足
                       usage[resource]['aux_use'] = remaining[resource]['aux']
                       remaining[resource]['aux'] = 0
                       
               else:#如果總量小於等於main庫存
                   usage[resource]['main_use'] = amount #aux的用量就是總量
                   remaining[resource]['main'] -= amount #main剩下的量為扣掉總量後的值
       
       #warehouse cost 
       wh_main_c={}
       wh_aux_c={}
       wh_c=0
               
       for r, remain in remaining.items():
           if r in self.supply:
               main_c = round(self.supply[r]['warehouse'] * remain['main'],2)
               aux_c = round(self.supply[r]['warehouse'] * remain['aux'],2)
               
               wh_main_c[r]=main_c
               wh_aux_c[r]=aux_c
               
               wh_c += main_c + aux_c  
    
       return usage, remaining, wh_main_c, wh_aux_c, wh_c

 
        
   #warehouse depreciation
    def depreciation(self, remaining):
        d = {}
        remained ={} #remmain被depr過
        for r, amount in remaining.items():
            if r in self.supply:
                main_d = math.ceil(self.supply[r]['depre'] * amount['main']) #依照規定depreciation要無條件進位成整數
                aux_d = math.ceil(self.supply[r]['depre'] * amount['aux']) 
                
                d[r] ={
                    'main' : main_d,
                    'aux': aux_d,                 
                    }
                
        for r in d:
            remained[r]={
                'main': remaining[r]['main'] - d[r]['main'],
                'aux': remaining[r]['aux'] - d[r]['aux']  
                }
            
        return d, remained
            
    def bankrupt_count(self, payment, wh_r):
        owe = []  #紀錄錢不夠
        n = self.cash + wh_r  
        zero = False  # 是否小於零
    
        #處理main
        for i, wh in payment.items(): #warehouse ingredient
            if wh['main'] > 0:  # 如果 main 有需求
                if n >=wh['main']:  # 足夠支付
                    n -= wh['main']  # 扣款
                    wh['main'] = 0
                else:  # 资金不足，无法支付
                    owe.append(
                        f"Can't restock {i}, insufficient funds, need {round(wh['main'],2)} from main but only have {round(n,2)}"
                    ) 
                    owe.append(f"Went bankrupt restocking warehouse Main")
                    zero = True  # 小於零
                    break
    
        #如果還是正數就進入處理aux
        if not zero:  # 只有當 main 階段沒小於零時才進入 aux
            for i, wh in payment.items(): #warehouse ingredient
                if wh['aux'] > 0:  # 如果 aux 有需求
                    if n >= wh['aux']:  
                        n -= wh['aux']  
                        wh['aux'] = 0
                    else:  #資金不足
                        owe.append(
                            f"Can't restock {i}, insufficient funds, need {round(wh['aux'],2)} from aux but only have {round(n,2)}"
                        )
                        owe.append(f"Went bankrupt restocking warehouse Aux")
                        break  
        for text in owe:
            print(text)
        return n

    def bankrupt (self,h_name, n, remained):
        s = ' '*4
        print('Hatchery Name:',h_name, 'Cash Balance :', round(n,2)) 
        print(s,'Warehouse Main') 
        for i, number in self.supply.items():
            if i in remained:
                print(s,s,i.capitalize(), remained[i]['main'], '(capacity =', number['main'], ')')
        print(s,'Warehouse Auxiliary')
        for i, number in self.supply.items():
            if i in remained:
                print(s,s,i.capitalize(), remained[i]['aux'], '(capacity =', number['aux'], ')')
        print(s,'Technicians')
        for name in self.tech_list:
            print(s,s,'Technician', name, 'weekly rate=500')  
  

    
    
    
        
        
       
            
        

        
                
        