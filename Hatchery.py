# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:20:26 2024

@author: Chieh-Yin
"""
#Hatchery class (supplies, cash ,technicians):
import math #為了無條件進位depreciation

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
                    name_remove = input("Please enter the name of the technicians you'd like to remove :").strip().capitalize()
                    if name_remove in tech_list:
                        print('Let go', name_remove,', weekly rate=500 in this quarter')
                        self.tech_list.remove(name_remove)
                       
                    else: #如果name_remove不在list
                        print('Technician',name_remove,'is not in the Technician list. Please check the name again!')
                        print('Here are the technicians in last quarter:',tech_list)
                            #except ValueError:
                            #print('Please enter a name on the technician list.',tech_list)
                else: #如果list是空的
                    print('The Technician list is empty!')
                    break

    #確認資源或人力到底夠不夠
    def check(self, need, workload):
        x_enough = [] #make a list of insufficient resource
        remainings ={}
        for resource, needs in need.items(): #能用的資源跟需要的
            if resource in self.supply:
                usable = self.supply[resource]['origin']
                remainings[resource] =usable - needs
                if usable <needs: #資源不足
                    x_enough.append(f"{resource} need {need}, storage {usable}")
               
    
                
        tech_work = self.tech_count * 9
        if workload > tech_work: #如果工作量大於tech工作
            x_enough.append(f"Insufficient labor: required {workload} weeks, available {tech_work - workload}")
            
        
        if x_enough:
            return False, x_enough, tech_work, remainings
        else:
            return True, [], tech_work, remainings
        
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
       wh_main_c =0
       wh_aux_c =0
               
       for r, remain in remaining.items():
           if r in self.supply:
               wh_main_c +=round(self.supply[r]['warehouse'] * remain['main'],2)#四捨五入到小數點第二位
               wh_aux_c =round(self.supply[r]['warehouse'] * remain['aux'],2)
               wh_c = wh_main_c + wh_aux_c  
    
       return usage, remaining, wh_main_c, wh_aux_c

 
        
   #warehouse depreciation
    def depreciation(self, remaining):
        
        d = {}
        for resource, amount in remaining.items():
            if resource in self.supply:
                main_d = math.ceil(self.supply[resource]['depre'] * amount['main']) #依照規定depreciation要無條件進位成整數
                aux_d = math.ceil(self.supply[resource]['depre'] * amount['aux']) 
                
                d[resource] ={
                    'main' : main_d,
                    'aux': aux_d,                 
                    }
        return d
    
    
    #Cash
    def money_change (self, earning, wh, wh_c, wh_r, payment): #計算成本
        """ 
        賺的錢就是賣出的魚*魚的金額
        成本包含 1500,technicians warehouse cost 跟補滿warehouse的錢 
        """
        #earning
        #self.cost = 1500 + (tech_count*500) + (warehouse.fertilizer*(origin-usage))+ (warehouse.feed*(origin-usage)) + (warehouse.salt*(origin-usage))
        base = 1500
        tech_cost = self.tech_count * 6000 #一季的薪水
        wh = 0 #warehouse cost
        for r in wh_c:
            wh+=sum(wh_c[r]['main']+wh_c[r]['aux'])
            
        wh_r = 0#補滿warehouse的錢
        for r in payment:
            wh_r=sum(payment[r]['main']+payment[r]['aux']) 
       
        change = earning - (base +tech_cost + wh_c+ wh_r)
        return change
    
    def balance (self): #計算當前現金餘額(cash)
        change = self.money_change()
        self.cash += change
        return self.cash
    
        """fish_sales = self.fish_type.sell #從Fish_type中獲得sell數值
        if fish_sales > 0:
            profit = fish_sales * price
            total_cost = self.cost()
            self.cash += profit-total_cost
        return self.cash"""
    
    
    
        
        
       
            
        

        
                
        