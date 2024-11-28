# Chieh-Yin   **Git Repo 網址**
## Introduction
This program simulate a fish hatchery which breeds and sells differnet fish species. Each quarter, user need to choose whether to hire/fire technicains and decide the amount of fish to sell, also user should select vendors to refill warehouses in the end of the quarter. This program will calculate the cash balance of this quarter to see if it's bankrupt.
## Code Design
### Class
1. **Hatchery**: A class displaying a hatchery with resources, cash balance, and technicians. Severakl calculations are included
   - Atttributes:
     - supply(dict): dictionary contains resource details
     - cash(float): Current cash balance of the hatchery
     - tech_count(int): number of technicians
     - tech_list(list): list of existing technicians and there specialized skill
   
2. **Fish_type**: A class with attributes for resource usage, maintenance cost, limit on sales, and price.
    - Attributes:
      - name(str): the name of each fish
      - fertilizer_usage (float): amount of fertilizer needed for each fish
      - feed_usage(int): amount of feed needed for each fish
      - salt_usage(int):amount of salt needed for each fish
      - maintenance(float): maintenance of each fish
      - limit(int): maximum number of fish that can be sold for each fish
      - price(int): selling price per fish
      - sell(int): number of fish sold
     
4. **Vendor**: A class with attributes for vendor's name and resource prices, and help to .
   - Attributes:
     - name(str): vendor's name'
     - fertilizer_p(float): price per unit of fertilizer
     - feed_p(float): price per unit of feed
     - salt_p(float): price per unit of salt
     -hatchery (Hatchery): Hatchery instance managing cash and tech count
### Method
- In Hatchery class
1. **__init__(self, cash, tech_count, tech_list = None)**: Initializes the Hatchery object with starting cash, technician count, and optional technician list.
2. **hatchery_name()**: Prompt user to enter a valid name for the hatchery.
3. **decide_tech(self, tech_change)**: Update the number of technicians based on user's input.
4. **current_tech(self, tech_change, fish_list)**: Manage technicians: hire/fire and assign specialized skills.
5. **check(self,total_usage,workload,fish_type)**: Check if there are sufficient resources and labor to meet the workload for a given fish type.
6. **warehouse_use(self, total_usage)**: Calculate the warehouse usage and the remaining stock of resources.
7. **depreciation(self, remaining)**: Calculate the depreciation and the amount left of each warehouse resource.
8. **bankrupt_count(self, payment, wh_r)**: Deduct payments for warehouse resources and checks if it's bankrupted
9. **bankrupt (self,h_name, n, remained)**: Show Hatchery name, remaining resources in both warehouses, and technician hired. 

- InFish_type class
1. **__init__(self, name, fertilizer_usage, feed_usage, salt_usage, maintenance, limit, price)**: Initializes fish with its attributes.
2. **fish_detail(self)**: Set up and return a list which contains all fish types.
3. **fish_resource(self, sell)**: Calculate the resource usage and maintenance for the specified number of fish sold.
4. **earning(self)**: Calculates the total earnings based on the number of fish sold.
   
- In Vnedor class
1. **__init__(self, name, fertilizer_p, feed_p, salt_p)**: Initializes a Vendor object with specific prices for fertilizer, feed, and salt, and creates a Hatchery instance with initial cash and tech count.
2. **vendor_detail(self)**: Show vendors and allow the user to select a vendor to buy resource.
3. **buy(self, reminaing)**:Calculate how much each resource is needed to refill warehouses.
4. **reset(self, full)**: Reset the remaining values to the full capacity for the next season.
   - Parameters:
     - full(dict): A dictionary contains full capacity for each resource in main and axilliary warehouse.
   - Return:
     - self.remaining(dict): The updated remaining resources, which are set to  full capacities.
   - Note: Reset the remaining quantities of all resources ('fertilizer', 'feed', 'salt')  to the specified full values for the next season. Only if the cash balance > 0.
     
### Data Structures and Logic

## Design Choices

## How to Use

## Testing and Debuging

## Conclusion
