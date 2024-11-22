# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:36:28 2024

@author: Chieh-Yin
"""

#Vendor class
class Vendor:
    def __init__(self, name, fertilizer_p, feed_p, salt_p):
        self.name = name
        self.fertilizer_p = fertilizer_p
        self.feed_p = feed_p 
        self.salt_p = salt_p
 
    def vendor_detail(number):
        SL = Vendor('1.Slippery Lakes', 0.3, 0.1, 0.05)
        SW = Vendor('2.Scaly Wholescaler', 0.2, 0.4, 0.25) 
        #vendor_list = [SL,SW]
        
        while True:
            print('List of Vendors:')
            print("1. Slippery Lakes")
            print("2. Scaly Wholesaler")
            
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

    