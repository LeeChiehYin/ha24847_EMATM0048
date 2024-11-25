# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:36:25 2024

@author: Chieh-Yin
"""

#Fish type class
class Fish:
    """
    A fish class with attributes for resource usage, maintenance cost, limit on sales, and price.

    Attributes:
      name(str): the name of each fish
      fertilizer_usage (float): amount of fertilizer needed for each fish
      feed_usage(int): amount of feed needed for each fish
      salt_usage(int):amount of salt needed for each fish
      maintenance(float): maintenance of each fish
      limit(int): maximum number of fish that can be sold for each fish
      price(int): selling price per fish
      sell(int): number of fish sold
    """
    def __init__(self, name, fertilizer_usage, feed_usage, salt_usage, maintenance, limit, price):
        """
        Initializes fish with its attributes..

        Parameters:
          name(str): the name of each fish
          fertilizer_usage (float): amount of fertilizer needed for each fish
          feed_usage(int): amount of feed needed for each fish
          salt_usage(int):amount of salt needed for each fish
          maintenance(float): maintenance of each fish
          limit(int): maximum number of fish that can be sold for each fish
          price(int): selling price per fish
          sell(int):number of fish sold(initialize as 0)
        """
        self.name = name
        self.fertilizer_usage = fertilizer_usage
        self.feed_usage = feed_usage
        self.salt_usage = salt_usage
        self.maintenance = maintenance
        self.limit = limit
        self.price = price
        self.sell = 0 #initializing the sell of each fish type

    
    def fish_detail(self): 
        """
        Set up and return a list which contains all fish types.
    
        Return:
         fish_list(list):a list contains all fish types
        """
        cf = Fish('Clef Fins', 0.1, 12, 2, 2, 25, 250)
        ts = Fish('Timpani Snapper', 0.05, 9, 2, 1, 10, 350)
        ab = Fish('Andalusian Brim', 0.09, 6, 2, 0.5, 15, 250)
        pc = Fish('Plagal Cod', 0.1, 10, 2, 2, 20, 400)
        ff = Fish('Fugue Flounder', 0.2, 12, 2, 2.5, 30, 550)
        mb = Fish('Modal Bass', 0.3, 12, 6, 3, 50, 500)
        fish_list = [cf, ts, ab, pc, ff, mb]
        return fish_list

    def fish_resource(self, sell):
        """
        Calculate the resource usage and maintenance for the specified number of fish sold.

        Parameters:
          sell(int):number of fish to sell
 
        Returns:
          u(dict):a dictionary with the calculated resource usage(fertilizer usage, feed usage,salt usage) and maintenance(weeks).
                  Returns None for invalid inputs
 
        Note:
          Handles invalid inputs(exceeding the fish limit or entering negative numbers and non-numeric) 
          by showing error messages.
        """
        #while True:  
            
        if sell > self.limit:
            print(sell, 'exceeds the limit for', self.name, '(Maxium demand:)', self.limit)
            return None #Avoid including in calculations
        elif sell < 0:
            print ('Invalid : The number of fish you sell should be 0 or positive integer!')
            return None 
        else:
            self.sell = sell
            u= {
             'fertilizer usage': self.fertilizer_usage *sell,
             'feed usage': self.feed_usage *sell,
             'salt usage': self.salt_usage *sell,
             'maintenance' : self.maintenance *sell/5
           }
            return u
            #except ValueError:
                #rint('Invalid : Please enter a valid integer!')
        
    def earning(self):
        """
        Calculate 
          Calculates the total earnings based on the number of fish sold.

        Returns:
            self.sell*self.price(int): total earnings of fish sold
        """
        return self.sell * self.price
        
        