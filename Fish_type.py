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
        self.sell = 0 #initializing the sell of each fish type
    
    #Initialzing all fish type and return fish list
    def fish_detail(self): 
        cf = Fish('Clef Fins', 0.1, 12, 2, 2, 25, 250)
        ts = Fish('Timpani Snapper', 0.05, 9, 2, 1, 10, 350)
        ab = Fish('Andalusian Brim', 0.09, 6, 2, 0.5, 15, 250)
        pc = Fish('Plagal Cod', 0.1, 10, 2, 2, 20, 400)
        ff = Fish('Fugue Flounder', 0.2, 12, 2, 2.5, 30, 550)
        mb = Fish('Modal Bass', 0.3, 12, 6, 3, 50, 500)
        fish_list = [cf, ts, ab, pc, ff, mb]
        return fish_list

    def fish_resource(self, sell): #要賣掉的魚會用掉多少資源 計算
        if sell > self.limit:
            print(sell, 'exceeds the limit for', self.name)
            return None # #避免被納入計算
        elif sell < 0:
            print ('Invalid : The number of fish you sell should be 0 or positive integer!')
            return None #避免被納入計算
        else:
            self.sell = sell
            return {
                'fertilizer': sell * self.fertilizer,
                'feed': sell * self.feed,
                'salt': sell* self.salt,
                'maintenance' : sell *self.maintenance /5
              }
            
    
    
#test 交作業刪
fish_instance = Fish('', 0, 0, 0, 0, 0, 0)  # 建立臨時 Fish 實例以調用 fish_detail 方法
fish_list = fish_instance.fish_detail()  # 初始化魚類型
for fish in fish_list:
    resources = fish.fish_resource(30)  # 假設每種魚賣出10條
    if resources:
        print(fish.name, 'Resources:' + str(resources))
        