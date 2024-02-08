from computer import * # import class Computer from the computer.py file

"""
    ResaleShop is a class that simulates a computer retail store. 
"""
class ResaleShop:

    # What attributes will it need?
    inventory: list # inventory is a list that keeps track of items in the store
    inventory_count: int # keeps track of number of computers in Resale shop's inventory

    # Setting up the constructor
    def __init__(self):
        self.inventory = []
        self.inventory_count = 0 
    
    # Methods in ResaleShop class
    # buying a computer (add to inventory)     
    """
    Takes in a computer class, adds it to the inventory and returns the number of items in the inventory
    """
    def buy(self, computer: Computer):
        self.inventory.append(computer)
        self.inventory_count += 1
        return self.inventory_count
    

    # selling a computer (remove from inventory)
    """
    Takes in an item_id, removes the associated computer if it is the inventory, 
    prints error message otherwise
    """
    def sell(self, item_id: int):
        if item_id <= self.inventory_count:
            del self.inventory[item_id - 1] # I have '-1' here as the item_id counts from 1, but list index counts from 0
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    # refurbishing a computer
    """
        Updates a computer's price or operating system based on certain criteria if computer exits in the inventory. 
        Prints an error message otherwise
    """
    def refurbish(self, item_id: int, new_os: str):
        if  item_id <= self.inventory_count:
            computer = self.inventory[item_id - 1] # locate the computer
            print(new_os)
            computer.update_os(new_os) # update details after installing new OS
            if computer.year_made < 2000:
                computer.update_price(0) # too old to sell, donation only
            elif computer.year_made < 2012:
                computer.update_price(250) # heavily-discounted price on machines 10+ years old
            elif computer.year_made < 2018:
                computer.update_price(550) # discounted price on machines 4-to-10 year old machines
            else:
                computer.update_price(1000) # recent stuff
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")


