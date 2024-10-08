# ------------------------------------------------->Create Classes


class Food:

    basket = {}

    def __init__(self, product, price, description):
        self.product = product
        self.price = price
        self.description = description
        self.total = self.price

    def add_to_basket(self, qty):
        self.total = self.price * qty
        if qty < 1:
            print("please input a quanity greater than zero")
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
                self.basket[self.product] = [new_qty, new_total]
            else:
                self.basket[self.product] = [qty, self.total]

    @classmethod
    def delete_from_basket(cls, key):
        del cls.basket[key]


class Burgers(Food):

    def __init__(self, product, price, description):
        super().__init__(product, price, description)
        self.product = product
        self.price = price
        self.description = description
        self.total = self.price


class Not_Burgers(Food):

    def __init__(self, product, price, description):
        super().__init__(product, price, description)
        self.product = product
        self.description = description
        self.price = price
        self.total = self.price


class Desserts(Food):

    def __init__(self, product, price, description):
        super().__init__(product, price, description)
        self.product = product
        self.description = description
        self.price = price
        self.total = self.price


class Drinks(Food):

    def __init__(self, product, price, description):
        super().__init__(product, price, description)
        self.product = product
        self.description = description
        self.price = price
        self.total = self.price


class Milkshakes(Food):

    def __init__(self, product, price, description):
        super().__init__(product, price, description)
        self.product = product
        self.description = description
        self.price = price
        self.total = self.price


# --->burger menu<---#

# Descriptions
burger_option_1_description = "As the name suggests, just a simple plain burger"
burger_option_2_description = "No veg, all the meat"
burger_option_3_description = "What can we say, this ones a beast"
chick_burger_option_1_description = "Tastes better than it sounds"
chick_burger_option_2_description = (
    "Which came first... Who cares! You get both on this one!"
)
chick_burger_option_3_description = (
    "As fiery as Mount Etna, if your up for the challenge??"
)
vegetarian_option_1_description = (
    "For those of you who like to be PC, we have a burger without the burger on it"
)
vegan_option_1_description = "For those of you who like to be really PC, we have a burger without anything on it (just to be safe)"

# Instantiate Menu
burger_option_1 = Burgers("The Simpleton", 15, burger_option_1_description)
burger_option_2 = Burgers("No Veggies Here", 20, burger_option_2_description)
burger_option_3 = Burgers("The Beefy One", 25, burger_option_3_description)
chick_burger_option_1 = Burgers(
    "Our Extra Special Fowl Burger", 15, chick_burger_option_1_description
)
chick_burger_option_2 = Burgers(
    "The Chicken Or The Egg??", 20, chick_burger_option_2_description
)
chick_burger_option_3 = Burgers(
    "Mount Etna Burger", 25, chick_burger_option_3_description
)
vegetarian_option_1 = Burgers("The PC Burger", 50, vegetarian_option_1_description)
vegan_option_1 = Burgers("The Very PC Burger", 49, vegan_option_1_description)

# --->not burger menu<---#

# Descriptions
not_burger_option_1_description = "KFC who?"
not_burger_option_2_description = "Just something we found in the canal tbh"
not_burger_option_3_description = "I dont even know what this is?"
not_burger_option_4_description = "We built a house, feel free to eat it"
not_burger_option_5_description = (
    "For those who like a bit of the garden on their plate"
)
not_burger_option_6_description = "Not Available"
not_burger_option_7_description = "Not Available"
not_burger_option_8_description = "Not Available"
not_burger_option_9_description = "Not Available"

# Instantiate Menu
not_burger_option_1 = Not_Burgers(
    "Kays Fried Chicken (K.F.C)", 15, not_burger_option_1_description
)
not_burger_option_2 = Not_Burgers(
    "Poach Of The Day", 20, not_burger_option_2_description
)
not_burger_option_3 = Not_Burgers("Smurf & Turf", 25, not_burger_option_3_description)
not_burger_option_4 = Not_Burgers(
    "Thatched Cottage Pie", 15, not_burger_option_4_description
)
not_burger_option_5 = Not_Burgers("Rabbit Food", 40, not_burger_option_5_description)
not_burger_option_6 = Not_Burgers("Not Available", 0, not_burger_option_6_description)
not_burger_option_7 = Not_Burgers("Not Available", 0, not_burger_option_7_description)
not_burger_option_8 = Not_Burgers("Not Available", 0, not_burger_option_8_description)
not_burger_option_9 = Not_Burgers("Not Available", 0, not_burger_option_9_description)


# --->dessert menu<---#

