### Chieh-Yin
### (EMATM0048) Data Science
### My Git Repo
[Git Repo](https://github.com/LeeChiehYin/ha24847_EMATM0048)

# Fish Hatchery Simulation
## Introduction
This program simulate a fish hatchery which breeds and sells differnet fish species. Each quarter, user need to choose whether to hire/fire technicains and decide the amount of fish to sell, also user should select vendors to refill warehouses in the end of the quarter. This program will calculate the cash balance of this quarter to see if it's bankrupted.
### Main Function
- Simulate the operations over several quarters.
- Manage hiring, firing and Specializing technicians
- Calculate remaining resources and workforce.
- Calculate warehouse usage, costs, and quarterly cash balance.
- Display bankrupt situation and quarter ended processes.
## Code Design
### File
1. **main.py**: A file contains the codes of main program.
2. **Hatchery.py**: A file contains the codes of Hatchery class.
3. **Fish_type.py**: A file contains the codes of Fish_type class.
4. **Vendor.py**: A file contains the codes of Vendor class.
### Class
1. **Hatchery**: A class displaying a hatchery with resources, cash balance, and technicians. Severakl calculations are included
   - Atttributes:
     - `supply(dict)`: dictionary contains resource details
     - `cash(float)`: Current cash balance of the hatchery
     - `tech_count(int)`: number of technicians
     - `tech_list(list)`: list of existing technicians and there specialized skill
   
2. **Fish_type**: A class with attributes for resource usage, maintenance cost, limit on sales, and price.
    - Attributes:
      - `name(str)`: the name of each fish
      - `fertilizer_usage (float)`: amount of fertilizer needed for each fish
      - `feed_usage(int)`: amount of feed needed for each fish
      - `salt_usage(int)`:amount of salt needed for each fish
      - `maintenance(float)`: maintenance of each fish
      - `limit(int)`: maximum number of fish that can be sold for each fish
      - `price(int)`: selling price per fish
      - `sell(int)`: number of fish sold
     
4. **Vendor**: A class with attributes for vendor's name and resource prices, and help to .
   - Attributes:
     - `name(str)`: vendor's name'
     - `fertilizer_p(float)`: price per unit of fertilizer
     - `feed_p(float)`: price per unit of feed
     - `salt_p(float)`: price per unit of salt
     - `hatchery (Hatchery)`: Hatchery instance managing cash and tech count
### Method
- In Hatchery class
1. `__init__(self, cash, tech_count, tech_list = None)`: Initializes the Hatchery object with starting cash, technician count, and optional technician list.
2. `hatchery_name()`: Prompt user to enter a valid name for the hatchery.
3. `decide_tech(self, tech_change)`: Update the number of technicians based on user's input.
4. `current_tech(self, tech_change, fish_list)`: Manage technicians: hire/fire and assign specialized skills.
5. `check(self,total_usage,workload,fish_type)`: Check if there are sufficient resources and labor to meet the workload for a given fish type.
6. `warehouse_use(self, total_usage)`: Calculate the warehouse usage and the remaining stock of resources.
7. `depreciation(self, remaining)`: Calculate the depreciation and the amount left of each warehouse resource.
8. `bankrupt_count(self, payment, wh_r)`: Deduct payments for warehouse resources and checks if it's bankrupted
9. `bankrupt (self,h_name, n, remained)`: Show Hatchery name, remaining resources in both warehouses, and technician hired. 

- In Fish_type class
1. `__init__(self, name, fertilizer_usage, feed_usage, salt_usage, maintenance, limit, price)`: Initializes fish with its attributes.
2. `fish_detail(self)`: Set up and return a list which contains all fish types.
3. `fish_resource(self, sell)`: Calculate the resource usage and maintenance for the specified number of fish sold.
4. `earning(self)`: Calculates the total earnings based on the number of fish sold.
   
- In Vnedor class
1. `__init__(self, name, fertilizer_p, feed_p, salt_p)`: Initializes a Vendor object with specific prices for fertilizer, feed, and salt, and creates a Hatchery instance with initial cash and tech count.
2. `vendor_detail(self)`: Show vendors and allow the user to select a vendor to buy resource.
3. `buy(self, reminaing)`:Calculate how much each resource is needed to refill warehouses.
4. `reset(self, full)`: Reset the remaining values to the full capacity for the next season.
## Main Process:
1. Decide how many quarters want to stimulate.
2. Decide to hire or fire technicians.
3. **Extension**: If new technicians are hired, decide whether to specialize he/she in a specific fish (less time to sell/maintain it), and choose the species to specialized in.
4. Decide the quantity fish to sell.
5. Check if there are enough resources and workforce.
6. Display the number of fish sold, indicate any shortages in resources or workforce, and show the remaining resources and workforce.
7. Caculate and show warehouse costs (the money you pay to store resources) in both Main and Auxilliary warehouses.
8. Select a vendor to purchase resources to refill warehouse.
9. Calculate the payment of warehouse refilling and the cash balance of this quarter.
10. - If the hatchery bankrupted, showing hacthery details and cash balance, end of stimulation.
    - If not bankrupted, refilled the warehouse  and start the new quarter stimulation.
## Design Choices
## Which file to calculate the money balance?
When deciding where to calculate the cash balance, I ran into a challenge. Initially, I planned to handle it in the `Hatchery` class since it's the central hub for resource and financial management. However, calculating the quarterly cash balance requires pulling earnings (via the earning method) from the `Fish_type` class and the warehouse refilling payment (via the buy method) from the `Vendor` class. This would make the calculation process unnecessarily complicated, especially since I’d also need to call the result back into the main file. Considering this, I ultimately decided to handle the cash balance calculations directly in the main file. It simplifies the process and keeps the workflow more straightforward.

## Should numbers be allowed in the name input?
When working on debugging and error handling, I was thinking whether to restrict users from entering numbers in the name fields for the Hatchery and technicians. However, since this is just a simulation, I figured it’s acceptable for users to use a nickname or a name with numbers if they prefer. For instance, “Att4Fun” or “tech1” could work fine.

As for the hatchery name, I also considered how some real-world brands or store names might have more than one capital letter, so I decided to automatically capitalize only the first character of the name and leave the rest as the user entered it, maintaining their input style.

## How to refill the warehouses's resource to exact the same amount?
When calculating numbers like in the `depreciation method`, I noticed there are cases where rounding to two decimal places or using ceiling functions might cause slight differences. This made me worry about how to precisely refill the warehouses back to their full capacity.

To handle this, I came up with an idea: First, I calculate the this quarter's cash balance (directly deducting warehouse refilling costs). If the balance is positive, I use the `reset` method to refill the warehouses back to their full capacity, allowing the user to move on to the next quarter or finish the simulation.

However, if the cash balance is negative, I add back the warehouse refilling costs (`wh_r`) to the new cash balance(`n = self.cah +wh_r`) Then, I check how much of the remaining cash can be used to partially refill the warehouse resources. This enalbes me to meet the requirements.

