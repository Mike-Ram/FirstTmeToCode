'''
This is the one that will make what kind of coffee
I will brew today every day with each brand of coffee
accompanied by flavord.
'''


import random


class Coffee:

    brand_lists = []

    def __init__(self, brand, flavor):
        self.brand = brand
        self.flavor = flavor

        Coffee.brand_lists.append(self)


    def __repr__(self) -> str:
        return f"{self.brand}: {self.flavor}"

#This is my favorite flavor of coffee in each brand
first_mixed = Coffee("Kopiko", "Black 3 in ONE")
second_mixed = Coffee("Nescafe", "Original")
third_mixed = Coffee("Great taste", "WHITE")


print("Coffee of the day is...")
print(random.choice(Coffee.brand_lists))