# Descriptions
dessert_option_1_description = "If you like chocolate, you've come to the right place"
dessert_option_2_description = "Our own take on Eton Mess"
dessert_option_3_description = "You'll have to wait and see what you get"
dessert_option_4_description = "Had a bad day, we'll give you ice cream"
dessert_option_5_description = (
    "As the name suggests its just a melba but not very peachy"
)
dessert_option_6_description = "Eat it before it sets"
dessert_option_7_description = "Honestly its not mud, promise"
dessert_option_8_description = "Crunchy smoothie, were not sure how it works either"
dessert_option_9_description = "Not Available"

# Instantiate Menu
dessert_option_1 = Desserts("Chocolate is Life", 15, dessert_option_1_description)
dessert_option_2 = Desserts("Eaton Trough", 20, dessert_option_2_description)
dessert_option_3 = Desserts("Golden Ticket", 25, dessert_option_3_description)
dessert_option_4 = Desserts(
    "Ice Cream For Comfort Eating", 15, dessert_option_4_description
)
dessert_option_5 = Desserts("Not Very Peachy Melba", 20, dessert_option_5_description)
dessert_option_6 = Desserts(
    "Freshly Laid Tarmac Cake", 25, dessert_option_6_description
)
dessert_option_7 = Desserts("Mud Pie", 15, dessert_option_7_description)
dessert_option_8 = Desserts("Crunchy Apple Smoothie", 20, dessert_option_8_description)
dessert_option_9 = Desserts("Not Available", 0, dessert_option_9_description)


# --->drinks menu<---#

# Descriptions
drinks_option_1_description = "One drink to rule them all"
drinks_option_2_description = "As hot as the Lone Star State"
drinks_option_3_description = "Got a serious bite to it"
drinks_option_4_description = "Don't ask"
drinks_option_5_description = "This will get you talking"
drinks_option_6_description = "Something you'd drink with you'r neighbour?"
drinks_option_7_description = "Perfect for his last night of freedom"
drinks_option_8_description = "Perfect for her last night of freedom"
drinks_option_9_description = "Apparently what Stifflers Mom drinks"

# Instantiate Menu
drinks_option_1 = Drinks("Lord Of The Drinks", 15, drinks_option_1_description)
drinks_option_2 = Drinks("Texas Heat", 20, drinks_option_2_description)
drinks_option_3 = Drinks("Rattlesnake", 25, drinks_option_3_description)
drinks_option_4 = Drinks("Baby Boomer", 15, drinks_option_4_description)
drinks_option_5 = Drinks("The Gossipmonger", 20, drinks_option_5_description)
drinks_option_6 = Drinks("The Neighbour", 25, drinks_option_6_description)
drinks_option_7 = Drinks("The Stag", 15, drinks_option_7_description)
drinks_option_8 = Drinks("The Hen", 20, drinks_option_8_description)
drinks_option_9 = Drinks("Stiflers Mom", 25, drinks_option_9_description)

# --->milkshake menu<---#

# Descriptions
milkshake_option_1_description = "Cheese, cake, milkshake"
milkshake_option_2_description = "A Fruity one"
milkshake_option_3_description = "If you like chocolate, you'll love this milkshake"
milkshake_option_4_description = (
    "Mega Chocolate Milkshake but white (we were running out of ideas)"
)
milkshake_option_5_description = "As many oreos as you can possibly fit in a milkshake"
milkshake_option_6_description = "Pretty much just a big brownie on top of a milkshake"
milkshake_option_7_description = "Milkshake with a flake in it"
milkshake_option_8_description = (
    "Who doesn't like Jamie Dodgers, broken up in a milkshake "
)
milkshake_option_9_description = "Bakewell Tart flavoured milkshake obviously"

# Instantiate Menu
milkshake_option_1 = Milkshakes(
    "Cheesecake Milkshake", 15, milkshake_option_1_description
)
milkshake_option_2 = Milkshakes(
    "Flurry Berry Milkshake", 20, milkshake_option_2_description
)
milkshake_option_3 = Milkshakes(
    "Mega Chocolate Milkshake", 25, milkshake_option_3_description
)
milkshake_option_4 = Milkshakes(
    "White Chocolate Wonderland Milkshake", 15, milkshake_option_4_description
)
milkshake_option_5 = Milkshakes(
    "Oreos Forever Milkshake", 20, milkshake_option_5_description
)
milkshake_option_6 = Milkshakes(
    "The Big Brownie Milkshake", 25, milkshake_option_6_description
)
milkshake_option_7 = Milkshakes(
    "Flakey Wakey Milkshake", 15, milkshake_option_7_description
)
milkshake_option_8 = Milkshakes("The Jamie Dodger", 20, milkshake_option_8_description)
milkshake_option_9 = Milkshakes("The Bakewell Tart", 25, milkshake_option_9_description)
