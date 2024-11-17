# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:36:25 2024

@author: Chieh-Yin
"""

#Fish type class
class Fish :
    def __init__(self, name, fertilizer, feed, salt, maintenance, limit, price):
        self.name = name
        self.fertilizer = fertilizer
        self.feed = feed
        self.salt = salt
        self.maintenance = maintenance
        self.limit = limit
        self.price = price
    
    def fish_resource(self, sell):
        if sell > self.limit:
            print(sell, 'exceeds the limit for', self.name)
        return {
            'fertilizer': sell * self.fertilizer,
            'feed': sell * self.feed,
            'salt': sell* self.salt
            }


#cf = Fish('Clef Fins', 0.1, 12, 2, 2, 25, 250)
#ts = Fish('Timpani Snapper', 0.05, 9, 2, 1, 10, 350)
#ab = Fish('Andalusian Brim', 0.09, 6, 2, 0.5, 15, 250)
#pc = Fish('Plagal Cod', 0.1, 10, 2, 2, 20, 400)
#ff = Fish('Fugue Flounder', 0.2, 12, 2, 2.5, 30, 550)
#mb = Fish('Modal Bass', 0.3, 12, 6, 3, 50, 500)

