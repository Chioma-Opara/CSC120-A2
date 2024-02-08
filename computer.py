from typing import Optional

'''
    Computer class defines a Computer object and allows the price and operating system of a computer to be updated
'''
class Computer:

    # What attributes will it need?
    description: str 
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system:str
    year_made: int
    price: int

    # Computer class constructor: contains information about the computer's specifications
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
        self.description = description 
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price


    # Methods in Computer class
    
    # updates the price of a computer
    def update_price(self, new_price: int):
        self.price = new_price

    # updates the operating system of a computer
    def update_os(self, new_os: Optional[str] = None):
        if new_os is not None:
            self.operating_system = new_os



