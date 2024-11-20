# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:20:26 2024

@author: Chieh-Yin
"""
#Hatchery class (supplies, cash ,technicians):
class Hatchery:
    def __init__(self, cash, tech_count, tech_list = None):
        self.supply = {'fertilizer' : {'origin':30, 'main':20, 'aux':10, 'depre':0.4, 'warehouse':0.1},
                       'feed' : {'origin':600, 'main':400,'aux':200, 'derpe':0.1,'warehouse': 0.001},
                       'salt' : {'origin':300, 'main':200,'aux':100, 'depre':0,'warehouse': 0.001}
                       }
        self.cash = cash #cash balance
        self.tech_count = tech_count #the number of current technicians
        if tech_list:
            self.tech_list = tech_list
        else:
            self.tech_list = []                     
                
    #Supply
    def supply(self, origin, main, aux, depre, warehouse ):
        self.origin = origin
        self.main = main
        self.aux = aux
        self.depre = depre
        self.warehouse = warehouse
        self.supply = (origin, main, aux, depre, warehouse)

    

    #Cash

    def cost (self): #計算成本
        """ 成本包含 1500,technicians warehouse cost 跟補滿warehouse的錢 """
        #self.cost = 1500 + (tech_count*500) + (warehouse.fertilizer*(origin-usage))+ (warehouse.feed*(origin-usage)) + (warehouse.salt*(origin-usage))
        base_cost = 1500
        tech_cost = self.tech_count * 6000 #一季的薪水
        warehouse_fee = 0 
        warehouse_add = 0 #補滿warehouse的錢
        total_cost = base_cost +tech_cost + warehouse_fee+ warehouse_add
        return total_cost
    
    def money (self, sell, price): #計算當前現金餘額(cash)
        profit = sell * price
        total_cost = self.cost()
        self.cash += profit-total_cost
        return self.cash
    
    #Technician
    def decide_tech(self, tech_change):
        self.tech_count += tech_change
        return self.tech_count
    
    def current_technician(self, tech_change, tech_list):
        """
        tech_change : the number of technicians who are hired or fired in this quarter(+/-)
        tech_list :the list which contains names of all technicians (updated every quarter)
        """
        if tech_change > 0:
            for i in range(tech_change):
                name_add = input('Please enter name of new technician.')
                self.tech_list.append(name_add)
        elif tech_change < 0:
            for i in range(abs(tech_change)):
                if self.tech_list:
                    name_remove = input("Please enter the name of the technicians you'd like to remove :")
                    if name_remove in tech_list:
                        self.tech_list.remove(name_remove)
                       
                    else: #如果name_remove不在list
                        print('Technician',name_remove,'is not in the Technician list. Please check the name again!')
                        print('Here are the technicians in last quarter:',tech_list)
                            #except ValueError:
                            #print('Please enter a name on the technician list.',tech_list)
                else: #如果list是空的
                    print('The Technician list is empty!')
                    break
    
    def workload(self):
        total_workload = self.tech_count * 9
        return total_workload