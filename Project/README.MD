# Kays Cafe
### Video Demo:
### Description:

Welcome to Kays Cafe!\
This project is a gui application for an online ordering system for Kays Cafe\
It allows you to access the gui interface and navigate through the various menus available to view the selection of products on offer by the cafe. You can then add any of these products to the basket, at which point you can then go to the basket, which you can edit by removing a product if you no longer require it and once satisfied with your selection you can continue through to the checkout window where you will enter your details before confirming your order. Once you have confirmed your order you will be presented with the order confirmation window which will confirm you have placed your order and that a confirmation email along with a receipt will be sent to the email address provided.

### Files:
#### project.py

#### menu.py
The purpose of this file is to keep all of the functionality surrounding creating the actual menu of products, setting the names of the items, setting the prices and storing the classes in which the menu items are instantiated and the basket is managed all in one place.\
This means that any modifications that need to be done to the menu can be done within this file, which will then be realised throughout the remainder of the project without having to navigate through the entirety of the main project file to make individual changes.

The menu.py file consists of a parent class (Food) and 5 child classes.

###### Food class:
The Food class is the parent class which both manages, records and updates the basket whilst also providing the functionality for all of the child classes.

The Food class begins with an empty dictionary named basket. This is where any items that are added to the basket will be stored in order for the project file to access later.

Next is the init method which takes in the self, product and price variables as arguments and uses them to assing the product and price instance variables. It also assigns the self.total instance variable to the same value as self.price.

Following the init method is the add_to_basket instance method which as the name suggests is used to add products to the basket dictionary referenced above. This method takes in the self and qty arguments.\
This method updates the self.total using the self.price * qty, it checks that qty is not less than 1 and then checks if the product is already in the basket\
If the product is in the basket already, then the method will update the basket adding the total price and quantity onto that product in the basket.\
If however the item is not already in the basket then the method will simply add the product, quantity and total price to the basket.

Finally in the Food class is the class method delete_from_basket which takes two arguments cls and key. This method has only one line of code which simply takes whichever key is passed to it and deletes that from the basket dict.

##### Child Classes (Burgers, Not_Burgers, Desserts, Drinks, Milkshakes):

The five child classes are all identical, they have the Food class as the parent, and then simply one just a init method which takes in self, product and price. This does the same with these arguments as the Food class. Also within this method is another init method which is used with the super function to initialize the attributes of the parent class, in this case product and price.

##### Class Instantiation

At the bottom of the file are each of the class instantiations. Each one is an individual product on the menu and these are seperated into 5 sections based on the menu they are assigned to.\
Any alterations to the menu can be made here, as this is where the name of each product and the prices are passed as parameters when the classes are called



#### requirements.txt
#### table.py
#### test_project.py
#### theme.json