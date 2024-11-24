# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:36:28 2024

@author: Chieh-Yin
"""

#Vendor class
from Hatchery import Hatchery

class Vendor:

    def __init__(self, name, fertilizer_p, feed_p, salt_p):
        self.name = name
        self.fertilizer_p = fertilizer_p
        self.feed_p = feed_p 
        self.salt_p = salt_p
        self.hatchery = Hatchery(cash=10000, tech_count=0)
        
    def vendor_detail(self):
        SL = Vendor('1.Slippery Lakes', 0.3, 0.1, 0.05)
        SW = Vendor('2.Scaly Wholescaler', 0.2, 0.4, 0.25) 
        #vendor_list = [SL,SW]
        
        while True:
            print('List of Vendors:')
            print("    1. Slippery Lakes")
            print("    2. Scaly Wholesaler")
            
            try:
                number = input('Enter number of vendor to purchase from (1 or 2): ').strip()

                if number == '1':
                    return SL 
                elif number == '2':
                    return SW 
                else:
                    print("Invalid : Please enter 1 or 2.")
            except ValueError:
                print("Invalid input: Please enter a valid number (1 or 2)")
                
    def buy (self,  remaining):

        """
        計算每個資源的購買成本。
      
        vendor: Vendor 實例，用於獲取資源價格。
        remaining: 更新後的倉庫剩餘數量。
        """
        full = {
            'fertilizer': {'main': 20, 'aux': 10},
            'feed': {'main': 400, 'aux': 200},
            'salt': {'main': 200, 'aux': 100}
        }
        
        payment =  {
            'fertilizer': {'main': 0, 'aux': 0},
            'feed': {'main': 0, 'aux': 0},
            'salt': {'main': 0, 'aux': 0}
        }

        dep,remained = self.hatchery.depreciation(remaining)
        
        for r, amount in full.items():
            print(type(amount))  # 查看 'amount' 變量的類型
            print(type(remaining))  # 查看 'remaining' 變量的類型
            print(type(dep))  # 查看 'dep' 變量的類型
            x_main = amount['main']-remaining[r]['main']+dep[r]['main']  #main需要補滿的量
            x_aux = amount['aux']-remaining[r]['aux']+dep[r]['aux']  #aux需要補滿的量
      
            
            if r == 'fertilizer':
                payment[r]['main'] = x_main *self.fertilizer_p
                payment[r]['aux'] = x_aux *self.fertilizer_p
            elif r == 'feed':
                payment[r]['main'] = x_main *self.feed_p
                payment[r]['aux'] = x_aux *self.feed_p
            elif r == 'salt':
                payment[r]['main'] = x_main * self.salt_p
                payment[r]['aux'] = x_aux *self.salt_p
   
            #remaining[r]['main'] += x_main #補滿main
            #remaining[r]['aux'] += x_aux #補滿aux
          
        return payment
    
    def reset(self, full): #下一季開始時讓remaining變成full狀態
        """
        Reset the remaining values to the full capacity for the next season.
        """
        for resource in full:
            self.remaining[resource] = {
                'main': full[resource]['main'],
                'aux': full[resource]['aux']
                }
            return self.remaining
    