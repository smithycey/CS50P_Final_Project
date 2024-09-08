
#------------------------------------------------->Create Classes

class Food:

    basket = {}
    
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.total = self.price

    def add_to_basket(self, qty):
        self.total = self.price * qty
        if qty < 1:
            print("please input a quanity")
        else:
            if self.product in self.basket:
                old_qty = 0
                old_total = 0
                for key, value in self.basket.items():
                    for i, value in enumerate(self.basket[key]):
                        if i == 0:
                            old_qty += value
                        else:
                            old_total += value
                new_qty = old_qty + qty
                new_total = old_total + self.total
                self.basket[self.product] = ([new_qty, new_total])
            else:
                self.basket[self.product] = ([qty, self.total])
    
    @classmethod
    def delete_from_basket(cls, key):
        del cls.basket[key]

class Burgers(Food):
    
    def __init__(self, product, price):
        super().__init__(product, price)
        self.product = product
        self.price = price
        self.total = self.price

class Not_Burgers(Food):
    
    def __init__(self, product, price):
        super().__init__(product, price)
        self.product = product
        self.price = price
        self.total = self.price

class Desserts(Food):
 
    def __init__(self, product, price):
        super().__init__(product, price)
        self.product = product
        self.price = price
        self.total = self.price

   
class Drinks(Food):
    
    def __init__(self, product, price):
        super().__init__(product, price)
        self.product = product
        self.price = price
        self.total = self.price

class Milkshakes(Food):
    
    def __init__(self, product, price):
        super().__init__(product, price)
        self.product = product
        self.price = price
        self.total = self.price

#--->burger menu
burger_option_1 = Burgers("The Simpleton", 15)
burger_option_2 = Burgers("No Veggies Here", 20)
burger_option_3 = Burgers("The Beefy One", 25)
chick_burger_option_1 = Burgers("Our Extra Special Fowl Burger", 15)
chick_burger_option_2 = Burgers("The Chicken Or The Egg??", 20)
chick_burger_option_3 = Burgers("Mount Etna Burger", 25)
vegetarian_option_1 = Burgers("The PC Burger", 50)
vegan_option_1 = Burgers("The Very PC Burger", 49)

#--->not burger menu
not_burger_option_1 = Not_Burgers("Kays Fried Chicken (K.F.C)", 15)
not_burger_option_2 = Not_Burgers("Poach Of The Day", 20)
not_burger_option_3 = Not_Burgers("Smurf & Turf", 25)
not_burger_option_4 = Not_Burgers("Thatched Cottage Pie", 15)
not_burger_option_5 = Not_Burgers("Rabbit Food", 40)
not_burger_option_6 = Not_Burgers("not burger option 6", 25)
not_burger_option_7 = Not_Burgers("not burger option 7", 15)
not_burger_option_8 = Not_Burgers("not burger option 8", 20)
not_burger_option_9 = Not_Burgers("not burger option 9", 25)

#--->dessert menu
dessert_option_1 = Desserts("Chocolate is Life", 15)
dessert_option_2 = Desserts("Eaton Trough", 20)
dessert_option_3 = Desserts("Golden Ticket", 25)
dessert_option_4 = Desserts("Ice Cream For Comfort Eating", 15)
dessert_option_5 = Desserts("Not Very Peachy Melba", 20)
dessert_option_6 = Desserts("Freshly Laid Tarmac Cake", 25)
dessert_option_7 = Desserts("Mud Pie", 15)
dessert_option_8 = Desserts("Crunchy Apple Smoothie", 20)
dessert_option_9 = Desserts("dessert option 9", 25)


#--->drinks menu
drinks_option_1 = Drinks("Lord Of The Drinks", 15)
drinks_option_2 = Drinks("Texas Heat", 20)
drinks_option_3 = Drinks("Rattlesnake", 25)
drinks_option_4 = Drinks("Baby Boomer", 15)
drinks_option_5 = Drinks("The Gossipmonger", 20)
drinks_option_6 = Drinks("The Neighbour", 25)
drinks_option_7 = Drinks("The Stag", 15)
drinks_option_8 = Drinks("The Hen", 20)
drinks_option_9 = Drinks("Stiflers Mom", 25)

#--->milkshake menu
milkshake_option_1 = Milkshakes("Cheesecake Milkshake", 15)
milkshake_option_2 = Milkshakes("Flurry Berry Milkshake", 20)
milkshake_option_3 = Milkshakes("Mega Chocolate Milkshake", 25)
milkshake_option_4 = Milkshakes("White Chocolate Wonderland Milkshake", 15)
milkshake_option_5 = Milkshakes("Oreos Forever Milkshake", 20)
milkshake_option_6 = Milkshakes("The Big Brownie Milkshake", 25)
milkshake_option_7 = Milkshakes("Flakey Wakey Milkshake", 15)
milkshake_option_8 = Milkshakes("The Jamie Dodger", 20)
milkshake_option_9 = Milkshakes("The Bakewell Tart", 25)

