# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:36:28 2024

@author: Chieh-Yin
"""

#Vendor class
from Hatchery import Hatchery

class Vendor:
    """
    A class with attributes for vendor's name and resource prices, and help to .
    
    Attributes:
      name(str): vendor's name'
      fertilizer_p(float): price per unit of fertilizer
      feed_p(float): price per unit of feed
      salt_p(float): price per unit of salt
      hatchery (Hatchery): Hatchery instance managing cash and tech count
      
    """
    def __init__(self, name, fertilizer_p, feed_p, salt_p):
        """
         Initializes a Vendor object with specific prices for fertilizer, feed, and salt, 
         and creates a Hatchery instance with initial cash and tech count.
         
         Parameters:
             name(str): vendor's name
             fertilizer_p(float): price per unit of fertilizer
             feed_p(float): price per unit of feed
             salt_p(float): price per unit of salt
    
         Attributes:
             hatchery: Hatchery instance initialized with a starting cash of 10,000 and zero technicians
             
         """
        
        self.name = name
        self.fertilizer_p = fertilizer_p
        self.feed_p = feed_p 
        self.salt_p = salt_p
        self.hatchery = Hatchery(cash=10000, tech_count=0)
        
    def vendor_detail(self):
        """
        Show vendors and allow the user to select a vendor to buy resource.

        Return:
          Vendor: the selected Vendor

        Note:
          Prompt user to select vendor, and handle invalid inputs by showing error messages.
          
        """
        SL = Vendor('1.Slippery Lakes', 0.3, 0.1, 0.05)
        SW = Vendor('2.Scaly Wholescaler', 0.2, 0.4, 0.25) 
        
        while True:
            s=' '*4
            print('List of Vendors:')
            print(s,'1. Slippery Lakes')
            print(s,'2. Scaly Wholesaler')
            
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
                
    def buy(self,  remaining):

        """
        Calculate how much each resource is needed to refill warehouses.
      
        Parameters:
          remaining(dict): the remaining resources in two warehouse 
        
        Return:
          payment(dict): dictionary contains the total cost for each resource in the two warehouses
        
        Note:
          Calculate the cost based on the chosen vendor's prices.
          
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
            x_main = amount['main']-remaining[r]['main']+dep[r]['main'] 
            x_aux = amount['aux']-remaining[r]['aux']+dep[r]['aux'] 
      
            
            if r == 'fertilizer':
                payment[r]['main'] = x_main *self.fertilizer_p
                payment[r]['aux'] = x_aux *self.fertilizer_p
            elif r == 'feed':
                payment[r]['main'] = x_main *self.feed_p
                payment[r]['aux'] = x_aux *self.feed_p
            elif r == 'salt':
                payment[r]['main'] = x_main * self.salt_p
                payment[r]['aux'] = x_aux *self.salt_p
   
        return payment
    
    def reset(self, full): 
        """
        Reset the remaining values to the full capacity for the next season.
        
        Parameters:
          full(dict): A dictionary contains  full capacity for each resource in main and axilliary warehouse.

        Return:
          self.remaining(dict): The updated remaining resources, which are set to  full capacities.
        
        Note:
          Reset the remaining quantities of all resources ('fertilizer', 'feed', 'salt') 
          to the specified full values for the next season. Only if the cash balance>0.
          
        """
        for resource in full:
            self.remaining[resource] = {
                'main': full[resource]['main'],
                'aux': full[resource]['aux']
                }
            return self.remaining
    