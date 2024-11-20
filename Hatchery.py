# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:20:26 2024

@author: Chieh-Yin
"""
#Hatchery class (supplies, cash ,technicians):
class Hatchery:
    def __init__(self, supply, cash, tech_count):
        self.supply = {'fertilizer' : {'origin':30, 'main':20, 'aux':10, 'depre':0.4, 'warehouse':0.1},
                       'feed' : {'origin':600, 'main':400,'aux':200, 'derpe':0.1,'warehouse': 0.001},
                       'salt' : {'origin':300, 'main':200,'aux':100, 'depre':0,'warehouse': 0.001}
                       }
        self.cash = cash #cash balance
        self.tech_count = tech_count #the number of current technicians
    
    #Supply
    def supply(self, origin, main, aux, depre, warehouse ):
        self.origin = origin
        self.main = main
        self.aux = aux
        self.depre = depre
        self.warehouse = warehouse
        self.supply = (origin, main, aux, depre, warehouse)

    

    #Cash
    def money (self,demand, price, cost): #計算當前現金餘額
        profit = demand* price
        self.cash += profit -cost
        return self.cash

    def cost (self): #計算成本
        """ 成本包含 1500,technicians warehouse cost 跟補滿warehouse的錢 """
        #self.cost = 1500 + (tech_count*500) + (warehouse.fertilizer*(origin-usage))+ (warehouse.feed*(origin-usage)) + (warehouse.salt*(origin-usage))
        base_cost = 1500
        tech_cost = self.tech_count * 6000 #一季的薪水
        supply_cost = 0
        warehouse_fee = 0 
        warehouse_add = 0 #補滿warehouse的錢
        return self.cost

    #Technician
    def decide_tech(self,tech_count, tech):
        self.tech_count += tech
        return self.tech_count
    
    def workload(self):
        total_workload = self.tech_count * 9
        return total_workload