# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:20:26 2024

@author: Chieh-Yin
"""
#Hatchery class (supplies, cash ,technicians)
class Hatchery:
    def __init__(self, supply, cash, tech_count):
        self.supply = {'fertilizer' = {'origin':30, 'main':20, 'aux':10, 0.4, 0.1)
    feed = (600, 400, 200, 0.1, 0.001)
    salt = (300, 200, 100, 0, 0.001)}
        self.cash = cash
        self.tech_count = tech_count
    
    #Supply
    def supply(self, origin, main, aux, depre, warehouse ):
        self.origin = origin
        self.main = main
        self.aux = aux
        self.depre = depre
        self.warehouse = warehouse
        self.supply = (origin, main, aux, depre, warehouse)

    

    #Cash
    def money (self):
        self.money = self. cash + self.profit - self.cost
        return self.money
    def profit (self):
        self.profit = Fish.demand * Fish.price
        return self.profit
    def cost (self):
        self.cost = 1500 + (tech_count*500) + (warehouse.fertilizer*(origin-usage))
               + (warehouse.feed*(origin-usage)) + (warehouse.salt*(origin-usage)

        return self.cost

    #Technician
    def decide_tech(self,tech_count):
        self.tech_count += tech
        return self.tech_count
    def workload(self):
        self.maintenance = Fish.maintenance * Fish.demand
        return self.workload